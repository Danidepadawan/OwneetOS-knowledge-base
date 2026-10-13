---
type: step
phase: "[[phase-2-system-daemon]]"
step: "2.5"
status: done
legacy: "ROADMAP.md 2.5"
tags: [step, phase-2]
---
# 2.5 Bluetooth

Up: [[phase-2-system-daemon]] · Status: **done**

- **Deliverables:** BlueZ over D-Bus: list, pair, trust, forget; **automatic gamepad pairing
  mode** (accept any device that identifies as a gamepad, no input needed).
- **Done when:** a real controller pairs with zero input on real hardware (VM Bluetooth is unreliable).
- **Progress:** `internal/bluetooth`: BlueZ over D-Bus (`godbus/dbus` v5.2.2, BSD-2-Clause, vendored
  with `golang.org/x/sys`; licences shipped in `/usr/share/licenses/owneetd/`). Auto-pair turns on
  by itself whenever no controller is connected (any connection) and off as soon as one is: adapter
  powered, scan, every device that identifies as a gamepad (class of device, LE appearance or BlueZ
  icon) is paired, trusted and connected. Pairing agent `NoInputNoOutput`: accepts only gamepads
  while auto-pair is on, re-registers when bluetoothd (re)starts; BlueZ is never D-Bus-activated
  (no journal noise without an adapter). API `GET /v1/bluetooth`, `POST /v1/bluetooth/auto-pair`,
  connect / disconnect / forget; events `bluetooth.*`. Unit tests with a fake BlueZ (policy, agent,
  no adapter) and API tests; race detector clean. **Test VM (no adapter):** `adapter: false`, clean
  log, no failed units; owneetd ~18 MB RSS (9.7 MB anonymous + 8.2 MB binary pages). The
  diagnostics report (tty9) shows owneetd's controllers and Bluetooth state and its log, and
  refreshes with Enter.
- **Outcome on real hardware (2026-10-07, NiPoGi E3B, owner's Xbox Wireless Controller over
  Bluetooth LE):** live ISO, no controller connected → auto-pair on at boot; controller put in
  pairing mode → paired, trusted and connected in 5 s with no input (`pairing gamepad` 18:04:05,
  `controller connected … guide=true` 18:04:10), auto-pair off; controller switched off and on →
  reconnected by itself in 4 s. Fixed after the test: the report used `bluetoothctl`, which fails
  without a terminal (showed "no adapter"; now it asks owneetd); Bluetooth LE controllers were named
  `bluez-hog-device` (now BlueZ's device name is used); `poweroff` from the diagnostics shell waited
  90 s for the shell to exit (now 3 s; normal shutdown was not affected). Approved by the owner;
  the re-test of these fixes on real hardware is postponed.
