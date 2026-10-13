---
type: step
phase: "[[phase-1-minimal-bootable-os]]"
step: "1.5"
status: done
legacy: "ROADMAP.md 1.5"
tags: [step, phase-1]
---
# 1.5 Hardware support set

Up: [[phase-1-minimal-bootable-os]] · Status: **done**

- **Deliverables:** firmware, Mesa + Vulkan drivers, `nvidia-open` with automatic detection,
  `xone` (built into `[owneet]`), PipeWire, NetworkManager, BlueZ, udev rules for controllers.
- **Done when:** ISO size is measured and stays **under 2 GB**; idle RAM is measured and recorded.
  First real-hardware boot of the live ISO on the owner's NiPoGi E3B mini PC (AMD/Intel path), and
  later on the owner's desktop (RTX 4060, NVIDIA path), confirming gamescope (step 1.3).
- **Real hardware, 2026-10-06:** the live ISO boots on the owner's NiPoGi E3B mini PC (AMD Ryzen
  7430U, 12 threads, integrated Radeon graphics, 24 GB RAM): boot splash shown, then the placeholder with **"console session: gamescope"**, so the
  Vulkan check and gamescope work on real hardware. Still to test: the NVIDIA path (owner's desktop).
  Note: gamescope does not allow switching to other virtual terminals (Ctrl+Alt+F9), so the debug
  shell is reachable only in the cage session: diagnostics use
  `systemd.debug_shell owneet.session=cage`. To do: a "diagnostics" boot menu entry with these
  arguments, so testers do not have to type them. **Done:** boot entry "OwneetOS (diagnostics)"
  with an automatic report on tty9 (`owneet-diagnostics`), verified in the VM.
  Owner's desktop (RTX 4060 + Intel UHD 770): normal boot shows "console session: gamescope";
  diagnostics report: `blacklist nouveau` (Turing+ detected), `nvidia` + `nvidia_drm` loaded (plus
  `i915`/`xe` for the Intel iGPU), Vulkan lists the RTX 4060 as discrete GPU. Memory: 2824 MiB used,
  of which 1540 MiB were the live image copied to RAM by archiso (`copytoram` defaults to on with
  plenty of RAM): this also explained the slow boot from USB. Fixed with `copytoram=n`. The RAM target
  (500 MB) is measured on the installed system with the real UI. Observed: the live boot from USB is slow (USB stick speed,
  LZMA-compressed root, first NVIDIA initialisation; an installed system will not have the first two),
  and the boot menu editor uses the US keyboard layout (firmware limitation).
- **Progress:** `owneet-hardware` meta-package (firmware, microcode, Mesa + Vulkan for AMD/Intel,
  `nvidia-open` + `nvidia-utils`, PipeWire, NetworkManager, BlueZ, controller rules) and
  `owneet-gpu-select` (nvidia-open for Turing+, nouveau for older NVIDIA). Measured in the VM:
  ISO **1664 MiB** (under 2 GB, but NVIDIA's user space alone is ~950 MiB installed: the budget left
  for Brave and the UI is tight; options if needed: trim NVIDIA files, or a separate NVIDIA ISO),
  boot to session ~13 s, system RAM without the placeholder UI ~235 MiB, no failed units,
  NetworkManager and Bluetooth enabled. New test tool: `vm/test.sh --debug-shell` + `run`.
  **xone is not included:** the dongle firmware is Microsoft's and cannot be redistributed; it needs
  a separate decision (download on the user's PC at first use).
