---
type: step
phase: "[[phase-2-system-daemon]]"
step: "2.3"
status: done
legacy: "ROADMAP.md 2.3"
tags: [step, phase-2]
---
# 2.3 Controller input

Up: [[phase-2-system-daemon]] · Status: **done**

- **Deliverables:** evdev discovery and hot-plug, SDL_GameControllerDB mapping, Guide button
  detection, controller battery level, event stream to clients.
- **Done when:** a virtual gamepad (uinput) in the test VM produces the expected events in automated tests.
- **Progress:** `internal/gamepad` (scan + inotify hot-plug, no grab), Guide from `BTN_MODE` or
  SDL_GameControllerDB (pinned, shipped in `owneetd`), `KEY_HOMEPAGE` companion devices, battery
  from sysfs power_supply; `GET /v1/controllers`, events `controller.added/removed/battery` and
  `guide.pressed`. Integration tests create real virtual controllers through `/dev/uinput` (Xbox-like
  pad: hot-plug, Guide, removal; generic pad: Guide found through the database): pass in the builder
  VM, run by `tools/lint` and CI. **Real controller (2026-10-07):** the owner's Xbox Wireless
  Controller (Bluetooth, passed to the test VM) is listed as brand `xbox`, connection `bluetooth`,
  Guide available; 3 presses of the Xbox button gave exactly 3 `guide.pressed` events, other
  buttons none. (In the VM the id is the virtio path: the Bluetooth address is not passed through.)
