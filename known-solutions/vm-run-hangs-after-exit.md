---
type: known-solution
description: "`vm/test.sh run` waits until its time is up and the VM never runs the command (the server sees no request): an `exit` in an earlier part of the command closed the VM's debug shell."
status: solved
seen: 2026-10-20
updated: 2026-10-20
tags: [known-solution, vm, testing]
---
# `vm/test.sh run` hangs: `exit` closed the VM's shell

## Symptom

- `vm/test.sh run '…' 180` prints nothing and waits until its time is up ("hanging forever").
- What the command should have done never happened: e.g. the package server on the developer's
  PC shows **no `GET` request**, although the VM's network, the server and pacman are fine (checked
  with separate, smaller `vm/test.sh run` commands, which work).

## Cause

`vm/test.sh run` types the command into the VM's root debug shell on the serial console and waits
for a marker that the shell prints when the command is done. A command with `exit` in it, e.g. a
check written as `test ! -e FILE || { echo "…"; exit 1; }`, **closes that shell** when the check
fails: the marker never comes. The shell is started again afterwards, so the next commands work.
In [[step-5.4-netflix]] the check failed because the probe's leftover
`/usr/share/owneet/extension.off` was still there.

## Solution

Never use `exit` in a command for `vm/test.sh run`: write checks as
`if [ -e FILE ]; then echo "…"; else …; fi`.

## How we found it

1. The package server on the PC showed no request: the command stopped before its download.
2. Network (`ip -br addr; ip route; curl … http://10.0.2.2:8000/`) and pacman (`pgrep -a pacman`,
   the lock file) were fine: the first part of the command, the check with `exit`, was left.
3. `ls -d /usr/share/owneet/extension*` showed the leftover folder that made the check fail.

## Watch out

- The same goes for anything that ends the shell (`exit`, `logout`, `exec` of another program).
- A probe round that swaps `/usr/share/owneet/extension` must always end with its "put things
  back" step; check with `ls -d /usr/share/owneet/extension*` before installing packages.
