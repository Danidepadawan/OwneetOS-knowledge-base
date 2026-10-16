---
type: step
description: "Udisks2 policy + daemon logic for internal and removable disks (ext4, btrfs, NTFS, exFAT), read-only NTFS when Windows left it…"
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.5"
status: todo
legacy: "ROADMAP.md 6.5"
tags: [step, phase-6]
---
# 6.5 Automatic disk mounting

Up: [[phase-6-first-boot-installer-disks]] · Status: **todo**

- **Deliverables:** udisks2 policy + daemon logic for internal and removable disks (ext4, btrfs,
  NTFS, exFAT), read-only NTFS when Windows left it hibernated, with an explanation to the user.
  Free space and notices of every disk reach the library's disks summary and Disks window
  (approved in demo 3.7); later actions there, e.g. "Safely remove" for USB disks.
- **GOG's DOS games in place (owner, 2026-10-16, [[games-on-disk]]):** once disks are mounted
  read-write, a GOG DOS game runs from its own folder on its own disk (no copy): its settings and
  saves stay with it (GOG's folder or `cloud_saves`), also on PCs with several disks. The copy on
  the console's disk (step 4.5) stays only for disks left read only (e.g. a Windows disk left
  dirty), and the game's details say so. At the switch, saves made in an existing copy go back to
  the game's folder, then the copy is removed: nothing is lost.
