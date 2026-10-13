---
type: step
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.3"
status: needs-decision
legacy: "ROADMAP.md 6.3"
tags: [step, phase-6]
---
# 6.3 Installer backend *(multi-prompt)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **needs-decision**

- **Deliverables:** whole-disk install: partitioning, btrfs subvolumes, snapper, bootloader, user,
  first-boot setup. Tested on virtual disks only, never on the host.
- **Open point:** **systemd-boot cannot boot btrfs snapshots by itself.** Rollback from the boot
  menu needs either GRUB + grub-btrfs or Limine + snapshot sync, or a different rollback design.
  Decision to be taken with the owner at the start of this step.
