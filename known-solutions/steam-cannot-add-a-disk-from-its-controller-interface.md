---
type: known-solution
description: "Steam's storage (controller interface) has no 'Add drive': a second disk cannot be chosen to install a Steam game. The system must hand the disk to Steam with steam://addlibraryfolder, as SteamOS does."
status: open
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

As SteamOS does: owneetd hands every disk the console prepared for games to the running Steam with
`steam steam://addlibraryfolder/<folder>`, every byte of the folder written as `%xx`; the folder is
`<disk>/SteamLibrary` (made first) or the disk itself when it has Steam's `libraryfolder.vdf`. Only the
disks the console prepared (owner, [[disks]]). owneetd 0.25.3, `daemon/internal/apps/steamdisks.go`.

**Not enough (FrankenPC, 2026-11-09):** Steam logs `ExecuteSteamURL: "steam://addlibraryfolder/%2f…"` and does
nothing more: no library, no log line, the disk still not offered. Outside SteamOS the address seems ignored.

## How we found it

- FrankenPC's logs (2026-11-08): the disk mounted rw at `/run/media/owneet/2TB HDD SATA`, its top owned by
  the console's user, no `noexec`: nothing on the console's side stopped Steam.
- The owner: no "Add drive", no list, no message in Steam's storage.
- A faithful copy of SteamOS's mounter (github.com/scawp/Steam-Deck.Mount-External-Drive, `automount.sh`):
  `send_steam_url "addlibraryfolder" "${mount_point}/SteamLibrary"` after `mkdir -p` of that folder,
  `urlencode` turning every byte into `%xx`, sent only when a `steam` process runs.
- Test VM: Steam with nobody signed in takes the address and shows nothing (no `libraryfolders.vdf`).

## Watch out

Steam must be signed in to show the result. A disk not prepared by the console (any other ext4, exFAT,
NTFS) is never handed: that is the owner's choice, not a limit of Steam.
