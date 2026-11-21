---
type: known-solution
description: "Package builds stop with 'does not appear to be an Arch chroot' and a missing makepkg.conf: systemd emptied the build chroot, then under /var/tmp, after 30 days."
status: solved
seen: 2026-11-04
updated: 2026-11-04
tags: [known-solution, build, builder-vm]
---
# Build chroot emptied by systemd-tmpfiles

## Symptom

In the builder VM every package build stops at once:

```text
==> ERROR: '/var/tmp/owneet-chroot/builder' does not appear to be an Arch chroot.
==> ERROR: /var/tmp/owneet-chroot/builder/etc/makepkg.conf not found.
==> ERROR: Could not download sources.
```

The chroot's folders are there and the disk has room, but few files are left in them (30 in
`usr/bin`). It had worked the day before.

## Cause

The chroot lived under `/var/tmp`, and `/usr/lib/tmpfiles.d/tmp.conf` says
`q /var/tmp 1777 root root 30d`: `systemd-tmpfiles-clean` deletes what has not been used for 30
days. The chroot was made on 2026-10-04, and the cleaning of 2026-11-03 emptied the files no build
had read.

## Solution

The chroot moved to `/var/lib/owneet-chroot` (`tools/build-packages`, `tools/frontend-preview`; code
commit 84746a3 on `feature/phase7`, step 7.6). The old one was removed in the VM and the build made
the new one.

## How we found it

The chroot's date was 30 days old that very day; counting the files in its `usr/bin` gave 30;
`/usr/lib/tmpfiles.d/tmp.conf` gave the 30 days; `journalctl -u systemd-tmpfiles-clean` showed the
cleaning the evening before, opening files of the chroot.

## Watch out

Nothing that must last goes under `/var/tmp` or `/tmp` in the builder VM. A build that fails on a
file that should always be there: look at the age of the folder first.
