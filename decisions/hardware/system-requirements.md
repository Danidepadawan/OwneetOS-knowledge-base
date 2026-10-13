---
type: decision
area: hardware
status: active
decided: 2026-10-03
updated: 2026-10-11
legacy: "PROJECT_RULES.md §3"
tags: [decision, hardware]
---
# System requirements (target hardware)

- CPU: x86_64, roughly the last ~10 years.
- Firmware: **UEFI required** (PCs from about 2012 onwards). Legacy BIOS boot is not supported.
  - PCs from about 2012–2019 often offer both modes: if set to "Legacy" / "CSM", the user switches
    to UEFI in the firmware settings. The user guide explains this in the same step as disabling
    Secure Boot, and the system requirements state it clearly.
  - Dual boot (later wave): a Windows installed in Legacy mode cannot be started from the
    OwneetOS boot menu; the installer must detect it and explain it.
- RAM: **4 GB minimum**, 8 GB recommended.
- Disk: **32 GB** minimum.
- GPU: **Vulkan** required for the main (gamescope) session. GPUs without adequate Vulkan support
  (e.g. Intel iGPUs older than ~2015) automatically fall back to a reduced **cage** session
  (no overlay). See [[console-session]].
- **Steam in the live session** (no installed disk) needs at least **12 GB of RAM**; the installed
  system's requirements do not change ([[steam-integration]]).
- The ISO boots UEFI only and contains no SSH server, cloud-init or VM guest tools.

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-04 | ISO boots UEFI only (no legacy BIOS); no SSH server, cloud-init or VM guest tools in the ISO (step 1.1). |
| 2026-10-04 | UEFI firmware is a system requirement (PCs from ~2012); Legacy/CSM switch explained in the user guide ([[system-requirements]]). |
| 2026-10-11 | Steam in the **live session** (no installed disk: Steam's first download of about 2.4 GB is kept in RAM): only with at least **12 GB of RAM**; otherwise a clear message asks to install OwneetOS to use Steam. The **installed system's requirements do not change** (4 GB minimum, 8 GB recommended); Steam is started only when needed (C1 is measured with Steam closed). |
