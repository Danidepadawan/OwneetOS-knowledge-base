---
type: step
phase: "[[phase-4-games]]"
step: "4.3"
status: todo
legacy: "ROADMAP.md 4.3"
tags: [step, phase-4]
---
# 4.3 Local DRM-free games

Up: [[phase-4-games]] · Status: **todo**

- **Deliverables:** folder convention + metadata file, automatic scan of mounted disks, artwork.
- **Scope (owner, 2026-10-11, [[games-on-disk]] and [[wave-1-scope]]):** `Games` (or its translated
  name) on every disk; one folder per game with any sub-folders, searched recursively for what to
  start (Linux executables, `.sh`, AppImage; Windows `.exe` → 4.5) or to install (→ 4.6);
  optional `cover.jpg` / `cover.png` and `game.txt`; when the choice is not clear, the console
  asks once with the controller and remembers (helpers, uninstallers, redistributables such as
  DirectX or Visual C++ are never offered). "Add games" → "From a USB stick or disk" explains it.
