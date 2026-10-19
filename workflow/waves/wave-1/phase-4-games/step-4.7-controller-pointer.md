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
  Connect: 4.2). Offered automatically when such a window is on screen, never needed elsewhere.
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
