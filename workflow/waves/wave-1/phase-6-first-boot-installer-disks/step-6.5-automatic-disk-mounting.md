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
- **GOG's DOS games' saves with the game (owner, 2026-10-16, [[games-on-disk]]):** once disks are
  mounted read-write, the overlay where a GOG DOS game writes (DOSBox Staging, step 4.5) is GOG's own
  `cloud_saves` next to the game on its disk, so settings and saves travel with it, also on PCs
  with several disks. The overlay folder on the console's disk stays only for disks left read only
  (e.g. a Windows disk left dirty), and the game's details say so. At the switch, what an existing
  overlay folder holds moves to `cloud_saves`: nothing is lost.
