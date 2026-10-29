---
type: decision
description: "Own QML installer, dual boot considered but not required, BitLocker, Secure Boot always disabled."
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
- **Which disks (owner, 2026-10-25):** internal disks of at least 32 GB only, never the USB stick
  the installer starts from, never other USB disks; external disks in [[wave-2]] (item 18).
- **A disk with Windows or BitLocker on it** can be used for "Use the whole disk" only after a
  specific warning (what was found and that all of it, encrypted files included, will be lost)
  and the final confirmation (owner, 2026-10-25); nothing is ever erased or changed automatically
  ([[user-data]]).
- **Formatting always needs the player's confirmation** (owner, 2026-10-25), for every disk: the
  installer's backend refuses to touch a disk unless the request carries the confirmation for that
  very disk, besides the Windows or BitLocker confirmation.
- **The console's name** (on the network and over Bluetooth) is **editable**, so several consoles
  can be told apart (owner, 2026-10-25); default "OwneetOS"; chosen in the installer, changed
  later in Settings, not asked at the first start (owner, 2026-10-26). If it becomes a problem, changing it
  moves to [[wave-2]] (item 19).
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
| 2026-10-25 | Installer (6.3): internal disks only (external ones in Wave 2); a disk with Windows or BitLocker erased only after a specific warning and the final confirmation; the console's name editable (default "OwneetOS"; Wave 2 if it becomes a problem). |
