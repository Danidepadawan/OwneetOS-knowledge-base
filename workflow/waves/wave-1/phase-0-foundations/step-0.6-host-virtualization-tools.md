---
type: step
phase: "[[phase-0-foundations]]"
step: "0.6"
status: done
legacy: "ROADMAP.md 0.6"
tags: [step, phase-0]
---
# 0.6 Host virtualization tools — **Owner input**

Up: [[phase-0-foundations]] · Status: **done**

- **Goal:** run VMs on the host without touching anything else.
- **Deliverables:** install `qemu-system-x86`, `ovmf`, `qemu-utils` (asked at the moment);
  `vm/` scripts that keep every disk image, firmware variable store and log inside the project folder.
- **Done when:** a throwaway UEFI VM boots and is removed cleanly.
- **Outcome:** packages installed by the owner (QEMU 8.2.2, OVMF 2024.02); `vm/vm.sh` created;
  `vm/vm.sh selftest` boots UEFI firmware under KVM in about 1 s and removes every file.
  `qemu-system-gui` added afterwards (VM windows, 3D acceleration for step 0.8); owner tested a VM in a window.
