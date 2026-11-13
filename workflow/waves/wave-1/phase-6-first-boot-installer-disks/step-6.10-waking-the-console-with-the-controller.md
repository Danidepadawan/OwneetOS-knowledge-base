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
- **Feasibility (2026-11-13):** Linux can do it: the USB Bluetooth adapter (and the USB devices above it) allowed to
  wake the PC (`power/wakeup`), and the paired controllers allowed to wake it through BlueZ (`WakeAllowed`); an Xbox
  controller turns on again with Guide only. It depends on the adapter staying powered in sleep. **The owner agreed
  to a test first:** owneet-base 0.0.72's test log does both with the switch `owneet.debug.bt_wake=on` in
  `owneet-debug.txt` (on OWNEETLOG) and writes `<log>.wake.txt`; the owner puts the console to sleep and presses
  Guide. If it works: the demo of the setting (off by default) and of the message when the adapter cannot.
