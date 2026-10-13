---
type: step
phase: "[[phase-4-games]]"
step: "4.6"
status: todo
legacy: "ROADMAP.md 4.6"
tags: [step, phase-4]
---
# 4.6 Installers *(added 2026-10-11)*

Up: [[phase-4-games]] · Status: **todo**

- **Deliverables:** installers found in a game's folder (GOG Linux `.sh`, Windows Inno Setup /
  NSIS / MSI, e.g. GOG's `setup_*.exe`) run silently in the background with their known options,
  into the console's games folder, with progress in the library; then the game appears.
- **Decided (owner, 2026-10-11):** a silent install accepts the game's licence for the user, so
  the console first shows "By installing you accept the game's licence" [Read] [Install].
- **Note:** installers of unknown kinds may only have windows made for a mouse: they need the
  controller pointer (4.7).
