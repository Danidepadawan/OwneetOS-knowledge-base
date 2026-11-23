---
type: known-solution
description: "A Steam game stays at \"Starting…\" for minutes (Steam's install script never ends) while owneetd keeps Proton's Xalia paused for an install-script window already gone."
status: solved
seen: 2026-11-23
updated: 2026-11-23
tags: [known-solution, steam, proton, xalia, pointer]
---
# Steam's install script stuck while Xalia is paused

## Symptom

A Steam game started again (often right after it was quit) stays on Steam's "Starting…" page with
nothing else on screen; Steam's `console_log.txt` stops at `LaunchApp changed task to
ProcessingInstallScript` / `Running install script evaluator for AppID N`, with no
`SynchronizingStats` after it. owneetd's journal has, a second before: `a window of the game's
install script: the pointer on for its windows` and `Proton's Xalia paused while the console's
pointer is on`, and no `the game's install script has ended` until Steam is closed. Seen with
South Park: The Fractured But Whole (`steam:488790`) on the FrankenPC, 2026-11-23: 16 minutes at
09:20, then at 10:18 and 10:50 ([[open-items]] 21).

## Cause

owneetd turns the pointer on for any window of a game's install script (an installer made for a
mouse, [[controller-input-map]]) and, while the pointer is on, pauses Proton's Xalia (SIGSTOP), so
that both do not click the same window. The pointer for the install script went off only when all
the script's programs had ended. Here the script's window showed for a few seconds and went
(the window log 10 s later lists only Steam's and the console's windows), but the pointer, and so
the pause, stayed; and the script did not end while Xalia was paused. Proof from the journal:
at 09:36:58 the pointer went off for another reason, Xalia went on (SIGCONT), and the script ended
at 09:37:09; when the script ended before Xalia was paused, the launch went through (10:17, 10:45).
Why the script waits for Xalia is not known (Proton's `proton` script and `steam_helper/steam.c` do
not start or stop Xalia; read 2026-11-23): hypothesis.

## Solution

owneetd 0.26.4: the pointer turned on for an install script also goes off as soon as no window of
the script is on screen (Xalia's own windows not counted), even while its programs run; Xalia then
goes on. A new window of the script turns it on again. Windows on screen come from gamescope's X
server (mapped top-level windows, `_NET_WM_PID` and X-Resource), as owneetd tags them. Confirmed on
the FrankenPC on 2026-11-23 (owneetd 0.26.5): two launches in a row, the pointer off within 1 s each time.

## How we found it

1. `owneet-*.steam/console_log.txt`: grep `GameAction [AppID 488790` and `Running install script
   evaluator`: the stuck launches never got past `ProcessingInstallScript`, the good ones did in 1-11 s.
2. `owneet-*.windows.txt` at the stuck moments: no window of the script mapped; the screenshots
   show only "Starting…".
3. owneetd's lines in the journal (`.previous/boot-minus-*.txt.gz` too): every stuck launch had
   Xalia paused just after the script's window; the 16-minute one ended 11 s after Xalia went on.

## Watch out

Anything that pauses a program of a game (SIGSTOP) can hold Steam's launch: pause only while the
reason is on screen. If a launch sticks again at "Starting…", check first for `Xalia paused` without
a later `goes on`.
