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
- **First try (2026-11-13 15:23): not woken, but nothing had been set** (the test log tried before BlueZ answered and
  again only after its first report, the console already asleep). owneet-base 0.0.73 runs the test on its own as
  soon as BlueZ has its adapter (at most a minute); the FrankenPC's adapter is a Realtek RTL8761BU (USB). To try
  again, a minute after the start.
- **Second try (2026-11-13 15:49): nothing set again** (the test came after the start's other work, minutes on the
  FrankenPC). owneet-base 0.0.74 runs it right after the journal starts (checked with a real restart in the test VM).
- **Third try (2026-11-13 16:13): everything set** (wakeup on the adapter, its hub and XHC; `WakeAllowed` on the Xbox
  controller); slept at 16:15:05, **woken at 16:15:16** (the owner's Guide, most likely), the controller back at
  16:15:31; then "the PC restarted by itself": the stick's log stops at 16:15:34 with no shutdown. The console's own
  journal of that start is needed (one more start with the stick).
