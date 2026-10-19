---
type: step
description: "A pointer moved by the controller (stick, A = click) for the few windows made only for a mouse: unknown installers (4.6), launchers…"
phase: "[[phase-4-games]]"
step: "4.7"
status: in-progress
legacy: "ROADMAP.md 4.7"
tags: [step, phase-4]
---
# 4.7 Controller pointer *(added 2026-10-11)*

Up: [[phase-4-games]] · Status: **in-progress**

- **Deliverables:** a pointer moved by the controller (stick, A = click) for the few windows
  made only for a mouse: unknown installers (4.6), launchers inside some games (EA app, Ubisoft
  Connect: 4.2). ~~Offered automatically when such a window is on screen~~ (owner, 2026-10-19:
  turned on by hand, see below), never needed elsewhere.
  Its buttons go into [[controller-input-map]] before it is implemented.
- **Never in games** (owner, 2026-10-16, [[games-on-disk]]): games made for a mouse and keyboard
  are left as their developers made them.
- **Started (owner, 2026-10-19)** while step 4.6 waits for its test (tested together). First:
  the pointer's buttons in [[controller-input-map]] with the owner, then the demo proposal.
- **Agreed (owner, 2026-10-19, [[controller-input-map]]):** turned on by hand from the console
  (Guide), on apps and launchers, never on games; left stick moves, D-pad small steps, A click,
  X right click, right stick wheel, Y types (the console's keyboard, then the text goes to the
  window). Nothing intercepted (no grab), compatible with the guard. Danidepadawan's branch
  (`feature/step5_media`, local copy of 2026-10-16) has no pointer work: the pointer goes in its own
  package to keep the merge simple (`gamepad/manager.go` changed there). The way it is explained
  to the user must be elegant and not annoying (owner): in the demo. Also to fix: owneetd opens
  `/dev/uinput` before the session is active and never tries again (the FrankenPC logs "virtual
  keyboard and mouse not available" at every start).
- **Demo proposal agreed (owner, 2026-10-19):** launchers run as part of their game, so "Resume
  with the pointer" is offered on the running game or app's card on the home screen; the pointer
  holds for one window and turns off by itself when another window takes the screen (the game
  after its launcher) or the app closes; with it on, the card has a "Pointer on" badge and "Turn
  the pointer off". Explained elegantly: once, a compact card with the controller drawing and a
  label at each button ("Got it", "Don't show again"), and always in the quick menu's Controls
  (3.13). Y opens the console's keyboard on the home screen ("Type in {app}"), Send types the text
  into the window and goes back with the pointer still on.
- **Demo approved (owner, 2026-10-19):** `design/demos/4.7-controller-pointer.html` (the running
  game's card with "Resume with the pointer" / "Turn the pointer off" and the "Pointer on" badge,
  the explanation card once, the keyboard for typing, Controls in the quick menu). One change,
  agreed without a new demo (no new screen): **A on a text field opens the keyboard by itself**
  when the pointer has the text "I" shape after the click (read through XFixes on gamescope's
  Xwayland; verified only on the FrankenPC); Y stays as the fallback. Known limits told to the
  owner: selectable text in Chromium-based launchers may open it (B closes), apps that draw their
  own pointer need Y.
- **Code (2026-10-19):** owneetd 0.16.0 (`internal/pointer`, `/v1/pointer`,
  [[owneetd-api-pointer]]; `vinput.Retrying` fixes the virtual keyboard and mouse never made on
  the FrankenPC; XFixes vendored from the same `jezek/xgb` module, with its `render` and `shape`);
  owneet-frontend 0.23.0 (the card's "Resume with the pointer" / "Turn the pointer off" and badge,
  the explanation once with the controller drawing and "Don't show again", the keyboard asked by
  owneetd with Send / Cancel, Controls in the quick menu, the `ls` glyph, the `pointer` icon).
  Verified: Go tests (one window, home screen waits, off on another window or when the app
  closes, speeds, D-pad repeat, wheel, buttons, the text cursor's shape, SDL mappings, ignored
  virtual pads), `tools/lint`; the preview (`tools/preview-steps/pointer.txt`, new `@gamescope`).
  Only on the FrankenPC: a real launcher, the pointer's speed, gamescope's cursor, the text
  cursor read through XFixes, typing into a Proton window.
