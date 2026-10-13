---
type: technical-analysis
description: "owneetd design: Go vs Rust, privileges, Unix socket transport, API conventions, open points."
component: owneetd
status: approved
legacy: "docs/daemon-design.md"
tags: [technical-analysis, owneetd]
---
# owneetd — design (draft for roadmap step 2.1)

Status: **approved by the owner on 2026-10-07**: Go, HTTP over a Unix socket, user service (not root).
The API list is a draft that grows step by step (phase 2).

`owneetd` is the OwneetOS system daemon ([[architecture-stack]]): it owns the controllers and
the Guide button, provides the on-screen keyboard's virtual input, manages Wi-Fi, Bluetooth, audio
and power, and launches and closes games and apps. The console UI (Pegasus fork) and later the
installer and the overlay talk to it.

Decision: [[owneetd]] · Practices: [[go]]

## 1. Language: Go or Rust

Both produce a single binary, both are memory-safe, both have what `owneetd` needs. The table
compares what matters for this daemon.

| | Go | Rust |
|---|---|---|
| Static single binary | Trivial (`CGO_ENABLED=0`) | Possible (musl target); harder as soon as a C library is involved |
| Idle memory (typical daemon of this kind) | ~10–20 MB | ~2–6 MB |
| Binary size | ~8–15 MB | ~2–6 MB |
| D-Bus (NetworkManager, BlueZ, logind) | `godbus/dbus` (mature, pure Go) | `zbus` (excellent, pure Rust) |
| Bluetooth (BlueZ) | Plain D-Bus calls (BlueZ's API is small); `go-bluetooth` exists but is less maintained | `bluer`, the BlueZ project's own Rust library |
| Controllers (evdev) and virtual input (uinput) | `holoplot/go-evdev`, `bendahl/uinput` (pure Go) | `evdev` crate (input and virtual devices, pure Rust) |
| Audio (PipeWire) | PulseAudio protocol via `pipewire-pulse`: `jfreymuth/pulse` (pure Go, volume + events) | PulseAudio/PipeWire bindings wrap C libraries (breaks the pure static build), or a pure client written by us |
| HTTP server | Standard library | `hyper`/`axum` (more dependencies) |
| Build time in CI | Seconds | Minutes |
| Learning curve for new contributors | Low | High |

**Assessment.** Rust uses less memory and has the best Bluetooth library; Go is simpler to build,
to keep static, and to contribute to, and its pure-Go audio client avoids C bindings. The memory
difference (~10–15 MB) is about 2–3 % of the 500 MB idle target (C1). **Recommendation: Go**,
mainly for build simplicity and for the second developer and future contributors. Rust remains a
good choice if the owner prefers the lowest possible footprint.

## 2. Process split and privileges

`owneetd` runs as a **systemd user service of the console user `owneet`**, inside the console
session, **not as root**:

| Needs | How it works without root |
|---|---|
| Read controllers (evdev) | Console user is in the `input` group; logind already grants access to gamepads |
| Virtual keyboard/mouse (uinput) | udev rule giving the console session access to `/dev/uinput` |
| Wi-Fi (NetworkManager) | NetworkManager lets the active local session scan, connect and switch Wi-Fi (polkit). Saving a network for the whole system needs one polkit rule (checked in 2.6, see Network) |
| Bluetooth (BlueZ) | BlueZ's default D-Bus policy already lets any local user call it (checked in 2.5): no extra rule |
| Audio (PipeWire) | PipeWire runs in the user session anyway: the daemon must be there too |
| Power (logind) | logind lets the active local session shut down, restart, suspend |
| Launch games and apps | Must run in the session, with the compositor's environment |

Operations that really need root later (installer, system updates, disk mounting policy) get their
own small privileged helpers with a narrow D-Bus/polkit interface, decided in their steps. A bug in
`owneetd` therefore cannot touch the system beyond what the console user can do.

## 3. Transport and security

**HTTP + JSON over a Unix socket** at `$XDG_RUNTIME_DIR/owneetd.sock` (`/run/user/1000/owneetd.sock`),
permissions `0600`, owned by `owneet`. No TCP port.

- Why not a localhost TCP port (as first written in the rules): any web page open in Brave could
  send requests to `http://127.0.0.1:PORT` (CSRF) and, for example, power the console off or
  connect to a Wi-Fi network. A Unix socket cannot be reached by web pages at all.
- The console UI is our Pegasus fork: a small C++ QML plugin (`QLocalSocket`) talks to the socket
  (decided in step 3.8, [[frontend-architecture]]).
- `owneetctl`, a tiny command-line client, is used by scripts and tests (`owneetctl get /v1/status`).
- Only processes of the console user can connect. No tokens needed.

## 4. API v1 (draft)

Conventions: JSON bodies; `/v1` prefix; errors as `{"error": {"code": "wifi.wrong_password",
"message": "…"}}` with a proper HTTP status. **`code` is stable and is what the UI translates**
(no UI text comes from the daemon — [[languages]]). `message` is English, for logs.

One note per area:

- [[owneetd-api-status|Status]]
- [[owneetd-api-controllers|Controllers]]
- [[owneetd-api-bluetooth|Bluetooth — implemented (2.5)]]
- [[owneetd-api-network|Network — implemented (2.6)]]
- [[owneetd-api-audio|Audio — implemented (2.7)]]
- [[owneetd-api-power|Power — implemented (2.8)]]
- [[owneetd-api-apps|Apps and games — implemented (2.9)]]
- [[owneetd-api-display|Display — implemented (3.9, part 3)]]
- [[owneetd-api-input|Virtual input (on-screen keyboard) — implemented (2.4)]]
- [[owneetd-api-events|Event stream]]

## 5. Open points for later steps

- The PC's power button keeps logind's default (shut down) for now; a console-like behaviour
  (e.g. short press = suspend) is decided with the UI.
- **Steam in the session (4.2, checked in the test VM):** started with `GAMESCOPE_WAYLAND_DISPLAY`,
  Steam binds gamescope's control protocol and writes `GAMESCOPECTRL_BASELAYER_APPID` itself
  (its own ids, e.g. `413091,769`): its window stays hidden and owneetd loses control of the
  screen. Started **without** that variable it is an ordinary window: owneetd tags it and brings
  it to the front, and Steam leaves the property alone. owneetd starts Steam that way.
- Which privileged helpers exist and their interfaces — installer (6.3), updates (7.1), disks (6.5).
- Configuration file format and location — step 2.2.
