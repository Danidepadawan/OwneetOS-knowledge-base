---
type: technical-analysis
description: "API and design of the controller pointer in owneetd (step 4.7): one window, the controllers read without a grab, the virtual mouse, gamescope's focused window and the text cursor."
component: owneetd
tags: [technical-analysis, owneetd, api, input]
---
# owneetd: the controller as a mouse (step 4.7)

Up: [[owneetd-design]] · Behaviour: [[controller-input-map]], [[step-4.7-controller-pointer]] ·
Code: `daemon/internal/pointer/`, `daemon/internal/vinput/retry.go`, `daemon/internal/apps/screen.go`

| Method | Path | What |
|---|---|---|
| GET | `/v1/pointer` | `{on, app, reason}` (reason when off: `user`, `window`, `closed`) |
| POST | `/v1/pointer` | `{"on": true, "app": id}`: on for that running app's next window (the interface then resumes it); `{"on": false}`: off. 204; 404 `apps.unknown`; 503 `pointer.unavailable` (no virtual mouse, or no gamescope X server) |

Events: `pointer.changed` (the status above), `pointer.type` `{app, reason}` (`button`: Y;
`field`: a click on a text field): owneetd has brought the home screen up; the interface opens
the console's keyboard, then `POST /v1/input/text` once the window is back (Resume).

## How it works

- **One window:** on, it waits for the app's window on screen (`GAMESCOPE_FOCUSED_APP` = the
  app's gamescope id, read every 200 ms on the root window of gamescope's Xwayland) and holds for
  `GAMESCOPE_FOCUSED_WINDOW` then. The home screen on screen: it waits (nothing moves). Another
  window of the app (the game after its launcher) or another app: off (`window`); the app gone:
  off (`closed`).
- **Controllers:** every `/dev/input/event*` gamepad (`gamepad.IsGamepad`), read without a grab
  (the app gets every input as always), rescanned every 2 s; Steam's virtual controller (vendor
  `28de`, "virtual") and owneetd's own virtual devices are ignored. Controls from
  SDL_GameControllerDB (buttons `bN`, axes `aN` in the order of their codes without the hats,
  hats `hN.M`, `+ - ~`), else the drivers' usual layout (A `BTN_SOUTH`, X `BTN_NORTH`, Y
  `BTN_WEST`, sticks `ABS_X/Y`, `ABS_RY`, D-pad hat or `BTN_DPAD_*`); axes scaled by their range
  (`evdev.AbsRange`, EVIOCGABS).
- **Movement** (every 8 ms): left stick past a 0.15 dead zone, speed `0.25 + 1.1 × push²` pixels
  per ms (fractions kept); D-pad 6 px, held: after 360 ms every 40 ms; right stick past half: a
  wheel notch every 160 ms (up = up). A: left click; X: right click; Y: `pointer.type`.
- **Text field:** 120 ms after a click, XFixes `GetCursorImageAndName`: the cursor named `text`,
  `xterm`, `ibeam` or `vertical-text`, or a nameless one (Wine / Proton) whose visible pixels are
  at least 1.4 times taller than wide and mirrored left to right (85 %): `pointer.type`
  (`field`). Limits: selectable text in Chromium-based launchers may show the same cursor (B
  closes the keyboard); apps drawing their own pointer need Y.
- **Virtual mouse:** `vinput.Retrying`: owneetd may start before logind gives `/dev/uinput` to the
  active session (`uaccess`), so it tries again every 3 s (the FrankenPC logged "permission
  denied" at every start until 2026-10-19); `/v1/input/*` answer 503 `input.unavailable` until then.
- `apps.Manager.AppIDOf` and `ShowHome` (screen.go) are what the pointer needs from the apps; the
  pointer lives in its own package so the merge with `feature/step5_media` (which changed
  `gamepad/manager.go`) stays simple.
