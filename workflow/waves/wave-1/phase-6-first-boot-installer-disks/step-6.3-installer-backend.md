---
type: step
description: "Whole-disk install: partitioning, btrfs subvolumes, snapper, bootloader, user, first-boot setup. Tested on virtual disks only, never on…"
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.3"
status: in-progress
legacy: "ROADMAP.md 6.3"
tags: [step, phase-6]
---
# 6.3 Installer backend *(multi-prompt)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **in-progress**

- **Deliverables:** whole-disk install: partitioning, btrfs subvolumes, snapper, bootloader, user,
  first-boot setup. Tested on virtual disks only, never on the host.
- **Decision (owner, 2026-10-25): option C.** systemd-boot cannot boot btrfs snapshots by itself;
  instead of GRUB + grub-btrfs or Limine (keyboard-only menus, a bootloader more), systemd-boot
  stays and rollback is done from the console with the controller, and automatically after 3
  failed boots (boot counting), the boot menu only a keyboard fallback
  ([[distribution-and-updates]]). The user's data live in subvolumes never rolled back.
- **Starts from** the tester installer `owneet-tester-install` of [[step-4.2a-tester-installer]]
  (GPT, 1 GiB EFI system partition, btrfs subvolumes, systemd-boot).
- **Branch:** `feature/step6_installer` in the code and in this vault (owner, 2026-10-25).
