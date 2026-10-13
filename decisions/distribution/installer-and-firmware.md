---
type: decision
area: distribution
status: active
decided: 2026-10-03
updated: 2026-10-04
legacy: "PROJECT_RULES.md §6 (installer, dual boot, Secure Boot)"
tags: [decision, distribution, installer]
---
# Installer, dual boot and Secure Boot

- **Own installer** in QML (same look as the OS), fully gamepad-driven. Calamares rejected
  (mouse-oriented). Tested on virtual disks only.
- Choices kept simple: "Use the whole disk" (default) / "Install alongside Windows" (later wave).
- **Dual boot must be considered, but it is NOT required.** OwneetOS must work fully as the only OS
  on the machine. Design choices (partitioning, bootloader, installer flow) must not prevent adding
  dual boot later, but no Wave 1 feature may depend on it. When implemented:
  - BitLocker partitions cannot be resized from Linux: detect them and guide the user to free
    space from Windows. Never touch them automatically.
  - Handle RTC (UTC vs local time) automatically.
  - Settings: default OS selection and a **"Restart into Windows"** button.
- **Secure Boot is always disabled** — explained in the user guide. The guide and the installer
  must **warn** that some Windows games with anti-cheat (e.g. Battlefield 6, Valorant) require
  Secure Boot.
- Firmware must be UEFI ([[system-requirements]]).

Guards: [[user-data]], [[host-safety]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-03 | Secure Boot always disabled; anti-cheat warning in guide. |
| 2026-10-04 | Dual boot: considered in the design, **not required** ([[disks]]). |
