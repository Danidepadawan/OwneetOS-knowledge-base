---
type: step
description: "Moved to Wave 2 (owner, 2026-11-03): the Xbox wireless dongle (xone driver, Microsoft firmware with consent), parked until a real dongle can be tested."
phase: "[[phase-1-minimal-bootable-os]]"
step: "1.7"
status: todo
legacy: "ROADMAP.md 1.7"
tags: [step, phase-1]
---
# 1.7 Xbox wireless dongle (xone): moved to Wave 2

Up: [[phase-1-minimal-bootable-os]] · Status: **todo** (Wave 2)

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
- **Moved to Wave 2 (owner, 2026-11-03):** a real dongle may not be bought (the legal review's
  costs come first), so nothing untested goes into the first release. Code commit 6cd37c4:
  `owneet-xone` waits in `packages/wave-2/` (outside the package build: in no ISO, no release),
  owneet-hardware 0.0.6 no longer depends on it, xone left `CREDITS.md`. owneetd's dongle code
  and the first start's "Xbox wireless adapter found" window (6.1) stay in the code, idle: without
  the driver no dongle is reported. The user guide does not name the dongle. **When it comes
  back:** the package back in `packages/`, owneet-hardware depends on it again, xone back in
  `CREDITS.md`, the test with a real dongle ([[wave-2]]).
