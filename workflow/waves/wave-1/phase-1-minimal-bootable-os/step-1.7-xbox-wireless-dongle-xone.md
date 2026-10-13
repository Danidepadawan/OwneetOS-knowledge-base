---
type: step
description: "Xone kernel module built for the ISO's kernel (rebuilt with every kernel change), firmware download helper (Microsoft's firmware,…"
phase: "[[phase-1-minimal-bootable-os]]"
step: "1.7"
status: in-progress
legacy: "ROADMAP.md 1.7"
tags: [step, phase-1]
---
# 1.7 Xbox wireless dongle (xone) (software done; real dongle test open)

Up: [[phase-1-minimal-bootable-os]] · Status: **in-progress**

- **Deliverables:** xone kernel module built for the ISO's kernel (rebuilt with every kernel
  change), firmware download helper (Microsoft's firmware, fetched on the user's PC with consent at
  first dongle use), first-boot notice that setup needs a Bluetooth or cable controller.
- **Done when:** a dongle-connected Xbox controller works after the firmware download, on real
  hardware.
- **Progress:** `owneet-xone` (xone 0.5.8, compiles cleanly against kernel 7.2.8; 8 modules, without
  `xone_wired`; `softdep mt76x2u pre: xone_dongle` instead of upstream's blacklist of `xpad` and
  `mt76x2u`), `owneet-xone-firmware` (status / install with explicit consent / udev flag
  `/run/owneet/xone-firmware-needed`). Verified in the test VM: driver loads, `xpad` untouched,
  install refused without consent, with consent the 4 firmware files are downloaded from
  Microsoft, checksum-verified and installed. CI build now pins its container to the ISO's Arch
  snapshot (kernel headers must match the ISO kernel). **Open:** test with a real dongle (the owner
  has none for now). The consent dialog and the first-boot notice are UI work: step 6.1.
