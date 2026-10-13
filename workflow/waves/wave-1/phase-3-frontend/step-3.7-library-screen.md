---
type: step
phase: "[[phase-3-frontend]]"
step: "3.7"
status: done
legacy: "ROADMAP.md 3.7"
tags: [step, phase-3]
---
# 3.7 Library screen

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** unified grid, filters on LT/RT, sort on Y, disks with free space.
- **Demo:** `design/demos/3.7-library.html`. Proposals in it: a grid of seven covers per row that
  scrolls with the selection (right stick: three rows at a time); filters All / Installed /
  Favorites / Steam / Local with their counts, switched only with LT / RT (the chips are not
  selectable); Y opens "Sort by" (Recently played, Name, Most played) and the current sort is
  shown beside the filters; games owned but not installed (Steam) are dimmed with a download mark
  and A reads "Install" (opens Steam: phase 4); favourites have a heart; X details (with the disk
  and size) and Menu options as on the home screen; disks with their free space in the header
  (from the system: phase 6); "No favorites yet" explains how to add one.
- **Review 1 (2026-10-09):** the prompt bar cut the focus ring of the last row: scrolling lists
  and grids keep room for the ring and the lift at both ends (in QML: the view's margins and the
  range the selection is kept in).
- **Review 2 (2026-10-09):** several disks. Up to two are shown in the header; with three or more,
  one summary ("4 disks · 2.3 TB free"). The disks are selectable (up from the first row of games,
  down to come back) and A opens the **Disks** window: every disk with its free space and the
  notices of [[disks]] (read-only NTFS left by Windows; Windows games on NTFS).
  Demo key D and `#disks=1|2|4` try 1, 2 or 4 disks.
- **Demo approved** on 2026-10-09.
- **Outcome:** `LibraryPage.qml` as in the demo: a grid of seven covers per row (room for the focus
  ring at both ends, right stick three rows at a time), filters All / Installed / Favorites /
  Steam / Local with counts on LT / RT, "Sort by" on Y (Recently played, Name, Most played; the
  choice is saved), favourites with a heart, X details and Menu options (without "Show in
  library" here), "No favorites yet". Disks: a new `owneet::Storage` (C++, `storage` in QML) lists
  the system disk and the disks mounted under /run/media, /media and /mnt with their free space;
  up to two in the header, a summary with more; up from the first row, A opens the **Disks**
  window (read-only disks say so). `Dialog` reworked: its own content sits between the text and
  the buttons. Checked with `tools/frontend-preview` (`tools/preview-steps/library.txt`).
  **Still to come:** owned-but-not-installed Steam games (dimmed, "Install") with the Steam
  integration (4.1–4.2); the Windows-disk notices and disk names with automatic mounting (6.5).
