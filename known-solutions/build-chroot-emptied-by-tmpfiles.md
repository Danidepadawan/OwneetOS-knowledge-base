---
type: known-solution
description: "A package build in the builder VM fails at once, a config file not found in the chroot: the system's cleaning of /var/tmp emptied the build chroot."
status: solved
seen: 2026-11-20
updated: 2026-11-20
tags: [known-solution, builder-vm]
---
# The build chroot emptied by the cleaning of /var/tmp

## Symptom

A package build through `tools/build-in-vm` fails at once, before compiling anything:

```text
==> Synchronizing chroot copy [/var/tmp/owneet-chroot/root] -> [builder]...done
==> ERROR: /var/tmp/owneet-chroot/builder/etc/makepkg.conf not found.
==> ERROR: Could not download sources.
```

In the builder VM the chroot's `/etc` (`/var/tmp/owneet-chroot/root/etc`) holds only folders: no
`pacman.conf`, `makepkg.conf` or `passwd`. `/var/log/pacman.log` is gone too, and `/usr/bin` has
far fewer programs than it should. The same build worked the day before.

## Cause

The package build script keeps its clean chroot in `/var/tmp/owneet-chroot`. systemd cleans
`/var/tmp` (`systemd-tmpfiles-clean.timer`, 15 minutes after boot and then daily; the rule
`q /var/tmp 1777 root root 30d` of `tmp.conf`): it deletes files nobody has read, written or
changed for 30 days, and keeps the folders. Builds work in a copy of the chroot (a btrfs
snapshot), so the chroot's own files are never read. The chroot was made on 2026-10-13: by
2026-11-20 most of its files had been deleted. The previews' containers in `/var/tmp`
(`owneet-preview`, `owneet-player`) can lose files the same way.

## Solution

In the builder VM, move the emptied chroot aside and build again. The package build makes a new
chroot by itself:

```text
tools/build-in-vm 'sudo mv /var/tmp/owneet-chroot /var/tmp/owneet-chroot.broken'
tools/build-in-vm tools/build-packages owneetd
```

Then delete the old chroot. Its folders are btrfs subvolumes, the nested ones first:
`sudo btrfs subvolume delete …/root/var/lib/machines …/root/var/lib/portables`, then `…/root` and
`…/builder`, then `rm -rf` the folder.

**A lasting fix, proposed to the owner (2026-11-20):** exclude the project's folders from the
cleaning in the builder VM, with a tmpfiles rule set up with the VM (`x /var/tmp/owneet-*` in
`/etc/tmpfiles.d/owneet.conf`), or keep them outside `/var/tmp`.

## How we found it

Step 5.6a, building owneetd 0.19.1 (2026-11-20). Listing the chroot's `/etc` showed only folders,
dated 2026-10-13, the day the chroot was made. The files that disappeared were those the builds
never touch, which pointed to the age-based cleaning of `/var/tmp`.

## Watch out

Every 30 days or so, until the lasting fix is in. A chroot or container in `/var/tmp` that fails in
odd ways (a missing file under `/etc`, a program not found) has probably been cleaned. Look at the
dates of the files that are left before looking for a fault in the build.
