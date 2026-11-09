---
type: step
description: "Evdev discovery and hot-plug, SDL_GameControllerDB mapping, Guide button detection, controller battery level, event stream to clients."
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
- **Reported by the owner (FrankenPC, 2026-11-09), open:** Settings → Controllers and Bluetooth lists two controllers, "Xbox
  Wireless Controller" and "Microsoft X-Box 360 pad 0", with one Xbox controller over Bluetooth (a generic USB dongle). Not the
  dongle: the second is **Steam's virtual controller** (Steam Input), made with uinput about 20 s after Steam starts and gone when
  it closes (`/devices/virtual/input/input20`; owneetd: "controller connected" id=event16, guide=true, 2026-11-09 00:09:05 and
  09:30:00). owneetd takes it as a controller, Guide included. To fix (accepted by the owner, 2026-11-09): controllers made by a program through uinput (under
  `/devices/virtual/input`) are not listed nor read; a Bluetooth controller (uhid, `/devices/virtual/misc/uhid/…`) stays.
- **Fixed (2026-11-09; owneetd 0.25.8):** a device made by a program through uinput (`/sys/devices/virtual/input/…`) is neither
  listed nor read: Steam's virtual controller, other programs' virtual keyboards (whose Super would be Guide), owneetd's own. A
  Bluetooth controller (uhid) and USB controllers stay; so do the project's test devices (names starting "OwneetOS Test":
  owneet-testpad, the uinput integration tests, which still pass). Go test with a fake sysfs (Steam's pad, a Bluetooth and a USB
  controller, a test pad, owneetd's keyboard). **Waits for the owner's test on FrankenPC:** Settings → Controllers and
  Bluetooth with Steam open shows one controller.
