---
type: decision
description: "xone in the image, Microsoft firmware downloaded with consent, xpad and mt76x2u kept."
area: hardware
status: active
decided: 2026-10-06
updated: 2026-10-06
legacy: "PROJECT_RULES.md §7 (xone)"
tags: [decision, hardware, controllers]
---
# Xbox wireless dongle (xone)

- Drivers shipped in the image: kernel HID drivers, **xone** (Xbox wireless dongle).
- The dongle's **firmware is Microsoft's and cannot be redistributed**: OwneetOS downloads it on
  the user's PC, with the user's consent, the first time a dongle is plugged in (internet needed).
- First-boot warning: the first setup needs a **Bluetooth or USB-cable controller**; a wireless
  Xbox controller can be used over its USB cable until the dongle is ready ([[first-boot-setup]]).
- xone is packaged **without `xone_wired`** and **without blacklisting `xpad` / `mt76x2u`**: wired
  controllers stay on the kernel's `xpad` and USB Wi-Fi adapters keep working
  (`softdep mt76x2u pre: xone_dongle`).
- The xone module is rebuilt for every kernel change; CI builds use the ISO's Arch snapshot for
  build dependencies too (kernel headers must match).

Plan and status: [[step-1.7-xbox-wireless-dongle-xone]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-05 | xone (Xbox wireless dongle) moved out of step 1.5: its firmware is Microsoft's and cannot be redistributed. |
| 2026-10-06 | xone: driver in the image, Microsoft firmware downloaded on the user's PC at first dongle use with consent; first setup needs a Bluetooth or cable controller ([[controllers-and-pairing]]). |
| 2026-10-06 | xone packaged without `xone_wired` and without blacklisting `xpad`/`mt76x2u` (wired controllers and USB Wi-Fi adapters keep working); CI builds use the ISO's Arch snapshot for build dependencies too (step 1.7). |
