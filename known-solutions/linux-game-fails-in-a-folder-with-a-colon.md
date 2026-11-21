---
type: known-solution
description: "A Linux game stops at once (The Witcher 2: \"eON failed to initialise!\") or misses its own libraries: its folder's name has \":\", the separator of Linux path lists (ICU data, LD_LIBRARY_PATH)."
status: solved
seen: 2026-11-11
updated: 2026-11-11
tags: [known-solution, linux-games, installers]
---
# A Linux game fails in a folder with ":" in its name

## Symptom

The Witcher 2 (GOG, Linux, eON port), installed by the console into `Giochi/The Witcher 2: Assassin of kings`, started
directly (`game/witcher2`): it ends at once. Its own log `~/.local/share/cdprojektred/witcher2/eon.txt` says "eON failed to
initialise!" after failing to load ICU's data (`icudt52l.dat`, error 4, U_FILE_ACCESS_ERROR), although the file is in
`game/`. With the folder renamed without ":", the same game starts (OpenGL, sound, Direct3D 9 over OpenGL).

## Cause

Linux lists of folders use ":" as their separator: ICU's data path (eON points it at the game's folder), and
`LD_LIBRARY_PATH` (which GOG's `start.sh` sets to the game's folder for `libopenal-eon.so.1`). A folder name with ":" is cut
in two, and neither half exists. Folder names like "Title: Subtitle" are common, because the console names the folder
after the game. It is the Linux side of [[windows-installer-folder-with-a-colon]].

## Solution

Owner, 2026-11-11 ([[games-on-disk]]): the console never installs a game into a folder whose name has ":". owneetd 0.25.24
(`installs.FolderName`) and owneet-frontend 0.38.16 (`DiskGames::installFolderName`, the same rule) write `: ` as ` - `:
an installer on another disk goes to a new folder without ":"; a game folder with an installer already on the console's
disk is renamed first (owner's choice). The title keeps the ":" (the mark `.owneet-installed` holds it). The interface
adds a program's folder to `LD_LIBRARY_PATH` only when the folder has no ":".

## How we found it

1. In the test VM, `witcher2` started by hand in its folder with `LD_LIBRARY_PATH=.`: ends at once, `eon.txt` shows the
   ICU error.
2. The file was there and readable, and ICU takes a list of folders split at ":": the folder's name was the only
   difference left.
3. The folder renamed to "The Witcher 2 - Assassin of kings": eON starts.

## Watch out

- Games the user copies by hand into a folder with ":" are not renamed (the console does not touch them); if one fails
  the same way, this is the first thing to check.
- Any list of paths built from a game's folder (`PATH`, `LD_LIBRARY_PATH`, `XDG_*`) has the same problem.
