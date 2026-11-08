---
type: known-solution
description: "A feature works in the test VM but not on a tester PC updated from the OWNEETLOG stick: a file is missing (\"no such file or directory\") because it lives in a package the PC never had."
status: solved
seen: 2026-11-08
updated: 2026-11-08
tags: [known-solution, testing, packages, updates]
---
# A tester PC misses a new package

## Symptom

On FrankenPC, after the stick's update, Settings → Storage let no disk be chosen; the journal said
`fork/exec /usr/lib/owneet/owneet-prepare-disk: no such file or directory`. In the test VM, installed from
a new ISO, everything worked. Settings → System showed 2026.10.13: that is the image's date
(`IMAGE_VERSION`), which the stick's updates never change, not a sign that the update failed.

## Cause

`owneet-update` installs only the OwneetOS packages **newer than the installed ones** (`pacman -S --needed`
of those names). A package added to the image after a tester PC was installed (here owneet-installer,
step 6.3, while FrankenPC dates from 2026-10-13) never reaches it, and neither does a file moved into it.

## Solution

What every console needs goes into a package every console has (owneet-base, owneetd,
owneet-frontend); a new package is a dependency of one of them. Here `owneet-prepare-disk` moved into
owneet-base 0.0.57 ([[step-6.7-preparing-other-disks]]).

## How we found it

The stick's journal (`owneet-*.journal.txt`): owneetd's warning, then `owneet-update: installing ...`, which
listed only owneet-base, owneet-frontend and owneetd.

## Watch out

Before giving the testers a feature, check which package each new file is in, and whether the tester PCs
have it (`out/update-extras/pkglist-2026.10.13.txt` is FrankenPC's list).
