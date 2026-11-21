---
type: known-solution
description: "The test VM never starts the ISO (or the installed disk): the firmware goes straight to PXE / HTTP boot and stops in the UEFI shell. Stale firmware boot entries; vm/test.sh reset or vm/vm.sh reset-firmware."
status: solved
seen: 2026-11-01
updated: 2026-11-01
tags: [known-solution, vm, testing]
---
# The test VM ignores the ISO and stops in the UEFI shell

## Symptom

`vm/test.sh boot ISO` (or `boot --disk`) starts, but the serial log only shows `>>Start PXE over
IPv4.`, `PXE-E16: No valid offer received`, the HTTP boot errors, then `UEFI Interactive Shell`
and `Shell>`. The ISO is listed in the shell's mapping table (`CD0…`, `CDROM(0x0)`) but is never
tried. `vm/test.sh run` then answers in the UEFI shell (`'…' is not recognized as an internal or
external command`) or says the debug shell does not answer.

## Cause

The VM's firmware variables (`vm/images/test/OVMF_VARS.fd`) keep the boot entries and boot order
of earlier tests (installers write "Linux Boot Manager" entries; disks were reset afterwards).
With those stale entries the firmware skipped the CD and tried only the network. Most likely
cause, not traced further: restoring the variables fixed it at once.

## Solution

`vm/test.sh stop; vm/test.sh reset` (disks **and** firmware variables back to the `blank` state),
then boot again. To keep the disks and only clear the firmware's entries:
`vm/vm.sh reset-firmware test` (already in `vm/README.md`, "Changing virtual hardware").

## How we found it

Step [[step-7.0-update-stick-image-for-the-test-vm]], 2026-11-01: `boot --disk` ended in the UEFI
shell (the disk was blank: expected), then `boot out/owneetos-2026.11.01-x86_64.iso` did the same.
A screenshot showed TianoCore with "Start PXE over IPv4"; the serial log had no line for the CD.
After `vm/test.sh reset` the same ISO started at once (`OwneetOS 7.2.8-arch1-2 (ttyS0)`).

## Watch out

After tests that install a system (tester installer, [[step-6.4-installer-ui]]) and a disk reset
done by hand, reset the whole VM with `vm/test.sh reset` before booting an ISO.
