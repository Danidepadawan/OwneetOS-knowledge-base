---
type: decision
description: "Banners, bell and list on Y; attention vs info sounds; nothing drawn over a game."
area: ux
status: active
decided: 2026-10-11
updated: 2026-10-11
legacy: "PROJECT_RULES.md §13 (2026-10-11); ROADMAP 3.11"
tags: [decision, ux, notifications]
---
# Notifications

- **Banners** at the top right, under the top bar (at most three, newest on top, gone after 5 s);
  a **bell** in the top bar counts the ones not seen yet; **Y on the home screen** opens the list
  (a page-level option, [[controller-input-map]]).
- Two kinds: "attention" (sound `notify-error`: battery low, controller disconnected, Wi-Fi lost,
  game closed unexpectedly, disk read only) and "info" (sound `notify`).
- **Nothing is drawn over a game** (the overlay is Wave 2): notifications wait in the list.
- What the user just did is not news ([[ui-patterns]]).

Step: [[step-3.11-notifications]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-11 | Demo 3.11 (notifications) approved: banners at the top right, a bell in the top bar, the list on Y from the home screen ([[controller-input-map]]: page-level option); nothing drawn over a game. Notifications that need attention get a sound of their own, `notify-error` (eleven sounds, [[interface-sounds-spec]]); `error` stays for something just done that failed. |
