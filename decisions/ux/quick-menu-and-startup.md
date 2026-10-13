---
type: decision
area: ux
status: active
decided: 2026-10-11
updated: 2026-10-11
legacy: "PROJECT_RULES.md §13 (2026-10-11); ROADMAP 3.13"
tags: [decision, ux]
---
# Quick menu and start-up animation

- **Animated start-up** from the boot splash's own picture (the wordmark), with the start-up sound,
  once per boot; "Reduce motion": a plain fade.
- A **quick menu** (side panel from the right, as on SteamOS) with "Power options" and a read-only
  "Controls and features" guide, opened by **B where there is nothing to go back to** (Home,
  Library, the list of Settings sections): an accidental press only opens the menu. The owner chose
  B over View; **View stays reserved for screenshots** in a later wave.
- Power options: Sleep, Restart, Shut down, **Cancel selected**; with a game running it says that
  Restart and Shut down close it.

Step: [[step-3.13-start-up-animation-and-power-options]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-11 | Step 3.12 (interface sounds) done; the first sound after boot needs the sound output running first (a looped silence). Demo 3.13 approved: animated start-up from the boot splash's wordmark; a **quick menu** (side panel from the right, as on SteamOS) with power options and a read-only "Controls and features" guide, opened by **B where there is nothing to go back to** (an accidental press only opens the menu). View stays reserved for screenshots in a later wave ([[controller-input-map]]). |
