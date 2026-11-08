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
- **Demo:** `design/demos/6.8-games-on-disk.html` (code commit on `feature/phase7`), waiting for the owner's approval.
