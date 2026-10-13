---
type: decision
description: "Host safety, everything in the project folder, builder and test VMs, asking before host installs."
area: process
status: active
decided: 2026-10-03
updated: 2026-10-03
legacy: "PROJECT_RULES.md §11"
tags: [decision, process, environment]
---
# Development environment

- Never damage the developer's PC or installed OS (host: Linux Mint).
- Keep everything inside the project folder (sources, VM disks, caches, build artefacts).
- ISOs are built inside an **Arch "builder" VM** (QEMU/KVM), never on the host; they are booted in
  the **test VM** (`vm/`).
- Host packages needed: `qemu-system-x86`, `ovmf`, `qemu-utils` (and `qemu-system-gui`) — **ask
  the owner at the moment of installation**, every time something must be installed on the host.
- VirtualBox and KVM cannot run VMs at the same time on recent kernels.

Guard: [[host-safety]]. Practices: [[testing-and-verification]], [[checks-before-commit]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
