---
type: decision
area: ux
status: active
decided: 2026-10-09
updated: 2026-10-11
legacy: "PROJECT_RULES.md §9 (overflow), §13 (2026-10-09)"
tags: [decision, ux]
---
# Home screen, library and top bar

- **Overflow rule:** when a list has more items than its place on screen, the last place opens the
  complete list instead ("All games" on the home screen, "All apps" with more than six apps, the
  disks summary in the library with more than two disks). Practice: [[ui-patterns]].
- **Library disks:** up to two disks shown in the header; with three or more, one summary. The disks
  are reached with up from the first row and A opens a window listing every disk with its free
  space and notices (demo 3.7, review 2).
- **Offline** is shown in the top bar with a crossed network icon (Wi-Fi, or cable on machines
  without Wi-Fi), not by hiding it.
- Library filters and "Add games": [[game-library]].

Steps: [[step-3.6-home-screen]], [[step-3.7-library-screen]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-09 | Overflow rule ([[design-direction]]): a list larger than its place opens the full list from its last place. Library: up to two disks shown, with three or more one summary; the disks are reached with up from the first row and A opens a window listing every disk with its free space and notices (demo 3.7, review 2). |
| 2026-10-09 | Offline is shown in the top bar with a crossed network icon (Wi-Fi, or cable on machines without Wi-Fi), not by hiding it. |
| 2026-10-09 | Offline icon approved; next: demo 3.9 (Settings). |
