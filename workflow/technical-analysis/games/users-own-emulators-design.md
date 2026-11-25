---
type: technical-analysis
description: "Step 4.9: how the console finds and starts the user's own emulators (folders, kinds of programs, options, archives, pointer), what was checked and what is still to try. No emulator or console is named."
component: games
tags: [technical-analysis, games, emulators]
---
# The user's own emulators: how

For [[step-4.9-the-users-own-emulators]]. Decision: [[users-own-emulators]]. **No emulator and no console is ever named here** (owner, 2026-11-25).

```
FunContainer/            the user's name for the console (invented here)
  Emulators/             (Emulatori, ...) one folder or file per emulator
  Games/                 (Giochi, ...) one file or folder per game
```

- **Found by its two sub-folders**, at the top of a disk or inside the Games folder (there, before 4.9, it was read as one PC
  game). The console's own "Add games" makes it inside the Games folder: the file manager, the moving between disks and the covers
  go on working.
- **Emulators:** the kinds a game on a disk may be (AppImage, program, script; a Windows program through Proton is a hypothesis).
  More than one: asked once per console, changed from Options.
- **Games:** one file, or a folder (the file to start asked once, as for games on a disk). Title: the name as written. Discs written
  as a text list and their tracks (`.cue`, `.m3u`) are one game.
- **Starting:** the emulator, its options, the game's path. Among the programs looked at, most need the path alone, some one
  option before it. Options: typed once ("How it starts"), split by spaces, double quotes keep a name together, anywhere in a word.
  No shell: `;`, `&`, `$` are plain signs (owneetd, `execCommand`). The interface's `CommandTokenizer` takes quotes only at a word's
  start and replaces `{...}`: not used for the options.
- **Closed straight away:** said, with "How it starts" and "Open the emulator".
- **Its own settings:** "Open the emulator" without a game, with the controller pointer on by itself for all its windows until it ends
  ([[controller-input-map]]). The console writes no emulator's settings.
- **What the console takes off the user:** makes the folders; opens an emulator in an archive by itself (`.zip`, `.7z`, `.tar`); gives
  the exec bit where the disk has none; unpacks an AppImage once.
- **Guide, close, "Starting ...":** as any game on a disk.

**For the law** (opinion, to [[step-7.5-legal-review-before-the-public-launch]]): OwneetOS names, ships, downloads, links and configures
none: it starts a program of the user's with a file of the user's. A notice once per emulator: other people's program, the user's
responsibility. It never decrypts anything, never holds keys, system files or games ([[legal]]).

**Checked (2026-11-25, builder VM, unpacked and never run, deleted after):** three AppImages unpack in 0.1 s or less (up to 180 MB; a
slow disk takes longer) and ask the system only for libraries whose packages the console has. `bsdtar` (libarchive, already there)
opens a `.7z` and keeps the exec bit. Flatpak and Snap cannot be used here.

**Still to try on the console:** running one; whether its bars stay on screen; the pointer in its settings; saves on a read-only
disk; an emulator that answers to Guide by itself (programs see the controller; not OwneetOS's binding).
