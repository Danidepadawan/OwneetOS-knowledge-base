---
type: meta
description: "Handoff of the AI session on step 5.2 (2026-10-16) from the Mac to the Arch PC: state, the open bridge bug, how to test in the VM, working agreements. Read first when resuming 5.2; delete when 5.2 is done."
tags: [meta, handoff]
---
# Handoff — step 5.2, moved to the Arch PC (2026-10-16)

For the AI session that continues [[step-5.2-extension-core]] on the owner's Arch PC (the machine
that runs the builder and test VMs). Everything below is as of commit `86b3147` (code) and the
commit that adds this note (vault), branch `feature/step5_media` in both repositories.

## Working agreements (from the previous session's memory, which stays on the Mac)

- **Commit locally in both repos as work is done**, without asking; the owner pushes. Never push.
- **The owner is a developer and reads logs.** When a command fails or "hangs", ask at once for the
  exact error / raw output and diagnose from it; no rounds of guessed workarounds.
- At the start of 5.2 the owner asked the AI **not to test in the VM or take screenshots** (to save
  tokens): the owner tests, the AI gives commands. Now that the session runs on the PC, **ask the
  owner whether to run VM commands directly**.
- [[host-safety]] still applies: nothing installed or built on the host; builds and checks only in
  the builder VM (`tools/build-in-vm …`); files only inside the project folder.

## Where 5.2 stands

Plan (agreed 2026-10-15): vault → demo → extension → bridge + owneetd → frontend → keyboard over
Brave in gamescope → packaging → close. Design: [[extension-design]]; API: [[owneetd-api-apps]].

| Part | State |
|---|---|
| 1. Vault decisions | done (bindings in [[controller-input-map]], [[architecture-stack]], [[decision-log]]) |
| 2. Demo `design/demos/5.2-web-app-controls.html` | approved; seeking (±10 s) left to 5.3 / 5.4 |
| 3. Extension (`extension/`): gamepad loop, ring, A, B chain, right stick | done; navigation tested by the owner in the VM: "solid" |
| Spatial navigation rules | agreed 2026-10-16 after comparing three versions (see [[extension-design]] "Moving"); `extension/test/spatnav.test.js` 15 tests, run by `tools/lint` |
| 4. `owneet-bridge` + owneetd `/v1/webapps/*` + manifest per profile | code done (owneetd 0.12.0); **bridge not started by Brave — open bug, below** |
| 5. Frontend: keyboard in "web" mode, "Close {name}?" on `webapp.ask_close`, look (accent, language) in the open request | not started |
| 6. Keyboard drawn over Brave in gamescope | not started; checkable on real hardware only |
| 7. Packaging, terms-of-service check, known limits, outcome | packaging current (owneetd 0.12.0, owneet-base 0.0.37) |

Part 5, open problem: in the cage session owneetd cannot bring the console in front of Brave. Idea
to verify first: the frontend hides and shows its own window (cage shows the newest window) and
hides it again on Done / Cancel.

## Open bug: Brave does not start owneet-bridge

Established in the test VM (cage session, YouTube open after a full reinstall):

- owneetd 0.12.0-1 runs; owneet-base 0.0.37; `/usr/lib/owneet/owneet-bridge` installed.
- Brave runs with `--user-data-dir=/home/owneet/.local/share/owneet/webapps/youtube` and
  `--load-extension=/usr/share/owneet/extension`; the extension works (navigation).
- `…/webapps/youtube/NativeMessagingHosts/org.owneet.bridge.json` exists; its `allowed_origins`
  id `jlekhdampjopkpjhbgilolchffjpdjcn` matches the id in the profile's preferences.
- No `owneet-bridge` process. owneetd's event stream shows `guide.pressed`, `app.started`,
  `focus.changed`, but never `webapp.keyboard` / `webapp.ask_close` (A on a text field, B on the
  first page).
- The journal has Brave errors: **not yet read** — first thing to do.

Next steps:

1. Read Brave's errors: `journalctl -b --no-pager | grep -i -E "native|messaging|extension|ERROR:" | tail -30`.
2. Start the bridge by hand as the console user (uid from `ls /run/user`):
   `printf '\x10\x00\x00\x00{"type":"hello"}' | runuser -u owneet -- env XDG_RUNTIME_DIR=/run/user/1000 /usr/lib/owneet/owneet-bridge | od -c`
   — expected: a `look` message.
3. If still unclear, make it observable: a start-up line from `owneet-bridge` in the journal, and the
   extension's background worker reporting `chrome.runtime.lastError` of `connectNative`
   (`extension/background.js` currently discards it).

## Testing in the VM: lessons from this session

- The test VM has no Vulkan: the session is **cage** by default (visible). Gamescope only with
  `--kargs "owneet.session=gamescope owneet.debug.gamescope_backend=headless"` (no picture; check
  `owneetctl get /v1/apps` → `focus`).
- `vm/test.sh run 'CMD'` types into the debug shell (`--debug-shell`) and waits for an end marker:
  **one stuck command blocks every later one**. Avoid: `$(...)` (arrived as `${...}` → "bad
  substitution", which drops the rest of the line and the marker), trailing `&`, endless streams.
- owneetd's socket as root: `--socket /run/user/*/owneetd.sock` (a glob, no substitution).
- Recording events without blocking the shell:
  `systemd-run --unit=owneet-rec -p RuntimeMaxSec=600 sh -c "owneetctl --socket /run/user/*/owneetd.sock events > /root/ev.log 2>&1"`,
  then `cat /root/ev.log`, `systemctl stop owneet-rec`.
- Keyboard state without the stream: `owneetctl --socket /run/user/*/owneetd.sock get /v1/webapps/keyboard`.
- Tools disk (`--tools out/vm-tools`) is `/dev/vdb1`; virtual gamepad:
  `/mnt/owneet-testpad -wait 4s -hold 150ms down right a`. The Super key is Guide.
- Updating the VM: `tools/build-in-vm tools/build-packages owneetd owneet-base`,
  `tools/make-update-stick`, `vm/test.sh boot --stick`. Raise `pkgver` for every rebuild the VM
  should install.

## Noted for later steps

- Netflix: hard to reach its cookie banner with the D-pad → [[step-5.4-netflix]].
- YouTube's normal site: cards with several buttons (picture, title, ⋮, channel) → [[step-5.3-youtube]]
  (TV interface).
- Known limits of 5.2 for the outcome: native `<select>` popups, cross-origin iframes.
- Test tooling: why some `;`-joined commands hung in `vm/test.sh run` was not fully explained.
