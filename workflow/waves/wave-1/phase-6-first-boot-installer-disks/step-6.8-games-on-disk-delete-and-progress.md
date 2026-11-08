---
type: step
description: "Deleting a game or an installer from a disk with the controller, and a Windows installer that says how much it has written and when it seems stuck."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.8"
status: in-progress
tags: [step, phase-6]
---
# 6.8 Games on disk: deleting them, and the progress of Windows installs *(added 2026-11-08)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **in-progress**

- **Why (owner's test on FrankenPC, 2026-11-08):** after moving his games to the 2 TB disk he could not remove their installers:
  the console had no way to delete files from a disk (only Uninstall, which keeps the installer, [[step-4.6-installers]]). The
  install of The Witcher 2 (GOG for Windows, 7 parts, about 20 GB) showed the download Windows games need the first time, then
  nothing that said whether it was working, stuck or failed (no log of that session: OWNEETLOG was not plugged in at start-up).
  Owner: "Non possiamo lanciare Owneet in questo stato penoso"; both now.
- **Deliverables (owner, 2026-11-08):** Options → **"Delete from disk"** for a game on a disk and for an installer, and
  **"Delete the installer"** for a game installed from it (the game stays); each asks first, Cancel selected; never Steam games
  (Steam's storage, [[disks]]) nor a read-only disk. A Windows installer shows **what it has written** ("Installing · 7.4 GB
  written", on the cover and in the home screen's notice) and, after **10 minutes without writing**, a banner and the cover say it
  **seems stuck** (Options: Stop installing). No new dependency (the percentage would need innoextract, given up on 2026-10-19).
  Also the owner's report: in a window whose buttons take two rows, left and right did not stay on the row.
- **Recorded as one step** (both are about games on disks), asked by the owner together.
- **Demo:** `design/demos/6.8-games-on-disk.html`. **Owner (2026-11-08):** one label, **"Uninstall"**, for every game on a disk that is not
  Steam's, games on the console's own disk included (the text says what goes: its folder, or the copy installed); **"Delete the installer"**
  apart. Demo updated so, **approved**.
- **Found on the way:** Uninstall was refused for a game installed and then moved to another disk (owneetd accepted only the home
  folder's games folder): now any games folder of the home folder or of a disk the console mounted.
- **Built (2026-11-08, code commit 06fede4):** owneetd 0.25.1 (`POST /v1/installs/delete`, `/v1/installs/delete-installer`, error
  `installs.read_only`; a Windows install's `done` measured every 5 s, `stalled` and the event `install.stalled` after 10 minutes
  without writing); owneet-frontend 0.38.0 (Options, the two windows with Cancel selected, the state line and the home notice with the GB
  written, the notice when stuck, texts in the five languages; `rowsHold` in Dialog: left / right stay on the row). Go tests for
  every refusal (outside a games folder, links, a running game, read only), both kinds of installers, and the stalled install.
  **Checked in the test VM:** Options on two rows, the installer deleted in a folder of its own (the game stays, the mark forgets it), a
  game ready to start uninstalled from its disk. Not checkable there: a real Windows install (FrankenPC, The Witcher 2).
  OWNEETLOG updated. **Waits for the owner's test.**
- **Owner's test on FrankenPC (2026-11-08, OWNEETLOG log `owneet-20261108-183027`):** (1) the installers deleted: done; (2) Uninstall
  works, but after an uninstall in the filter "Local" the list looked empty for a moment; (3) The Witcher 2: no GB written, a banner
  said to try again, then "Not installed" again.
  - **(2)** Every reading of the games rebuilt every cover of the library's grid, and a new cover shows nothing until it is drawn. The
    grid now keeps one row per game (by its key) and changes only the rows that change: the covers that stay are kept. The selection
    goes to the first place as before.
  - **(3)** Two faults, see [[windows-installer-folder-with-a-colon]]: the game's folder "The Witcher 2: Assassins of Kings…" has a
    ":", which Windows refuses (Inno Setup ended at once with code 3), and owneetd took that 3 for "Windows games are not ready".
    Now an installer gets a folder through a link without such characters, and owneetd checks Proton itself.
  - **Fixed (code commit 5c3125e):** owneetd 0.25.2, owneet-frontend 0.38.1; Go tests for both faults; the grid checked in the test VM
    (uninstall in "Local", the covers stay). OWNEETLOG updated. **Waits for the owner's test** (The Witcher 2 again).
