---
type: known-solution
description: "A black screen of about 6 s between the boot splash and the interface, then the animation already in colour: what it is made of, and what was tried without success."
status: open
seen: 2026-11-05
updated: 2026-11-05
tags: [known-solution, boot, session, plymouth]
---
# Black screen between the boot splash and the session

## Symptom

On every start the white and grey logo of the boot splash goes black for some seconds before the
interface shows it again. On FrankenPC the start-up animation then seemed to begin directly in colour,
so the passage was not seamless ([[step-7.6-final-logo-and-brand]]).

## Cause

Measured in the test VM (cage session, no sound, 2026-11-05):

- **At `plymouth quit` the screen goes black:** the kernel's console takes the screen over ("fbcon: Taking
  over console"), also with `plymouth quit --retain-splash`.
- **About 5 s:** `getty@tty1` is `Type=idle`: systemd holds it back up to 5 s while other start-up jobs run.
  `owneet-boot-check.service` runs for about a minute, so the wait is always the full 5 s (trace of agetty:
  "Started Getty" at 02.26, its `execve` at 07.28).
- **About 1 s:** the login, `owneet-session` and the interface's first frame.
- **On a real screen,** the screen may also take a moment to show the session's first frames, and the
  fade (`OutCubic`) is nearly over after 1 s: this is why it seemed to start in colour.

## Solution

**Fixed:** the colours (`owneet-frontend` 0.36.1, code commit on `feature/phase7`): the animation and its
sound wait 1.5 s on the splash's still picture. In the VM: black, the logo in white and grey, then the colours.
To be confirmed on FrankenPC.

**Open:** the black itself. Tried in the VM, all reverted:

| Tried | Result |
|---|---|
| `plymouth quit --retain-splash` in a drop-in | Black at the same moment: fbcon takes over |
| `Type=simple` for `getty@tty1` | Login **30 s** later instead of 5 s |
| The same, without `pam_systemd_home` in `system-auth` | Still 30 s: not the cause, though the journal shows `org.freedesktop.home1` failing just before the session |
| `Type=simple` for the boot check, `getty@tty1` left `idle` | Login more than 28 s later |

What holds the login back when it starts during the boot check was **not found**. An idea not tried: keep Plymouth
running until the compositor starts (the way display managers do), quitting it from the session.

## How we found it

Screenshots in a loop during a real reboot (`vm/test.sh screenshot`, about 18 per second), classified as black,
logo or other; `journalctl -o short-precise` between "Finished Terminate Plymouth" and "starting cage"; `strace -f -tt`
in front of `agetty` through a drop-in, to see when it really starts.

## Watch out

- Measure every change with a real reboot: `Type=simple` looks like an obvious fix and makes it six times worse.
- A `home1` line just before a slow login is not the cause.
- A build's "completed" is not its result: check its exit status (2026-11-05, a first build failed on a network
  error while the notification said completed).
