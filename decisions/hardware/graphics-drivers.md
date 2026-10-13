---
type: decision
area: hardware
status: active
decided: 2026-10-05
updated: 2026-10-10
legacy: "PROJECT_RULES.md §13 (2026-10-05, 2026-10-08)"
tags: [decision, hardware, gpu]
---
# Graphics drivers

- **NVIDIA:** Turing and newer use `nvidia-open`; older NVIDIA GPUs use nouveau, chosen at boot by
  `owneet-gpu-select` (no `kms` initramfs hook, which would load nouveau first). Package
  `owneet-hardware`.
- **With the NVIDIA driver, gamescope always composites**: direct scanout showed flickering black
  rectangles on the owner's RTX 4060. AMD and Intel keep direct scanout.
- **Intel:** gamescope runs with `INTEL_DEBUG=noccs` (compositor and interface only): Intel's
  compressed (CCS) buffers need widths that are multiples of 128 pixels on some GPUs, and a
  1440 × 900 screen stayed black (hardware test 3 of [[step-3.9-settings]]).
- **NVIDIA DDC/CI** needs the driver's software I2C (`owneet-nvidia-i2c.conf`, ddcutil's
  recommended setting).

Details and measurements: [[step-1.5-hardware-support-set]], [[step-2.9-process-manager-and-guide-button]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-05 | Hardware support (`owneet-hardware`): NVIDIA Turing and newer use `nvidia-open`; older NVIDIA GPUs use nouveau, chosen at boot by `owneet-gpu-select` (no `kms` initramfs hook). ISO 1664 MiB (step 1.5). |
| 2026-10-08 | With the NVIDIA driver, gamescope always composites (direct scanout showed flickering black rectangles on the owner's RTX 4060). |
