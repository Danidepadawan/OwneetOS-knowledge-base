---
type: known-solution
description: "The Witcher 2's Linux tenfoot-launcher shows a black screen and closes (basic_string::_S_construct null not valid): its language files have escapes today's GLib refuses. The console fixes them."
status: solved
seen: 2026-11-11
updated: 2026-11-12
tags: [known-solution, linux-games]
---
# The Witcher 2's TV launcher aborts at once

## Symptom

The Witcher 2 (GOG, Linux) started with `game/tenfoot-launcher` (its launcher for the TV and the controller): a black
screen for a couple of seconds, then it closes with no message. In the journal: `terminate called after throwing an
instance of 'std::logic_error' what(): basic_string::_S_construct null not valid`, right after "reading
.../Witcher 2/config/User.ini failed".

## Cause

The launcher reads its language files `game/bin/config/lang/*.ini` as GLib key files and builds a C++ string from every
value. They hold `IK_Backslash=\ (Backslash)` (group `[InputEditor]`): `\ ` is an escape that today's GLib (2.88) refuses,
`g_key_file_get_string` returns NULL, and a string made from NULL aborts. The `User.ini` message is harmless (the file is
made later). With the backslashes escaped the launcher runs and starts the game with A, then crashes itself (a recursion
out of stack). GOG's other launcher, `desktop-launcher`, needs 32-bit GTK 2, which the console does not have.

## Solution

Owner, 2026-11-11 ([[games-on-disk]]): first the console started the game's own program, `game/witcher2`, with its
folder in `LD_LIBRARY_PATH` (owneet-frontend 0.38.16); the game ran on the FrankenPC, but its language could not be
changed (only the launchers write it, in `User.ini`, `[linux] Language=`, `Speech=`). Then the launcher again
(owneet-frontend 0.38.17): the list of known games (`frontend/known-games/known-games.json`, by the GOG id in
`gameinfo`) names `game/tenfoot-launcher` and `fix-key-files: game/bin/config/lang/*.ini`; when the interface reads
the game on the console's disk it writes each lone backslash twice (`\ (Backslash)` → `\\ (Backslash)`, `「\」` →
`「\\」`), only that line in the 14 files changing. In the test VM the launcher then stays open (no abort). Not
seen yet on the console: whether it crashes after starting the game (it did once in the VM), and its language
choice.
Then (owner, 2026-11-12): the launcher stayed **black** even with its language files fixed: its loop updates only when a
turn lasts more than 10 ms, and under SDL3 `SDL_WaitEventTimeout(NULL, 1)` waits 1 ms (SDL2 polled every 10 ms); after
Start Game its clean-up **crashed** (a recursive `std::map` destruction, stack overflow; not caused by address
randomisation: 2 crashes in 3 runs with it and without), and it **ignored `SDL_QUIT`** (killed after the 10 s stop
limit). Fixed by OwneetOS's `compat/old-sdl2-launcher` library (`lib32-owneet-compat`, `LD_PRELOAD` only for this file,
named by `known-games.json`'s `launchers`): the old 10 ms wait, `_exit` once the game is started and on `SDL_QUIT`;
and owneetd keeps the app while the game the launcher started runs (`handover`, `ExitType=cgroup`).

## How we found it

1. Test VM, the owner's copy of the game: `gdb --args ./tenfoot-launcher`, `catch throw`, `bt`: the throw comes from
   building a string from `g_key_file_get_string`'s result.
2. A breakpoint on `g_key_file_get_string` printing group and key: the last one is `[InputEditor] IK_Backslash`, NULL.
3. The line in the `.ini` files: `IK_Backslash=\ (Backslash)`; escaped as `\\ (Backslash)` in a copy, the launcher runs.

## Watch out

- Other old Linux games that read GLib key files written for an older GLib can fail the same way: look for a NULL from
  `g_key_file_get_*` and backslashes in their `.ini` files.
- A game with a launcher that does not work: add it to `known-games.json` (`frontend/known-games/README.md`).
- A screen that stays black but shows at once after a pause (gdb attached, SIGSTOP/SIGCONT): a loop that measures
  its turns and resets its clock when they are short; look at how it waits for events.
- A launcher that starts the game and ends: with `Type=exec` and `KillMode=control-group`, the game is stopped with it.
- Only the copy the launcher reads counts: `GameDocuments/Witcher 2/config/lang` in the home folder holds copies,
  fixing them alone changed nothing.
