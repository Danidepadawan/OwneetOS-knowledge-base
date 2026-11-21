---
type: known-solution
description: "Steam started from the console shows its logo, flickers, passes by its home or stays there, instead of the page asked for: its interface was not ready. How to know when it is, on any computer."
status: solved
seen: 2026-11-05
updated: 2026-11-05
tags: [known-solution, steam, gamescope]
---
# Steam loses the address while its interface starts

## Symptom

"Open Steam's storage" with Steam closed, on FrankenPC (gamescope): Steam's home instead of Storage, or Storage after passing by the
home; Steam's Big Picture logo on screen for some seconds, then a flicker for a couple of seconds. With Steam already running the same
address works at once ([[step-6.6-moving-games-and-media-between-disks]]).

## Cause

Steam's window exists well before its interface. An address that comes in between is dropped. A fixed wait does not fit: it depends
on the computer.

From FrankenPC's logs (`out/test-logs/frankenpc-2026-11-05/`, `console_log.txt` for `ExecCommandLine`, `webhelper.txt` for the line below):

| Address reached Steam | `notificationtoasts_uid…: STARTUP LoadEnd` | Result |
|---|---|---|
| 12:10:58 | 12:11:01 (3 s later) | Lost: Steam's home |
| 13:28:15 | 13:28:13 (2 s earlier) | Storage opened |

The address takes about 4 s to go through the `steam` command on FrankenPC, while the check loop waits for it.

## Solution

**`owneetd` 0.24.4:** the window stays hidden until that line appears in `logs/webhelper.txt` after the point where the log
ended when Steam started; the page goes then, the window shows 3 checks later; `app.window` closes "Preparing Steam…" at that moment.
At most 30 checks without the line, then Steam shows anyway. Only with an account and started from the console.
**Owner's test on FrankenPC (2026-11-05):** line 15:33:47, address 15:33:49, window 15:33:53, 31 s from the press; Steam's start no longer shows; a flicker does, kept by the owner; Steam's home shows for about a second before Storage, accepted by the owner.

## How we found it

The address tested by hand in the VM with Steam ready proved it right (a first conclusion that it was wrong had been a mistake). Then:
every Steam start in FrankenPC's `webhelper.txt`, with the time of that line: it comes in all 33 starts since it first appears (2026-10-14), 9 to
12 s after the interface starts, and in none of the 21 before (most likely before the account signed in: not proved).

## Watch out

- The line is Steam's own log, not a promise: a new Steam may change it. Then every start waits the full 30 s: check it first if Steam seems slow to open.
- Not seen yet when Steam **starts** without internet (in the test of 2026-11-05 Steam was already running when the Wi-Fi went): at worst the 30 s.
- An expired sign-in has no line either: the sign-in shows after the 30 s.
- In the test VM: `vm/test.sh run` too early goes to the boot menu and edits the kernel's options (`Failed to mount '' on real root`): wait for the system.
