---
type: decision
description: "Automatic mounting of every disk, read-only dirty NTFS, moving games and media between disks."
area: games
status: active
decided: 2026-10-03
updated: 2026-10-11
legacy: "PROJECT_RULES.md §6 (mounting, moving)"
tags: [decision, games, disks]
---
# Disks: automatic mounting and moving games

- **Automatic mounting** of all internal disks and removable drives (ext4, btrfs, NTFS, exFAT), at
  boot and on hot-plug, with automatic scanning for game libraries and media folders.
  - NTFS left dirty by Windows Fast Startup / hibernation → mount read-only and explain why.
  - Windows games on NTFS with Proton are unreliable → readable, but suggest moving them.
- **Moving games and media between disks** (Wave 1, roadmap 6.6): e.g. from a USB stick to the
  console's disk, with progress and cancel; the original is deleted only after the copy is
  checked. Steam games are moved by Steam itself (its storage settings, opened from the console).
- The library shows the disks with their free space and notices ([[home-and-library]]).

Guard: [[user-data]]. Steps: [[step-6.5-automatic-disk-mounting]],
[[step-6.6-moving-games-and-media-between-disks]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-11 | **Wave 1 scope grows** ([[disks]] and 10): DRM-free games on a disk play whatever their form (ready to run or installer, Linux or Windows through umu-launcher + GE-Proton, hidden from the user); installers run by themselves in the background; moving games and media between disks (new step 6.6). Games folder: `Games` or its translated name, one folder per game with any sub-folders, searched recursively. "Add games" also offers "From a USB stick or disk". |
