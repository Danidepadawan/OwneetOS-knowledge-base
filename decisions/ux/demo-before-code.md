---
type: decision
description: "Mockups and an interactive HTML demo approved by the owner before any screen's code."
area: ux
status: active
decided: 2026-10-03
updated: 2026-10-08
legacy: "PROJECT_RULES.md §9 (mockups, interactive demo)"
tags: [decision, ux, process]
---
# Mockups and interactive demos before UI code

- **Mockups are approved by the owner before UI code is written.**
- **Interactive demo before each screen:** before the code of each screen is written (controller
  pairing, home, library, settings, on-screen keyboard, …), the owner gets an interactive demo of
  that screen (HTML, usable with keyboard and gamepad in a browser) to adjust details first. The
  screen is implemented only after the owner approves its demo.
- Demos live in `design/demos/` of the code repository ([[mockups-and-demos]]).

Guard: [[collaboration]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Next step: UI mockups for owner approval, then repo structure and builder VM. |
| 2026-10-08 | Each screen gets an interactive demo approved by the owner before its code is written ([[design-direction]]). |
