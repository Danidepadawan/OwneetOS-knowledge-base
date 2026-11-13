---
type: decision
description: "Automatic mounting of every disk, read-only dirty NTFS, moving games and media between disks."
area: games
status: active
decided: 2026-10-03
updated: 2026-11-13
legacy: "PROJECT_RULES.md §6 (mounting, moving)"
tags: [decision, games, disks]
---
# Disks: automatic mounting and moving games

- **Automatic mounting** of all internal disks and removable drives (ext4, btrfs, NTFS, exFAT), at
  boot and on hot-plug, with automatic scanning for game libraries and media folders.
  - NTFS left dirty by Windows Fast Startup / hibernation → mount read-only and explain why.
  - Windows games on NTFS with Proton are unreliable → readable, but suggest moving them.
- **Moving games and media between disks** (Wave 1, roadmap 6.6): e.g. from a USB stick to the
  console's disk, with progress and cancel (cancel asks first, "Keep going" selected); the
  original is deleted only after the copy is checked. A copy that fails its check is removed and
  the original stays untouched: "The copy did not work" with Close (selected) and Try again; with
  several games the others go on and a summary comes at the end. Steam games are moved by Steam itself (its storage settings, opened from the console).
  A **moved** game takes with it its own folders on the console's disk (a Windows game's prefix: saves,
  settings, what its installer wrote; a DOS game's data), named after the game's folder, and the link its
  install was made through (owner, 2026-11-10). The check of the copy will show its own progress, as the
  copy (demo 6.6d, owner 2026-11-10).
  A moved or copied game keeps the file chosen to start it; a **copied** game gets a copy of those
  folders (owner, 2026-11-10). When those folders cannot be copied, the game's copy did not work: it is removed,
  the original untouched (owner, 2026-11-10). The removal of the original shows its progress too, and a copy that keeps
  the original shows no step for it (demo 6.6d, owner's corrections).
  **A game removed from the console leaves nothing behind on an internal disk** (owner, 2026-11-12): when a Windows
  game on an internal disk (the console's disk or another disk inside the console) and its installer are both
  removed through the console, the console removes the game's prefix too, saves included. A game on an external disk
  (USB, read-only included) keeps its prefix and saves on the console's disk: the user removes them with the file
  manager ([[open-items]] 3t). A prefix whose game is only on a disk not plugged in is never removed automatically.
  **A copy goes on behind its window** (demo 6.6e, approved 2026-11-10): Home on the copy's window closes
  it and shows the home screen (only there: elsewhere Guide keeps its meaning, e.g. back to the open app);
  the top bar and the covers of its games show it, A on one of them shows the window again, so those games
  are never started meanwhile; one copy at a time; its end or its failure with the window closed in a
  notice. **A shutdown or a restart during a copy asks first** and says the copy stops (owner,
  2026-11-10); then, and whenever owneetd stops, the copy and its check stop, the partial copy is removed
  and the game stays where it was ([[user-data]]).
- The library shows the disks with their free space and notices ([[home-and-library]]).
- **Until step 6.5** (owner, 2026-10-15): step 4.3 mounts external disks automatically, read only,
  just enough to read the games on them; the full mounting stays in step 6.5.
- **How (owner, 2026-11-01, step 6.5):** OwneetOS's own small mounter grows (the udev rule and the
  root service of step 4.3), no udisks2 (a daemon and a package more for nothing the console
  needs). Read-write when the file system is clean; NTFS left dirty by Windows read only, with the
  note. **The partition where Windows itself is installed (C:) is always read only**, even when
  Windows was shut down completely: its games can be read, OwneetOS never writes there; other NTFS
  data partitions read-write when clean. **From the USB stick** (live) the internal disks are
  mounted read only (nothing is kept there anyway, and the installer may erase one: it unmounts
  the chosen disk first); USB disks as on the installed console.

Guard: [[user-data]]. Steps: [[step-6.5-automatic-disk-mounting]],
[[step-6.6-moving-games-and-media-between-disks]].

- **Other disks (owner, 2026-11-07):** erased and prepared for games with the controller, in the installer and in Settings → Disks, after a clear warning and the final confirmation ([[step-6.7-preparing-other-disks]]).
- **Disks for games are Steam libraries too (owner, 2026-11-08; how, 2026-11-09):** Steam's interface for the controller
  has no way to add a disk. Every disk **the console prepared for games**, mounted read-write, is written by owneetd into
  Steam's own list of libraries (`libraryfolders.vdf`, both its copies) **while Steam is closed, right before the console
  starts it**: the disk's `SteamLibrary` folder, labelled with the disk's name (Steam shows the label, not the folder). A
  disk plugged in while Steam runs is added at Steam's next start. Other disks are not added. `steam://addlibraryfolder`
  (SteamOS's way, first chosen on 2026-11-08) is ignored by Steam outside SteamOS. A fix of
  [[step-6.7-preparing-other-disks]], not a new feature ([[steam-cannot-add-a-disk-from-its-controller-interface]]).

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-15 | Step 4.3 mounts external disks automatically, read only, just enough to read games on them; full mounting stays in step 6.5 (plan not reordered). |
| 2026-10-11 | **Wave 1 scope grows** ([[disks]] and 10): DRM-free games on a disk play whatever their form (ready to run or installer, Linux or Windows through umu-launcher + GE-Proton, hidden from the user); installers run by themselves in the background; moving games and media between disks (new step 6.6). Games folder: `Games` or its translated name, one folder per game with any sub-folders, searched recursively. "Add games" also offers "From a USB stick or disk". |
| 2026-10-26 | Cancelling a copy or move asks first ("Stop?", "Keep going" selected by default); the copy waits meanwhile. |
| 2026-10-26 | A copy that fails its check: removed, the original untouched, "The copy did not work" with Close (selected) and Try again; with several games the others go on, then a summary. |
| 2026-11-01 | Step 6.5: OwneetOS's own mounter grows (no udisks2); Windows's own partition (C:) always read only; from the USB stick the internal disks read only, the installer unmounts the chosen disk first. |
| 2026-11-07 | Other disks erased and prepared for games from the console: installer and Settings → Disks ([[step-6.7-preparing-other-disks]]). |
| 2026-11-08 | Disks prepared for games by the console become Steam libraries: owneetd hands them to Steam with `steam://addlibraryfolder` (owner: use it; only the disks the console prepared; a fix of step 6.7). |
| 2026-11-09 | Disks for games in Steam: `steam://addlibraryfolder` is ignored outside SteamOS; owneetd writes them into Steam's `libraryfolders.vdf` (both copies) while Steam is closed, before starting it, labelled with the disk's name (owner chose this way). |
| 2026-11-10 | A moved game takes its own folders on the console's disk (Windows prefix, DOS data) and its install's link with it; the check of a copy gets its own progress, demo 6.6d first (owner). |
| 2026-11-10 | A moved or copied game keeps its chosen file; a copy gets a copy of the prefix and DOS data; demo 6.6d: the removal with a progress, no step when the original is kept (owner). |
| 2026-11-10 | Demo 6.6e approved with one correction (owner): Home closes only the copy's window, the copy goes on behind it (top bar, covers, A shows it again, one copy at a time); everywhere else Guide keeps its meaning. A shutdown or restart during a copy is confirmed first; the copy then stops and its partial copy is removed (also when owneetd stops). |
| 2026-11-10 | A copy whose own folders (prefix, DOS data) cannot be copied did not work: removed, the original untouched (owner). |
| 2026-11-12 | A Windows game on an internal disk removed through the console with its installer: its prefix goes too, saves included; games on external disks keep prefix and saves, removed by the user with the file manager (owner). |
| 2026-11-13 | Junk on the disks: a very simplified file manager in Settings → Advanced (folders, delete) in Wave 1, more in Wave 2 (download, move, unzip, rename); a slow disk stays slow, nothing to do for it (owner). |
| 2026-11-13 | The file manager opens on places named for the user (games folders, Windows games' data with their game's name, games' logs), A opens, B up, Delete asks with Cancel selected, system files never shown; the console cleans its packages' cache (last 2 versions) and core dumps by itself; step 6.11 (owner). |
