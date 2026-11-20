---
type: decision
description: "Overflow rule, library disks summary and Disks window, offline icon in the top bar."
area: ux
status: active
decided: 2026-10-09
updated: 2026-11-20
legacy: "PROJECT_RULES.md §9 (overflow), §13 (2026-10-09)"
tags: [decision, ux]
---
# Home screen, library and top bar

- **Overflow rule:** when a list has more items than its place on screen, the last place opens the
  complete list instead ("All games" on the home screen, "All apps" with more than six apps, the
  disks summary in the library with more than two disks). Practice: [[ui-patterns]].
- **The home's apps** (step 5.7, owner 2026-11-20): one fixed order, **the built-in apps first**
  (Videos, Music, the store), then the web apps in the catalogue's order; the tiles do not move as
  they are used. With six apps or fewer the home shows every app, a missing one dimmed in its
  place. With more than six it shows the first five, the **installed apps before the missing
  ones**, and "All apps", which opens the **Apps page**: every app in a grid of tiles, in that same
  order ([[step-5.7-apps-page]]).
- **Library disks:** up to two disks shown in the header; with three or more, one summary. The disks
  are reached with up from the first row and A opens a window listing every disk with its free
  space and notices (demo 3.7, review 2).
- **Offline** is shown in the top bar with a crossed network icon (Wi-Fi, or cable on machines
  without Wi-Fi), not by hiding it.
- Library filters and "Add games": [[game-library]].

Steps: [[step-3.6-home-screen]], [[step-3.7-library-screen]], [[step-5.7-apps-page]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-09 | Overflow rule ([[design-direction]]): a list larger than its place opens the full list from its last place. Library: up to two disks shown, with three or more one summary; the disks are reached with up from the first row and A opens a window listing every disk with its free space and notices (demo 3.7, review 2). |
| 2026-10-09 | Offline is shown in the top bar with a crossed network icon (Wi-Fi, or cable on machines without Wi-Fi), not by hiding it. |
| 2026-10-09 | Offline icon approved; next: demo 3.9 (Settings). |
| 2026-11-20 | Step 5.7: the home's apps in one fixed order, installed first; with more than six apps the first five and "All apps", which opens the Apps page (a grid of tiles, the same order, the home grid's buttons). |
| 2026-11-20 | Step 5.7, after the demo (owner): the built-in apps (Videos, Music, the store) first, then the web apps; with six apps or fewer a missing app keeps its place; with more than six the installed ones come before the missing ones. |
