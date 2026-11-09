---
type: known-solution
description: "Every Windows game (and owneet-windows-run) ends at once with exit 0, no error, and the prefix is never made (drive_c holds only users): umu's ~/.local/share/umu/umu-shim is a 0-byte file after a hard stop."
status: solved
seen: 2026-11-09
updated: 2026-11-09
tags: [known-solution, proton, umu, windows-games, vm]
---
# Windows games quit at once: empty umu-shim

## Symptom

A Windows game started by the console (`owneet-windows-run`, umu-launcher) ends after a few
seconds with exit status 0 and no error. umu's own log shows only "Running 'GE-Proton…' using
runtime 'steamrt4'"; there is no Proton log even with `PROTON_LOG=1`. A new prefix holds only
`drive_c/users` (no `windows` folder). With `UMU_LOG=debug PRESSURE_VESSEL_VERBOSE=1` the container
starts, runs `~/.local/share/umu/umu-shim` and reports "Command exited with status 0".

## Cause

`~/.local/share/umu/umu-shim` is **0 bytes**. umu writes it (a small `sh` script that ends in
`exec "$@"`, 402 bytes, mode 700) the first time it sets itself up; the test VM was stopped by
hand right after (2026-11-08 13:35), and btrfs had saved the file's entry but not its contents
(the same as [[empty-files-after-an-update-and-a-hard-stop]]). An empty executable file runs as
an empty shell script: nothing happens, status 0. umu rewrites the shim only when it is
**missing** (`umu_run.py`: "Restore shim if missing", `is_file()`), never when it is empty, so it
stays broken for good.

## Solution

By hand: `rm ~/.local/share/umu/umu-shim`; umu writes it again at the next start (test VM,
2026-11-09). On every console since owneetd 0.25.10 (code `77f35a7`, owner's go-ahead
2026-11-09): `owneet-windows-run` removes a shim that does not hold `exec "$@"` (empty, or cut
short) before it starts umu, and says so in the game's log ("umu-shim was broken (N bytes):
removed, umu writes it again"). Tested in the test VM with an empty shim, one cut to 150 bytes
and an intact one: the first two were written again (402 bytes) and the prefix was made; the
intact one was left alone.

## How we found it

1. A prefix made through `owneet-windows-run` held only `drive_c/users`; the run ended at once.
2. `UMU_LOG=debug PRESSURE_VESSEL_VERBOSE=1 PROTON_LOG=1`: the container was fine and ran the
   command it was given, which was `umu-shim … proton waitforexitandrun …`; no Proton log at all,
   so Proton never ran.
3. `file ~/.local/share/umu/umu-shim`: "empty"; `ls --time-style=full-iso` dated it to a few
   seconds after umu's first setup in the VM; `umu_run.py` showed the "missing" check.

## Watch out

After any hard stop of a machine (the test VM above all) while umu or Proton set themselves up:
if Windows games end at once, look at `umu-shim`'s size first. If umu ever changes its shim so
that it no longer holds `exec "$@"`, the console removes it at every start and umu writes it
again: harmless, but the log line appears at every launch, so update the check.
