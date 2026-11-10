---
type: known-solution
description: "The console's free space does not grow after a game is moved away (or files are removed), and changes only much later: btrfs frees the room at its next commit, and the library read the disks only when shown again."
status: solved
seen: 2026-11-10
updated: 2026-11-10
tags: [known-solution, disks, btrfs]
---
# Free space shown late after removing files

## Symptom

After moving a game from the console's disk to another disk (its original removed), the library
still shows the console's disk with the free space it had before (owner, FrankenPC, 2026-11-10: 38 GB
before and after moving The Witcher 2's Linux version away); much later it shows the right value
(50 GB). An install that needs that room may still be refused meanwhile.

## Cause

Two things together:

- **btrfs** (the console's disk, `owneet-install`) counts the room of removed files as free only
  at its next transaction commit, every 30 s by default: `statfs` (`df`, `QStorageInfo`) shows the
  old value until then. Measured in the test VM: 3 GB removed, the free space the same for 20 s,
  right after 25 s.
- **The library** (`LibraryPage.qml`) read the disks only when it was shown again; at the end of a
  move the interface read the games again (`readGamesQuietly`) but not the disks.

## Solution

- owneetd 0.25.20 (`daemon/internal/moves`): after removing an original, `syncDisk` (syncfs on its
  disk) makes btrfs commit, before the move is told done.
- owneet-frontend 0.38.15 (`theme.qml` `readGamesQuietly`): the library reads the disks again with
  the games (after a move, an install, an uninstall).

Checked in the test VM: a 3 GB game moved from `/home` (btrfs) to another disk, the free space
right as soon as owneetd told the move done (52 067 → 54 928 MB).

## How we found it

- The owner's logs (`out/test-logs/frankenpc-20261110-203820`): the move of 20:39 ended at about
  20:43:55 ("Installs changed: reading the games again"), the install of 20:44:35 was accepted: the
  room was there for owneetd's check, not on screen.
- `LibraryPage.qml`: `refreshVolumes()` only in `onVisibleChanged` and at the start.
- In the test VM: `rm` of a 3 GB file on `/home` and `df` every 5 s: unchanged for 20 s.

## Watch out

Anything that removes files on the console's disk and then shows or checks its free space at once
(uninstall, deleting an installer, clearing caches) meets the same btrfs delay: sync the disk
(syncfs) first, then read the space.
