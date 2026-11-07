---
type: step
description: "Erasing and preparing a disk other than the console's for games, with the controller: in the installer and in Settings → Disks, with a clear warning and the final confirmation."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.7"
status: in-progress
tags: [step, phase-6]
---
# 6.7 Preparing other disks *(added 2026-11-07)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **in-progress**

- **Why (owner, 2026-11-07, "gravissimo"):** the console could erase only the disk it is installed on. A new disk, one in a format the
  console cannot read, or one to turn into a better format for games needed another PC: the owner took it for granted, and no step had it.
- **Deliverables (owner, 2026-11-07):** both **in the installer** (the other internal disks) and **in Settings → Disks**, with the controller
  only; a clear warning and the final confirmation for every disk ([[user-data]], [[installer-and-firmware]]); the disk comes out ready for
  games (its Games folder, the console allowed to write on it).
- **When:** now, before everything else left (owner, 2026-11-07). **Demo first** ([[demo-before-code]]); the details are asked to the owner.
- **Choices (owner, 2026-11-07):** **ext4 only** (the best for games, Windows ones and Steam included; Windows and Mac no longer read
  the disk); from Settings → Disks **internal and USB disks**, never the console's own disk, the stick it runs from or OWNEETLOG;
  in the installer **a screen of its own** after the system disk, each other internal disk "Leave as it is" (selected first) or
  "Erase and prepare for games"; **started from the USB stick, only the installer** prepares disks (the internal disks stay read only, [[step-6.5-automatic-disk-mounting]]).
- **Demos (2026-11-07), waiting for the owner's approval:** `design/demos/6.7-installer-other-disks.html` (on the approved 6.4: the screen
  "Other disks" after the disk for OwneetOS, every other internal disk of any size, "Leave as it is" first; the warning and the final
  confirmation name every disk) and `design/demos/6.7-settings-disks.html` (on the approved 6.2: every disk but the console's own can be
  chosen, a disk the console cannot read listed as "Not ready for games", "Prepare {disk} for games?" with Cancel selected, Windows's warning
  to switch on, A held three seconds, the wait and the notice; from the USB stick only a note).
- **Owner (2026-11-08):** both demos **approved**; the final confirmation must be held to the end (letting go stops it: the settings demo
  went on after a mouse click, a slip of the demo, fixed). **The player names each disk** prepared for games, and two disks never share a
  name: "Games" ("Games 2"…) offered in the console's language, up to 16 characters (ext4's label: accented letters count as two). In the
  settings demo a step before the final confirmation; in the installer the screen "Name the disks for games" after "Other disks", and the
  warning says each name. **The naming screens wait for the owner's look** before the code.

