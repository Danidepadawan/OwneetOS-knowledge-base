---
type: step
description: "Folder convention + metadata file, automatic scan of mounted disks, artwork."
phase: "[[phase-4-games]]"
step: "4.3"
status: done
legacy: "ROADMAP.md 4.3"
tags: [step, phase-4]
---
# 4.3 Local DRM-free games

Up: [[phase-4-games]] · Status: **done**

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
- **FrankenPC test 1 (2026-10-15):** the SSD (USB-SATA adapter with UAS) was not mounted: the udev
  rule asked for `ID_BUS` "usb", the adapter gives "ata". Fixed in owneet-base 0.0.33 (USB by the
  device's path); the test report now lists the disks.
- **FrankenPC test 2 (2026-10-16):** the SSD is mounted; plugging, unplugging and plugging again
  add and remove its games with their notices. (1) Plugging it showed the black loading screen
  with the logo before the notice: the owner expects only the notice, as in a real OS → the
  games are now read again quietly, the interface stays on screen (owneet-frontend 0.18.1,
  [[frontend-disk-games]]). (2) Beneath a Steel Sky starts (GOG's ScummVM), but it is a game made
  for a mouse; ScummVM could not write its settings file in the game's folder (read-only disk).
  (3) CAYNE does not show up: Unity stops after finding the controller, the console stays on the
  home screen, the disk keeps working; the owner switched off after about a minute → the test
  report now lists the busiest processes and disk reads, and copies Unity's `Player.log`
  (owneet-base 0.0.34); `owneet-xprobe` on the stick. Beneath a Steel Sky: the owner decided to
  leave games made for a mouse and keyboard as they are ([[games-on-disk]], 2026-10-16).
- **FrankenPC test 3 (2026-10-16):** plugging the SSD gives only the notice (quiet reading OK).
  CAYNE runs (Unity 5.4 initialises, its 1440×900 window is mapped) but stays behind the home
  screen: its window has no `_NET_WM_PID`, so owneetd never tagged it for gamescope; the home
  screen, still on screen, did not answer because the interface had paused the controller at the
  launch → owneetd 0.12.9 finds a window's process through X-Resource when `_NET_WM_PID` is
  missing (checked on Xvfb); owneet-frontend 0.18.2 pauses the controller only when a game is
  really on screen.
- **FrankenPC test 4 (2026-10-16):** everything works: CAYNE comes on screen, Home goes back and
  forth, the game closes from the console. **Step approved by the owner (2026-10-16).**
  Covers of games on disks are already drawn (4.3); the rest of artwork is step 4.4.
