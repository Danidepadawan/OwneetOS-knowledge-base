---
type: known-solution
description: "A package build in the builder VM never ends and the builder stops answering SSH: the developer's PC went to sleep during the build."
status: solved
seen: 2026-11-09
updated: 2026-11-09
tags: [known-solution, builder-vm]
---
# The builder VM stops answering after the PC sleeps

## Symptom

`tools/build-in-vm tools/build-packages …` never ends: its log stops at a ninja step (e.g.
`[428/452] …`) and does not move for many minutes. `vm/builder.sh ssh '…'` hangs or prints nothing;
inside the VM, when it answers, no `makepkg`, `ninja` or `systemd-nspawn` runs and the guest's
uptime is a few minutes. The QEMU process on the PC is still there.

## Cause

The developer's PC went to sleep (suspend) during the build. After it wakes, the VM's build is gone
and the SSH session that `tools/build-in-vm` keeps open waits on a dead connection.

## Solution

Stop the waiting `tools/build-in-vm`, stop the builder VM, and build again (the next build starts
the VM by itself):

```text
vm/builder.sh stop
tools/build-in-vm tools/build-packages owneet-frontend
```

Keep the PC awake for the whole build (the frontend takes about 15 minutes: compile, tests, the
theme's check).

## How we found it

Step 5.6, sub-step 4 (2026-11-09): the log had stopped for ten minutes; `ps` in the VM showed no
build; the PC's journal (`journalctl -b | grep -i resum`) showed "Resume from sleep detected" during
the build. It happened twice that day.

## Watch out

A long build or preview with the PC left alone. Check the PC's journal for a resume before looking
for a fault in the build.
