---
type: step
description: "`iso/` profile derived from Arch `baseline`, minimal package list, pinned Arch Linux Archive snapshot date, OwneetOS branding in…"
phase: "[[phase-1-minimal-bootable-os]]"
step: "1.1"
status: done
legacy: "ROADMAP.md 1.1"
tags: [step, phase-1]
---
# 1.1 archiso profile

Up: [[phase-1-minimal-bootable-os]] · Status: **done**

- **Deliverables:** `iso/` profile derived from Arch `baseline`, minimal package list, pinned
  Arch Linux Archive snapshot date, OwneetOS branding in `os-release`.
- **Done when:** the ISO builds in the builder VM and boots to a TTY in the test VM.
- **Outcome:** `iso/` profile (UEFI only, systemd-boot; packages `base`, `linux`, `mkinitcpio`,
  `mkinitcpio-archiso`; Arch Linux Archive snapshot 2026-10-03) and `tools/build-iso`. Build takes
  about 2 minutes; ISO is 471 MiB. In the test VM the systemd-boot menu shows "OwneetOS" and the
  system reaches `OwneetOS 7.2.8-arch1-2 (ttyS0)` / `owneet login:`. Added `vm/test.sh wait-serial`
  and `vm/test.sh log` for automated boot checks.
