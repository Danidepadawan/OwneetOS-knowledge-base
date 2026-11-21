---
type: step
description: "Mounting (OwneetOS's own mounter) for internal and removable disks (ext4, btrfs, NTFS, exFAT), read-only NTFS when Windows left it…"
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.5"
status: done
legacy: "ROADMAP.md 6.5"
tags: [step, phase-6]
---
# 6.5 Automatic disk mounting

Up: [[phase-6-first-boot-installer-disks]] · Status: **done**

- **Deliverables:** mounting for internal and removable disks (ext4, btrfs,
  NTFS, exFAT), read-only NTFS when Windows left it hibernated, with an explanation to the user.
  Free space and notices of every disk reach the library's disks summary and Disks window
  (approved in demo 3.7); later actions there, e.g. "Safely remove" for USB disks.
- **GOG's DOS games' saves with the game (owner, 2026-10-16, [[games-on-disk]]):** once disks are
  mounted read-write, the overlay where a GOG DOS game writes (DOSBox Staging, step 4.5) is GOG's own
  `cloud_saves` next to the game on its disk, so settings and saves travel with it, also on PCs
  with several disks. The overlay folder on the console's disk stays only for disks left read only
  (e.g. a Windows disk left dirty), and the game's details say so. At the switch, what an existing
  overlay folder holds moves to `cloud_saves`: nothing is lost.
- **Started (owner, 2026-11-01)** on `feature/phase6`, after 6.2 and 6.4. **Decided:** OwneetOS's
  own mounter of step 4.3 grows instead of udisks2 (plan changed: the deliverable said "udisks2
  policy"); Windows's own partition always read only; from the USB stick the internal disks read
  only, and the installer unmounts the chosen disk before erasing it ([[disks]]).
- **Built (2026-11-01, code 699d0e9, 7ed8684):** `owneet-base` 0.0.53: `owneet-mount` (was
  `owneet-mount-ro`), `owneet-mount@.service`, `90-owneet-disks.rules` (internal disks too); the
  reason of a read-only mount in `/run/owneet-mount/<name>` (`windows`, `windows-system`, `live`,
  `error`). `owneet-installer` 0.0.3: the disk being installed on is left alone
  (`/run/owneet-mount/installing`) and unmounted first. `owneetd` 0.21.0: `owneet-dos-run` writes a
  GOG DOS game's saves to GOG's own `cloud_saves` next to it on a writable disk (the console's folder
  copied there once, kept aside as `cloud_saves.old`), on the console's disk otherwise.
  `owneet-frontend` 0.28.0: `Storage` tells the reason and NTFS; the Disks window shows demo 3.7's
  notes (the Windows one only for that reason, the generic one otherwise, the NTFS one).
- **Tested in the test VM (2026-11-01)** with a test disk made in the builder VM (ntfs-3g and
  ntfsprogs installed there, owner's consent): ext4, clean NTFS, NTFS with `Windows/System32`, NTFS
  with a hibernated `hiberfil.sys`. As a USB disk, from the stick and installed: ext4 and clean
  NTFS read-write, Windows's partition read only (`windows-system`), the hibernated one read only
  (`windows`); copied to an internal disk: from the stick all read only (`live`), installed as on
  USB; the console user writes on ext4 and not on the hibernated one; the console's own disk never
  mounted again. An installation on an internal disk that was mounted (from the stick) unmounted it
  and left its new partitions alone. Found and fixed: Windows's partition labelled "WINDOWS" was
  taken for the Windows folder. The DOS saves checked by hand with a stand-in DOSBox.
- **Demo for approval (2026-11-01):** `design/demos/6.5-saves-read-only.html` (on demo 4.5): the
  details of a GOG DOS game on a read-only disk say "Saves: On the console: this disk is read only".
- **Demo approved by the owner (2026-11-01)**; the row written (`owneet-frontend` 0.29.0, theme's
  `detailsFacts`: a game with `disk.dos` on a read-only disk), seen in the preview
  (`tools/preview-steps/saves-read-only.txt`). **Step 6.5 done (owner, 2026-11-01).** Later, as
  the step says: "Safely remove" for USB disks in the Disks window.

