---
type: step
description: "Waking the console from sleep with the controller (a feature many players want): what the hardware allows, the Bluetooth adapter and the Xbox wireless adapter, and how the console asks for it."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.10"
status: needs-decision
tags: [step, phase-6]
---
# 6.10 Waking the console with the controller *(added 2026-11-09)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **needs decision**

- **Why (owner, 2026-11-09):** many players want to wake the console with the controller; in Wave 1.
- **What is known:** the console has Sleep (Power options: Sleep, Restart, Shut down). Waking needs the device the controller talks
  to (a Bluetooth adapter, the Xbox wireless adapter, a USB cable) to stay powered in sleep and to be allowed to wake the PC
  (USB remote wake-up); not every adapter can (FrankenPC uses a generic USB Bluetooth dongle). Waking from a full power-off is
  not possible with a controller on most PCs.
- **Choices (owner, 2026-11-09):** **only Guide** wakes the console; the feature is **switched on and off in the settings, off by
  default**. First a test on FrankenPC: whether its generic Bluetooth dongle can wake it from sleep.
- **Still open:** what the console says when the adapter cannot wake the PC; the setting's place and text (demo first).
