---
type: technical-analysis
component: owneetd
legacy: "docs/daemon-design.md §4 Display"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Display — implemented (3.9, part 3)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/display` | `available` (gamescope session), `screens` (`id`, `connector`, `name`, `internal`, `active`), `modes` of the screen in use (`"1920x1080@60"`, preferred first; none for a laptop's built-in screen), `mode` (`auto` or one of them), `brightness` (0-100, only when the screen allows it), `pending` (`kind`, `seconds`) |
| PUT | `/v1/display/screen` | `{"id": "card1-HDMI-A-1"}` — move the console to that screen (gamescope restarts; refused while a game or app is open) |
| PUT | `/v1/display/mode` | `{"mode": "1920x1080@60"}` or `"auto"` — applied at once |
| POST | `/v1/display/confirm` · `/revert` | Keep the change waiting for confirmation, or go back now |
| PUT | `/v1/display/brightness` | `{"value": 0-100}` |

Errors: `display.unavailable` (503), `display.not_gamescope` (409), `display.unknown_screen`
(404), `display.unknown_mode` (400), `display.apps_open` (409), `display.not_pending` (409),
`display.no_brightness` (409), `display.failed` (502).

- **One screen at a time** ([[screens-and-display]], decision of 2026-10-10). gamescope drives one
  screen and turns off the others on its graphics card. The screen and its card are chosen when
  gamescope starts (`--prefer-output`, `--prefer-vk-device`): owneetd writes them to
  `~/.config/owneet/display.conf`, which `owneet-session` reads, and stops gamescope (a marker
  file tells `owneet-session` the stop was wanted). Screens are read from sysfs
  (`/sys/class/drm`: status, EDID names with hwdata's `pnp.ids`, the card's PCI ids).
- **Other graphics cards:** `owneet-screens-off@CARD.service` (root, `/usr/lib/owneet`) becomes DRM
  master of every card but the console's, turns their outputs off and holds them until stopped.
  owneetd starts and stops it over systemd's D-Bus API; a polkit rule allows only these units,
  only start and stop, only to the console user in the active local session.
- **Modes**, as Steam does on SteamOS: gamescope publishes the screen's modes in
  `GAMESCOPE_DISPLAY_MODE_LIST_EXTERNAL`; owneetd writes the choice to gamescope's
  `GAMESCOPE_MODE_SAVE_FILE` (`~/.config/owneet/gamescope-modes`, "Make Model:WxH@Hz") and sets
  `GAMESCOPE_DISPLAY_MODE_NUDGE`: gamescope applies it at once and keeps it for that screen.
- **"Keep this?":** a new screen or mode goes back after 15 seconds without `confirm`; for a new
  screen the time starts once the console is back on screen. Events `display.pending`
  (`kind`, `seconds`), `display.confirmed`, `display.reverted`, `display.changed` (the status, also
  on hot-plug).
- **Brightness:** a laptop's backlight through logind (`Session.SetBrightness`, allowed to the
  active session's user); monitors through DDC/CI with `ddcutil` (its udev rule gives the active
  session the I2C devices; monitors are found in the background, values are sent one at a time).
- **Keyboard layout:** `PUT /v1/input/layout` also sets the layout of physical keyboards:
  `GAMESCOPE_KEYBOARD_LAYOUT` at once, `XKB_DEFAULT_LAYOUT` (display.conf) when the compositor
  starts — the only way in cage.
- Tested in the test VM: gamescope (headless backend) recompiles its keymap after a layout change,
  `owneet-screens-off` turns the VM's screen off and gives it back, `owneet-session` restarts
  gamescope without counting a failure, the polkit rule refuses other units and verbs.
