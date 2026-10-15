---
type: step
description: "Folder convention + metadata file, automatic scan of mounted disks, artwork."
phase: "[[phase-4-games]]"
step: "4.3"
status: in-progress
legacy: "ROADMAP.md 4.3"
tags: [step, phase-4]
---
# 4.3 Local DRM-free games

Up: [[phase-4-games]] · Status: **in-progress**

- **Deliverables:** folder convention + metadata file, automatic scan of mounted disks, artwork.
- **Scope (owner, 2026-10-11, [[games-on-disk]] and [[wave-1-scope]]):** `Games` (or its translated
  name) on every disk; one folder per game with any sub-folders, searched recursively for what to
  start (Linux executables, `.sh`, AppImage; Windows `.exe` → 4.5) or to install (→ 4.6);
  optional `cover.jpg` / `cover.png` and `game.txt`; when the choice is not clear, the console
  asks once with the controller and remembers (helpers, uninstallers, redistributables such as
  DirectX or Visual C++ are never offered). "Add games" → "From a USB stick or disk" explains it.
- **Minimal mounting (owner, 2026-10-15):** external disks (USB) are mounted automatically, **read
  only**, just enough for the console to find and start the games on them (the console's own disk
  has no room for test games). Everything else of disk mounting stays in
  [[step-6.5-automatic-disk-mounting]] (read-write, internal disks, Windows disks left dirty,
  notices, moving games). The plan is not reordered.
- **Demo proposal agreed (owner, 2026-10-15):** a disk with a `Games` folder plugged in → the
  notice "USB disk connected: N games found" (3.11), its games in the library as "Local"; title =
  the folder's name as written (or `game.txt`), cover from `cover.jpg` / `cover.png` or generated;
  unplugged → its games leave the library. One file to start → A starts it; several → at the
  first start "Which file starts {game}?" (name and folder of each, chosen with the controller,
  remembered), changed later from Options → "Choose the file to start"; uninstallers,
  configurators and redistributables never listed. Details show the disk. **Windows games are not
  shown until step 4.5, folders with only an installer not until step 4.6.** Demo:
  `design/demos/4.3-games-on-disk.html`.
- **Demo approved (owner, 2026-10-15).** Code written 2026-10-15 (owneet-base 0.0.32,
  owneet-frontend 0.18.0; design: [[frontend-disk-games]]); checked in the preview
  (`tools/preview-steps/library-disk.txt`). A disk without a games folder gives no notice.
  `game.txt` format agreed (owner, 2026-10-15, [[games-on-disk]]). Update on the OWNEETLOG stick;
  waiting for the FrankenPC test with the owner's SSD (`SSD-256GB-D`, `Giochi/`).
