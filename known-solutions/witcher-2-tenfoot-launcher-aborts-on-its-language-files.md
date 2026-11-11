---
type: known-solution
description: "The Witcher 2's Linux tenfoot-launcher shows a black screen and closes (basic_string::_S_construct null not valid): its language files have escapes today's GLib refuses. The console starts the game itself instead."
status: solved
seen: 2026-11-11
updated: 2026-11-11
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

Owner, 2026-11-11 ([[games-on-disk]]): the console starts the game's own program, `game/witcher2`, with its folder in
`LD_LIBRARY_PATH`, as GOG's `start.sh` does: the list of known games (`frontend/known-games/known-games.json`, by the GOG
id in `gameinfo`) names it; owneet-frontend 0.38.16. The game's files are never changed.

## How we found it

1. Test VM, the owner's copy of the game: `gdb --args ./tenfoot-launcher`, `catch throw`, `bt`: the throw comes from
   building a string from `g_key_file_get_string`'s result.
2. A breakpoint on `g_key_file_get_string` printing group and key: the last one is `[InputEditor] IK_Backslash`, NULL.
3. The line in the `.ini` files: `IK_Backslash=\ (Backslash)`; escaped as `\\ (Backslash)` in a copy, the launcher runs.

## Watch out

- Other old Linux games that read GLib key files written for an older GLib can fail the same way: look for a NULL from
  `g_key_file_get_*` and backslashes in their `.ini` files.
- A game with a launcher that does not work: add it to `known-games.json` with the game's own program
  (`frontend/known-games/README.md`).
