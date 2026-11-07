---
type: step
description: "Erasing and preparing a disk other than the console's for games, with the controller: in the installer and in Settings → Disks, with a clear warning and the final confirmation."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.7"
status: in-progress
tags: [step, phase-6]
---
# 6.7 Preparing other disks *(added 2026-11-07)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **in-progress**

- **Why (owner, 2026-11-07, "gravissimo"):** the console could erase only the disk it is installed on. A new disk, one in a format the
  console cannot read, or one to turn into a better format for games needed another PC: the owner took it for granted, and no step had it.
- **Deliverables (owner, 2026-11-07):** both **in the installer** (the other internal disks) and **in Settings → Disks**, with the controller
  only; a clear warning and the final confirmation for every disk ([[user-data]], [[installer-and-firmware]]); the disk comes out ready for
  games (its Games folder, the console allowed to write on it).
- **When:** now, before everything else left (owner, 2026-11-07). **Demo first** ([[demo-before-code]]); the details are asked to the owner.
- **Choices (owner, 2026-11-07):** **ext4 only** (the best for games, Windows ones and Steam included; Windows and Mac no longer read
  the disk); from Settings → Disks **internal and USB disks**, never the console's own disk, the stick it runs from or OWNEETLOG;
  in the installer **a screen of its own** after the system disk, each other internal disk "Leave as it is" (selected first) or
  "Erase and prepare for games"; **started from the USB stick, only the installer** prepares disks (the internal disks stay read only, [[step-6.5-automatic-disk-mounting]]).
