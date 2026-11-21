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
  place. With more than six it shows five apps and "All apps": while six or fewer are installed, the
  first five of that order, the **installed apps before the missing ones**; **from the seventh
  installed app, the five most used**, the most used first (every opening from the console counts,
  since the app was installed; removing it clears its count; equal counts follow the fixed order).
  "All apps" opens the **Apps page**: every app in a grid of tiles, in the fixed order with the
  installed apps before the missing ones ([[step-5.7-apps-page]]).
- **Library disks:** up to two disks shown in the header; with three or more, one summary. The disks
  are reached with up from the first row and A opens a window listing every disk with its free
  space and notices (demo 3.7, review 2).
- **Offline** is shown in the top bar with a crossed network icon (Wi-Fi, or cable on machines
  without Wi-Fi), not by hiding it.
- **Details window:** a value too long for the window (an installer's file name) is shortened in the
  middle with "…"; the window keeps its width (owner, 2026-11-10).
- **Covers' titles** (owner, 2026-11-13, open item 3ad): one line; a title that does not fit ends
  with "…" and scrolls while its cover is highlighted (the rule of [[design-direction]] for long
  texts), so the source badge never sits over it. A change of look: demo
  `design/demos/3.7b-cover-title-scroll.html`, approved 2026-11-13; built in owneet-frontend 0.38.29.
- Library filters and "Add games": [[game-library]].

Steps: [[step-3.6-home-screen]], [[step-3.7-library-screen]], [[step-5.7-apps-page]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-09 | Overflow rule ([[design-direction]]): a list larger than its place opens the full list from its last place. Library: up to two disks shown, with three or more one summary; the disks are reached with up from the first row and A opens a window listing every disk with its free space and notices (demo 3.7, review 2). |
| 2026-10-09 | Offline is shown in the top bar with a crossed network icon (Wi-Fi, or cable on machines without Wi-Fi), not by hiding it. |
| 2026-10-09 | Offline icon approved; next: demo 3.9 (Settings). |
| 2026-11-10 | Details window: a value too long for it is shortened in the middle with "…" (owner chose this over wrapping). |
| 2026-11-12 | The home's big card: when its rows do not fit (text size XL, a title on two lines), the space between them shrinks from 12 px down to 4 px; the title stays whole (owner, option 2 of 3w d). |
| 2026-11-13 | The home's big card when its rows do not fit even 4 px apart (text size XL, a long title): the title on one line, "…", scrolling while a button of the card is selected; the buttons clipped at the card's edge, sliding to the selected one (owner's idea; demo 3.6c approved). |
| 2026-11-13 | Covers' titles on one line, "…" when they do not fit, scrolling while the cover is highlighted (owner, after the badge was seen over a three-line title); demo 3.7b to approve. |
| 2026-11-13 | Demo 3.7b (covers' titles on one line, scrolling when highlighted) approved. |
| 2026-11-13 | The library's Options on the running game: "Resume", "Resume with the pointer", "Close game", then the usual options (demo 3.7c approved; the cover's badge and A = "Resume" not wanted). |
| 2026-11-20 | Step 5.7: the home's apps in one fixed order, installed first; with more than six apps the first five and "All apps", which opens the Apps page (a grid of tiles, the same order, the home grid's buttons). |
| 2026-11-20 | Step 5.7, after the demo (owner): the built-in apps (Videos, Music, the store) first, then the web apps; with six apps or fewer a missing app keeps its place; with more than six the installed ones come before the missing ones. |
| 2026-11-20 | Step 5.7 (owner): from the seventh installed app the home shows the five most used apps (each opening from the console counts, all time); with six installed or fewer its places stay fixed; the Apps page keeps the fixed order. |
