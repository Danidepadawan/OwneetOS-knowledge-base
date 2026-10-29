---
type: step
description: "QML installer in the OwneetOS style, gamepad-only, clear warnings and a final confirmation before erasing anything."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.4"
status: in-progress
legacy: "ROADMAP.md 6.4"
tags: [step, phase-6]
---
# 6.4 Installer UI

Up: [[phase-6-first-boot-installer-disks]] · Status: **in-progress**

- **Deliverables:** QML installer in the OwneetOS style, gamepad-only, clear warnings and a final confirmation before erasing anything.
- **Demo (2026-10-26):** `design/demos/6.4-installer.html`, on the backend of
  [[step-6.3-installer-backend]]: welcome (a whole disk, offline, nothing saved yet); the
  internal disks with model, size and what is on them (Windows and BitLocker marked, too small
  ones off with the reason); the console's name ("OwneetOS", changed with the console's
  keyboard); the warning, with a specific box and a switch to turn on before "Continue" for a disk
  with Windows or BitLocker; the final confirmation, **A held for three seconds** (a ring fills;
  letting go cancels); the progress in the backend's steps; the end (remove the stick, restart)
  and the errors in the player's words. The owner likes it (2026-10-26). Where the installer is
  started from: [[step-6.2-live-vs-installed-mode]]. Branch `feature/step6_installer`.
