---
type: step
description: "UEFI test VM script with blank virtual disks (single disk, multi-disk, 'Windows-like' NTFS disk for later), controller passthrough (USB…"
phase: "[[phase-0-foundations]]"
step: "0.8"
status: done
legacy: "ROADMAP.md 0.8"
tags: [step, phase-0]
---
# 0.8 Test VM harness

Up: [[phase-0-foundations]] · Status: **done**

- **Goal:** boot any built ISO the same way every time.
- **Deliverables:** UEFI test VM script with blank virtual disks (single disk, multi-disk,
  "Windows-like" NTFS disk for later), controller passthrough (USB passthrough or evdev), serial
  log capture, snapshot/reset.
- **Done when:** the stock Arch ISO boots in the harness and a host gamepad reaches the guest.
- **Progress:** `vm/test.sh` + shared `vm/lib/common.sh`. Stock Arch ISO 2026.10.01 (verified by
  checksum and release signature) boots in UEFI mode in ~45 s with 4 GB RAM, 4 CPUs, 32G + 64G disks;
  `reset` returns to blank disks; `--gl` gives a virgl GPU (OpenGL only with QEMU 8.2, no Vulkan).
  Gamepad passthrough verified with the owner's Xbox One controller over Bluetooth: the guest sees
  it with the same name and USB IDs (`js0`), and received A/B/X/Y, LB/RB, both triggers, both sticks
  (full range) and the D-pad.
  NTFS test disk moved to step 6.5, where it is first needed.
