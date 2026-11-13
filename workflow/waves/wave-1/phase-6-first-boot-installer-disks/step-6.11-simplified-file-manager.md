---
type: step
description: "Junk on the disks: a very simplified file manager in Settings → Advanced (places named for the user, going through folders, deleting), and the console cleaning its own system leftovers by itself."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.11"
status: todo
tags: [step, phase-6]
---
# 6.11 A simplified file manager *(added 2026-11-13)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **to do**

- **Why (owner, 2026-11-11 / 2026-11-13):** no junk may stay on the disks ([[open-items]] 3p, 3t); the system
  cannot tell by itself whether a save is still needed, so the user decides, with a simple tool.
- **Agreed (owner, 2026-11-13):**
  - A new section **Advanced** at the end of Settings, with a row that opens a **very simplified file manager**
    on the whole screen: going through folders and deleting, nothing else ([[wave-2]] 21 adds downloading,
    moving, unzipping, renaming).
  - It opens on **places**, not on technical folders: each disk's games folder; "Windows games' data" (each
    prefix with its game's name, "Game no longer here" when the game is gone); the games' logs. In a folder: a
    list with name, size and date; A opens, B goes up; Options → Delete shows the room it frees and asks, Cancel
    selected. System files are never shown.
  - **The console cleans its own system leftovers by itself:** old versions in the packages' cache (the last 2
    of each package kept) and the core dumps left by programs that crash (3p (c), (e)).
  - A Windows game removed from an internal disk takes its prefix with it ([[disks]], 2026-11-12): built with
    this step.
- **Steam's leftovers (owner, 2026-11-13):** a place "Steam's leftovers": the shader caches, Windows data
  (`compatdata`) and orphan unfinished downloads of games no longer installed, each with its game's name; installed
  games never shown; deleted only with Steam closed (Steam may be writing there). Downloads still in Steam's queue
  are cancelled from the console as today; an old Proton and Steam's old runtime are left to Steam.
- **Windows data (owner, 2026-11-13):** before deleting them (the console's prefixes and Steam's `compatdata`), a
  first question: they may hold saves and settings of the game, and cannot come back (Continue, Cancel selected).
- **Demo** `design/demos/6.11-file-manager.html` (2026-11-13): Settings → Advanced → File manager; places; a
  game's folder; Options → Delete; the saves question; Steam open or closed. Waits for the owner's approval.
- **Its look (owner, 2026-11-13):** like Windows' or Linux's file managers: folder-shaped icons in a grid, in the
  console's colours (the first round's list was not wanted). Second round of the demo: folders in the accent colour
  (the places with a small emblem), documents with their kind, a bar under the grid with the selected item's size
  and date. **Approved** (owner, 2026-11-13).
