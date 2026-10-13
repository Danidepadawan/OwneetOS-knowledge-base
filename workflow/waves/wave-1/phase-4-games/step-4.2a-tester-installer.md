---
type: step
description: "A boot entry 'Install OwneetOS (testers: erases a disk)' (text screen, keyboard) that installs the stick's own system image onto a whole…"
phase: "[[phase-4-games]]"
step: "4.2a"
status: in-progress
legacy: "ROADMAP.md 4.2a"
tags: [step, phase-4]
---
# 4.2a Tester installer *(owner, 2026-10-13: test PCs are installed, not run from a stick)*

Up: [[phase-4-games]] · Status: **in-progress**

- **Deliverables:** a boot entry "Install OwneetOS (testers: erases a disk)" (text screen, keyboard)
  that installs the stick's own system image onto a whole internal disk chosen by the tester:
  GPT with a 1 GiB EFI system partition and btrfs with subvolumes ready for snapshots, fstab,
  initramfs without the live hooks, systemd-boot, pacman pinned to the same snapshot, the tester
  mark. Never the USB stick or other USB disks; ERASE typed to confirm. `docs/tester-install.md`.
  Leaves the user ISO with the other test entries (7.4). The user installer stays 6.3 / 6.4.
- **Outcome (2026-10-13):** `owneet-tester-install` (owneet-base 0.0.23). Checked in the test VM
  with two disks: the chosen disk installed, the other untouched, the installed system starts
  into the console without the stick (btrfs subvolumes mounted, no failed unit, every file
  matching its package). Found and fixed on the way: (1) a `Conflicts=` on the console login
  stopped the console on every boot (now a condition on getty@tty1 itself); (2) **the ISO's
  erofs + LZMA image had silently corrupted six files** (five rarely used kernel modules and the
  AMD firmware `gc_11_0_3_mes1.bin`, Radeon 780M family; `mkfs.erofs` wrote them wrong, the
  original packages were fine): the image is now squashfs + xz (ISO 1822 MiB instead of 2164) and
  `tools/build-iso` checks every file of the image against its package. `vm/test.sh boot --disk`
  starts the VM from its disks.
- **FrankenPC (owner, 2026-10-13):** installed, but it started only with "Linux Boot Manager"
  chosen from the F12 menu: its firmware settings offer only "Fallback Linux Boot Manager", which
  systemd 262's `bootctl install` registers while writing its file
  (`\EFI\systemd\systemd-boot-fallbackx64.efi`) only on later updates. The installer now writes
  it (owneet-base 0.0.27), and the update to 0.0.27 writes it on systems already installed;
  checked in the test VM (update from the stick at start-up, then a start through the Fallback
  entry).
