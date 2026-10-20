---
type: decision
description: "Host safety, everything in the project folder, builder and test VMs, asking before host installs."
area: process
status: active
decided: 2026-10-03
updated: 2026-10-20
legacy: "PROJECT_RULES.md §11"
tags: [decision, process, environment]
---
# Development environment

- Never damage the developer's PC or installed OS (host: Linux Mint).
- Keep everything inside the project folder (sources, VM disks, caches, build artefacts). The
  project is the code repository `OwneetOS/` **and** this knowledge base next to it,
  `OwneetOS-knowledge-base/` (owner, 2026-10-14): writing in both is inside the project.
- ISOs are built inside an **Arch "builder" VM** (QEMU/KVM), never on the host; they are booted in
  the **test VM** (`vm/`).
- Host packages needed: `qemu-system-x86`, `ovmf`, `qemu-utils` (and `qemu-system-gui`) — **ask
  the owner at the moment of installation**, every time something must be installed on the host.
  On an Arch-based host (e.g. CachyOS), QEMU's devices are separate packages: `qemu-base`,
  `edk2-ovmf`, `qemu-hw-display-virtio-gpu`, `qemu-hw-display-virtio-vga` (without them the test
  VM stops with "Virtio VGA not available"), and for windows and 3D `qemu-ui-gtk`,
  `qemu-hw-display-virtio-gpu-gl`, `qemu-hw-display-virtio-vga-gl`. Full table: `vm/README.md`.
- VirtualBox and KVM cannot run VMs at the same time on recent kernels.
- **The website** ([[website]], owner, 2026-10-20): built on the host with the owner's Node
  (installed with nvm in the home folder); its dependencies stay in `OwneetOS-website/` (no global
  installs), and each installation is asked first, like any host install.

Guard: [[host-safety]]. Practices: [[testing-and-verification]], [[checks-before-commit]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-13 | Host packages for Arch-based hosts listed (the test VM needs the `virtio-vga` packages). |
| 2026-10-20 | The website is built on the host with the owner's Node (nvm), dependencies in its folder only, each installation asked first (option a). |
