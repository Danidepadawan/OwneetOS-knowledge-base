---
type: known-solution
description: "Steam's storage (controller interface) has no 'Add drive': a second disk cannot be chosen to install a Steam game. The system must hand the disk to Steam with steam://addlibraryfolder, as SteamOS does."
status: solved
seen: 2026-11-08
updated: 2026-11-09
tags: [known-solution, steam, disks]
---
# Steam cannot add a disk from its controller interface

## Symptom

On FrankenPC, with a second disk prepared for games and mounted read-write, Steam's Settings → Storage
(opened from the console, `steam://settings/storage`) shows only the console's own library: **no "Add
drive" button**, no list of disks, no message. Installing a game offers only the console's disk. Steam's
logs (`content_log.txt`, `console_log.txt`) say nothing about the disk: "Loaded … (1 libraries)".

## Cause

Steam started with `-gamepadui` on a system that is not SteamOS gives no way to add a library folder with
the controller. On SteamOS it is the system's own mounter (`/usr/lib/hwsupport/steamos-automount.sh`) that
tells Steam about each disk it mounts. Forum posts blaming `/run/media` (Steam's desktop folder picker
hides it) are about the desktop interface, which the console never shows.

## Solution

owneetd 0.25.4 (`daemon/internal/apps/steamdisks.go`): **while Steam is closed, right before the console starts it**, each
disk the console prepared for games is written into Steam's list of libraries, as Steam writes it: a numbered block in
`steamapps/libraryfolders.vdf` and in its copy `config/libraryfolders.vdf` (Steam keeps both; it reads `steamapps/` first),
with `path` `<disk>/SteamLibrary`, `label` the disk's name (Steam shows the label instead of the folder), a random
`contentid`; the folder gets `steamapps/` and `libraryfolder.vdf` with the same contentid and label. Steam loads it at
start ("Loaded … (2 libraries)") and keeps it. Only the disks the console prepared (owner, [[disks]]).

**What did not work:** `steam steam://addlibraryfolder/<folder, every byte as %xx>`, SteamOS's way (owneetd 0.25.3):
Steam logs `ExecuteSteamURL: "steam://addlibraryfolder/%2f…"` and nothing more (FrankenPC, 2026-11-09).

## How we found it

- FrankenPC's logs (2026-11-08): the disk mounted rw at `/run/media/owneet/2TB HDD SATA`, its top owned by
  the console's user, no `noexec`: nothing on the console's side stopped Steam.
- The owner: no "Add drive", no list, no message in Steam's storage.
- A faithful copy of SteamOS's mounter (github.com/scawp/Steam-Deck.Mount-External-Drive, `automount.sh`):
  `send_steam_url "addlibraryfolder" "${mount_point}/SteamLibrary"` after `mkdir -p` of that folder,
  `urlencode` turning every byte into `%xx`, sent only when a `steam` process runs.
- Test VM: Steam with nobody signed in takes the address and shows nothing (no `libraryfolders.vdf`).
- Test VM with the owner signed in (2026-11-09): the entry written while Steam was closed is loaded at start, the disk
  shows in Storage (by its label) and among the places to install.

## Watch out

Steam writes its list itself while it runs: write it only while Steam is closed. Steam must be signed in to show the result. A disk not prepared by the console (any other ext4, exFAT,
NTFS) is never handed: that is the owner's choice, not a limit of Steam.
