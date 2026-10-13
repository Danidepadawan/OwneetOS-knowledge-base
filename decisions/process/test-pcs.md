---
type: decision
description: "Test PCs are installed with a tester installer and updated from the OWNEETLOG USB stick; only they accept unsigned OwneetOS packages."
area: process
status: active
decided: 2026-10-13
updated: 2026-10-13
legacy: "PROJECT_RULES.md §13 (2026-10-13)"
tags: [decision, process, testing]
---
# Test PCs are installed

- Test PCs are **installed**, not run from a USB stick: a tester installer
  ([[step-4.2a-tester-installer]], boot entry "Install OwneetOS (testers)") and updates from a USB
  stick ([[step-4.2b-updates-from-a-usb-stick]]: the `owneet-updates` folder on the OWNEETLOG
  stick, applied automatically at boot and from Settings → System), before step 4.3.
- **Nothing is published online.** Only systems installed by the tester installer accept unsigned
  OwneetOS packages, and only from that stick (option b; [[package-signing]]).
- Test PCs: **"FrankenPC"** (i7-6700, 16 GB, 96 GB SSD + 2 TB HDD, GTX 1660 Super), installed; the
  **NiPoGi** stays a live-stick test PC.
- The tester installer leaves the user ISO with the other test entries before the release
  ([[step-workflow]], step 7.4). The user installer stays steps 6.3 and 6.4.

Guide for testers: `docs/tester-install.md` (code repository).

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-13 | **Test PCs are installed**, not run from a stick: a tester installer (step 4.2a, boot entry "Install OwneetOS (testers)") and updates from a USB stick (step 4.2b: the `owneet-updates` folder on the OWNEETLOG stick, applied automatically at boot and from Settings → System), before step 4.3. Nothing is published online. Only systems installed by the tester installer accept unsigned OwneetOS packages, and only from that stick (option b). Test PC: "FrankenPC" (i7-6700, 16 GB, 96 GB SSD + 2 TB HDD, GTX 1660 Super); the NiPoGi stays a live-stick test PC. |
