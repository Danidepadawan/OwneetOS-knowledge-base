---
type: step
description: "Erasing and preparing a disk other than the console's for games, with the controller: in the installer and in Settings → Disks, with a clear warning and the final confirmation."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.7"
status: done
tags: [step, phase-6]
---
# 6.7 Preparing other disks *(added 2026-11-07)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **done**

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
- **Built (2026-11-08, code commit d4f148d on `feature/phase7`):** `owneet-prepare-disk` in owneet-installer 0.0.4 (the disks, the
  checks, the work: GPT, one ext4 file system with no space kept for root, the name as its label, the console user owning it, the Games
  folder; `owneet-prepare-disk.service` started from Settings through polkit); `owneet-install` takes up to 8 other internal disks,
  checked before anything is touched and prepared last (state `games`, error `games_failed`); owneet-mount (owneet-base 0.0.56)
  leaves them alone meanwhile; owneetd 0.25.0 ([[owneetd-api-disks]]); owneet-frontend 0.37.0 (Settings → Storage, the installer's
  two screens, the hold shared as `HoldButton`, texts in the five languages). Go tests for every refusal (names, disks, confirmations).
  **Checked in the test VM:** Settings on an empty disk and on one with a Windows partition (a short press starts nothing; the name
  another disk keeps is refused; ext4, the label, the Games folder, mounted read-write, the notice); the installer from a new ISO
  (`out/owneetos-2026.11.08-x86_64.iso`) with a second disk for games, then the installed system writing on it.
  Found on the way: the Settings list did not follow disks changing while it was open; it now does, and the question reads the disk again.
  **Left:** the owner's test on real hardware.
- **Owner's test on FrankenPC (2026-11-08), first try:** no disk could be chosen: owneetd found no `owneet-prepare-disk` ("no such
  file or directory"). It was in owneet-installer, which a console installed by the tester installer before step 6.3 never got (updates
  from the stick only update packages already there). Moved into owneet-base 0.0.57 with its unit, its polkit rule
  (`50-owneet-disks.rules`) and its folder; owneet-installer 0.0.5 depends on owneet-base (code commit da951de). Checked in the test VM
  with and without owneet-installer. The version in Settings → System stays 2026.10.13 on FrankenPC: it is the image's date, which the
  stick's updates do not change. **Waits for the owner's second try.**
- **Owner's second try on FrankenPC (2026-11-08):** the 2 TB disk prepared from Settings ("2TB HDD SATA"); owner: "Tutto risolto". **Done.**
- **Owner's test on FrankenPC (2026-11-08, later):** the prepared 2 TB disk could not be chosen in Steam to install Batman: Arkham
  Knight: Steam's storage had no "Add drive" at all, no list and no message. Steam's interface for the controller cannot add a disk; on
  SteamOS the system tells Steam ([[steam-cannot-add-a-disk-from-its-controller-interface]]). **Fix (owner: a fix, not a new
  feature; use Steam's address; only the disks the console prepared):** owneetd 0.25.3 hands every disk prepared for games (ext4, its
  top folder owned by the console's user, the Games folder), mounted read-write, to the running Steam as
  `steam://addlibraryfolder/<disk>/SteamLibrary` (the folder made first; the disk itself when Steam already keeps a library at its top),
  once Steam's window is up or Steam has run a minute; once per disk while Steam runs, never a folder Steam lists already. Go tests.
  **Test VM (cage session, no Steam account):** after a minute the disk was handed and `SteamLibrary` made; Steam with nobody signed in
  showed nothing of it. **Waits for the owner's test on FrankenPC** (Steam signed in).
- **Owner's test on FrankenPC (2026-11-09):** owneetd handed the disk (00:09:13, after Steam's window and the page asked for) and
  Steam logged `ExecuteSteamURL: "steam://addlibraryfolder/…"`, then nothing: no library added (`libraryfolders.vdf` still one
  library), the disk not in Storage nor among the places to install. **Not solved.** Also reported: one press of A confirmed two of
  Steam's dialogs in a row (installing Batman: Arkham Knight); Steam's logs do not say which. Next: the owner decides the way.
- **Second fix (owner, 2026-11-09: the first way, Steam's own list):** owneetd 0.25.4
  writes each disk prepared for games into Steam's `libraryfolders.vdf` (both copies, `steamapps/` and `config/`) while Steam is
  closed, right before the console starts it: `<disk>/SteamLibrary` with its `libraryfolder.vdf` and `steamapps`, labelled with the
  disk's name; never twice, never a folder Steam lists already; nothing when Steam has never run. The addlibraryfolder address is
  gone. Go tests. **Test VM, the owner signed in (2026-11-09):** Steam loaded "2 libraries"; Storage shows "GamesVM Games, 31.3 GB
  free of 31.3 GB" (before the label: the folder `/run/media/owneet/GamesVM Games`); Batman: Arkham Knight's install offers it (not
  enough room in the VM), cancelled. Steam's own library shows as "/home" (Steam's label, not ours): asked to the owner.
  **Waits for the owner's test on FrankenPC.** On the way: with `--gl` the VM's window stayed black on the host; without it, it shows.
- **Owner's test on FrankenPC (2026-11-09):** "2TB HDD SATA" in Steam's Storage and among the places to install; Batman: Arkham
  Knight downloads there. **Solved, step done again** (owner).
