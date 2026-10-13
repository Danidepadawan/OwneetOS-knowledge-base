---
type: step
phase: "[[phase-3-frontend]]"
step: "3.5"
status: done
legacy: "ROADMAP.md 3.5"
tags: [step, phase-3]
---
# 3.5 Navigation and input map

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** spatial navigation and the global input map ([[controller-input-map]]) implemented once and shared by every screen.
- **Outcome:** in C++, the gamepad and keyboard map of [[controller-input-map]] (LB/RB = sections, LT/RT =
  filters, Y = page option, X = secondary, Menu = options; keyboard fallback keys), the right
  stick as fast scrolling (new `scroll-up/down` keys; it no longer moves the selection like the
  left stick), repeat timing of demo 3.3 (360 ms, then 140 ms; scrolling 90 ms), and a fixed map
  (key bindings no longer saved or read from the settings file). In QML (`foundation/`): `Nav`
  turns key events into actions (held buttons act once; directions and scrolling repeat), finds
  the nearest item in a direction (spatial navigation, as in the demo) and handles lists;
  `NavArea` gives any screen or window spatial navigation, A and B; `Nav.feedback(kind)` reports
  move, edge, confirm, back, section, tab, toggles and windows for the sounds of 3.12. Windows
  (`Sheet`) and the pickers now use them. Buttons with no use on a screen do nothing (LB/RB/LT/RT
  report "edge"). New `tools/frontend-preview` runs the frontend in the builder VM with test games
  and a virtual controller, following a step list (`tools/preview-steps/`), and saves
  screenshots: checked there with keyboard, D-pad, right stick and buttons.
- **Fix (2026-10-09, found by the owner on the ISO with an Xbox controller):** LT / RT switched
  filters without end. Analog triggers send a stream of values and every value above 0 counted as
  a new press. Now a trigger is pressed above half its travel and released below a quarter, and
  only changes are reported (owneet-frontend 0.7.2). The preview's virtual controller now pulls
  triggers like real ones (`tools/preview-steps/triggers.txt`). Hardware check batched with the
  next test.
- **Held buttons (2026-10-09, owner's choice after demo 3.7):** LB / RB and LT / RT repeat while
  held, after 0.72 s then every 0.36 s (directions: 0.36 s then 0.14 s); a keyboard's own repeat
  is held to the same pace. Checked with the virtual controller (`tools/preview-steps/held.txt`).
