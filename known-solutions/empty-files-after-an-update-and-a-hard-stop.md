---
type: known-solution
description: "A package installed with pacman, then the machine stopped by hand: the package's files are 0 bytes (\"Exec format error\", the interface does not start). How to see it and repair it."
status: solved
seen: 2026-10-17
updated: 2026-10-17
tags: [known-solution, packages, pacman, vm]
---
# Empty files after an update and a hard stop

## Symptom

- After an update, the console shows "OwneetOS could not start its interface. It will try again
  in one minute." (`owneet-session`, after three failed starts).
- The journal (`journalctl -b -t owneet-cage`) says
  `exec: /usr/bin/owneet-frontend: cannot execute: Exec format error`.
- The program is **0 bytes**, and so is every other file of the package; pacman's own record of
  it is broken (`pacman -Qkk` → `error while reading file /var/lib/pacman/local/<pkg>/mtree:
  Unrecognized archive format`).
- Reinstalling it fails with "exists in filesystem": with its record unreadable, pacman no longer
  knows that the files are the package's.

## Cause

Seen 2026-10-17 in the test VM: owneet-frontend 0.16.11 installed with `pacman -U` at 01:32,
the VM **stopped by hand** from the host before 02:00. pacman does not force its files to the
disk, and btrfs writes them out about every 30 seconds: the files' entries reached the disk, their
contents were still only in memory. The package itself was intact (its program started with
`\x7fELF`).

## Solution

Reinstall, overwriting only the package's own paths, then write everything to the disk:

```sh
pacman -U --noconfirm --overwrite /usr/bin/owneet-frontend \
  --overwrite "/usr/share/licenses/owneet-frontend/*" --overwrite "/usr/share/owneet-frontend/*" PKG
sync
```

The paths come from the package (`bsdtar -tf PKG`). Afterwards `pacman -Qkk owneet-frontend`
reports 0 altered files.

## How we found it

1. The journal line above: the kernel refuses the file as a program.
2. `ls -la` → 0 bytes; `head -c 64 FILE | od -c` → nothing (a program starts with `177 E L F`).
3. `pacman -Qkk PKG` → every file of the package wrong, the record unreadable; other packages
   fine. `find /usr /etc -xdev -type f -size 0 -newermt "<date>"` lists the empty files (some
   system files are empty on purpose: `/usr/lib/clock-epoch`, `/usr/share/mime/icons`).
4. On the host, `bsdtar -xOf PKG usr/bin/owneet-frontend | head -c 4 | od -c` → `177 E L F`: the
   package was fine, the VM's copy was not. The journal of the failing boot started after the
   install, and the VM had been stopped by hand in between.

## Watch out

- In a VM: run `sync` after installing by hand, and stop the VM from inside
  (`systemctl poweroff`) rather than from the host.
- **The same can happen to a real console** that loses power right after an update. To consider
  in [[step-7.1-updates]] (snapshots before updates): `sync` after `owneet-update` installs, and a
  check of the installed packages (`pacman -Qkk`) at the next start.
