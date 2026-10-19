---
type: technical-analysis
description: "How games on a disk are found and started (step 4.3): read-only mounting of USB disks, the disk-games provider, the file to start, plug and unplug."
component: owneet-frontend
tags: [technical-analysis, frontend, games]
---
# owneet-frontend: games on a disk (step 4.3)

Up: [[frontend-architecture]] · Behaviour: [[games-on-disk]], [[step-4.3-local-drm-free-games]] ·
Demo: `design/demos/4.3-games-on-disk.html`

## Mounting (owneet-base, until [[step-6.5-automatic-disk-mounting]])

- `90-owneet-usb-disks.rules` (udev): a file system on a **USB** disk (ext2/3/4, btrfs, xfs, vfat,
  exFAT, NTFS) pulls in `owneet-mount-ro@<kernel name>.service`. USB is recognised by the
  device's path (`ID_PATH` with `-usb-`): USB-SATA adapters with UAS (e.g. JMicron 152d:0583, the
  owner's SSD on the FrankenPC, 2026-10-15) give `ID_BUS` "ata", so `ID_BUS` is not used. Not the OWNEETLOG stick, not EFI
  system partitions (e.g. the installation stick's), not internal disks (the tester installer
  only offers internal disks, so it never meets a mounted one).
- `owneet-mount-ro start|stop <name>` (root): mounts **read only** at
  `/run/media/owneet/<label>` (the kernel name without a label), `nosuid,nodev`, journals not
  replayed (`noload`, `norecovery`, `rescue=nologreplay`: nothing is ever written); vfat, exFAT
  and NTFS (`ntfs3`) owned by the console user (uid 1000). A device already mounted is left
  alone. The unit `BindsTo` the device: unplugging stops it (lazy unmount, folder removed).
- Games start from the disk, so it is not `noexec`. Windows disks left dirty are only read
  ([[user-data]]).

## Finding the games (`providers/owneet_disk/DiskGamesProvider.cpp`)

Runs at every reading of the games (not cached). Roots: the home folder ("internal") and every
mounted disk Storage lists (`/run/media`, `/media`, `/mnt`); `OWNEET_DISKS` adds folders that act
as disks (previews). In each root, a top-level folder named `Games` or a translation
(`owneet::DiskGames::folderNames()`: games, giochi; case does not matter); each of its folders is
a game.

- **What can start** (searched 5 sub-folders deep, at most 20 000 entries per game): ELF programs
  for x86 / x86-64 with the exec bit (no extension, `.x86_64`, `.x86`, `.amd64`, `.bin`),
  `.sh` scripts (run with bash, no exec bit needed), `.AppImage` with the exec bit (run with
  `APPIMAGE_EXTRACT_AND_RUN=1`: no FUSE in the system). Never: names with unins, setup, install,
  config, redist, directx, dxsetup, crash reporters; folders `support`, `docs`, `manual`,
  licences, redistributables, Unity's `*_Data`, hidden ones. A `.sh` with "makeself" or
  "MojoSetup" in its first 64 KiB is an installer (step 4.6).
- **Only an installer (4.6)**: the best installer of the folder (kinds the console can use
  first, then the shallowest) makes a game "not installed" with `disk.installer` and
  `disk.installer.kind`: `sh` (a makeself / MojoSetup script whose ZIP list, in its last 4 MiB,
  names `data/noarch/`; other scripts `unknown`), `inno` / `nsis` (an `.exe` named setup /
  install, not unins, whose first 4 MiB say "Inno Setup" / "Nullsoft"; else `unknown`), `msi`,
  `galaxy` (`GOG_Galaxy_*.exe`, never a Windows game's file). Folders marked `.owneet-installing`
  are not listed; a game folder marked `.owneet-installed` has `disk.installed` and
  `disk.installed.from` (its installer), and hides installers of the same folder name on other
  disks. `DiskGames::installRequest(game, language)` gives owneetd's request
  ([[owneetd-api-installs]]): `dest` in the home folder's games folder (made as `Giochi` / `Games`
  by the console's language when there is none; the game's own folder when its installer is
  already on the console's disk), `prefix` = `windowsPrefix(dest)`. `folderSize(path)`: what
  uninstalling frees. Folders with nothing at all are not listed; the log says which.
- **Installers in the theme (4.6, approved demo `design/demos/4.6-installers.html`)**:
  `GameInfo.steamState` gives such a game `none`, `queued`, `installing` (with `progress`, none
  for Windows installers: the cover's bar keeps moving) or `unusable`, from owneetd's installs
  (`GameInfo.installs`, matched by folder name), so filters, sorting and covers treat it as a game
  not installed. A: unusable → why; Windows installer before Windows games are ready → their
  progress; inspect → "Not enough space" or "Install {game}?" [Read] [Install] [Cancel]; Read
  shows the licence in a scrolled box (right stick) or where it is. Options: Stop installing,
  Uninstall (`disk.installed`). `install.done` notifies and reads the games again quietly
  (`readGamesQuietly`, as for disks). Preview: `tools/preview-steps/installers.txt` and
  `installers-windows.txt` (`@disk` has GOG `.sh`, Inno Setup, too big, Galaxy, unknown, and a game
  installed earlier; `fake-owneetd.py` installs in a few seconds).
- **The file to start**: the user's saved choice → `game.txt`'s `start` → `start.sh` at the top of
  the folder (GOG) → the only file found → none (the theme asks).
- **`game.txt`** (optional; format agreed with the owner, [[games-on-disk]]): `key: value` lines,
  keys `title`, `start` (relative path), `description`; `#` starts a comment.
- **The game**: collection "Games on disks" (local, not Steam), its file is the game's folder (play
  time and owneetd's app id stay the same when the chosen file changes); title = `game.txt`'s or
  the folder's name as written; cover = `cover.jpg` / `.png` / `.jpeg` / `.webp` at the top
  (asset `boxFront`). Extras: `disk.dir`, `disk.root` (mount folder or "internal"), `disk.files`
  (relative paths, top-level first), `disk.start`.

## Windows games (step 4.5)

A folder with nothing to start on Linux but `.exe` files is a Windows game (`disk.windows`): it
starts as GOG's `goggame-<id>.info` says (the primary `FileTask`: path, arguments, working folder;
each part of the path matched without case, e.g. `DOSBOX\dosbox.exe` → `DOSBOX/DOSBox.exe`),
otherwise the usual choice among its `.exe` files (never setup, uninstallers, configurators such
as `GOGDOSConfig.exe`, help programs, `__redist`). The command is
`/usr/lib/owneet/owneet-windows-run <prefix> <exe> <GOG's arguments>` ([[owneetd-api-windows]]).
The theme tells owneetd when the library has one (`POST /v1/windows/needed`), blocks a start
until owneetd's download is ready (its progress, or "connect to the internet"), and shows
"Preparing {game}…" (the Steam preparing screen, `windows: true`) until the game is on screen;
`diskGames.firstStart(game)` (no `pfx` in its prefix yet) adds "The first start takes a little
longer". Preview: `tools/preview-steps/windows-games.txt`.

## The file to start (`owneet::DiskGames`, `diskGames` in QML)

`chosen(game)` (relative path, "" when the user must choose), `choose(game, file)` (sets the
launch command and working folder at once and saves `~/.config/owneet-frontend/disk-games.json`:
game folder → file), `hasGames(root)`. The theme asks "Which file starts {title}?" at the first
start (mode `chooseFile` of the dialog) and offers Options → "Choose the file to start" when
there are several.

## Plug and unplug

`owneet::Storage` emits `volumesChanged` when the mount table changes (`/proc/self/mountinfo`
polled for priority data, 0.7 s to settle; with `OWNEET_DISKS`, a watcher on the parent folder).
The theme compares the disks: a new disk with a games folder, or a gone disk that had games, makes
it read the games again **quietly** (owner, 2026-10-16: only the notice, as in a real OS): it sets
`diskGames.quietReading` and calls `reloadProviders`; then `main.qml` keeps the theme loaded and
shows no loading screen, and `Backend` keeps the old games until the new ones are ready, replaces
them in one go and clears the flag. The old game objects are never deleted (Pegasus never deletes
them), so windows and lists that still hold one stay safe; the theme refreshes its lists on
`gamedataReady`, the library finds its selected game again (`GameInfo.sameGame`: app id, folder or
title), and a window about a game of a disk that is gone closes. The notice ("USB disk connected:
N games found…" / "USB disk removed") is kept in `api.memory` (`diskNotice`) until the games are
ready. While a game runs, the reading waits for its end. Disks without games change nothing.
Preview: `tools/preview-steps/library-disk.txt` (`@disk`, `plug`, `unplug`).
