---
type: decision
area: ux
status: active
decided: 2026-10-08
updated: 2026-10-11
legacy: "PROJECT_RULES.md §13 (2026-10-08 – 2026-10-11)"
tags: [decision, ux, sounds]
---
# Interface sounds

- The interface has sounds; the **owner provides the WAV files**.
- **Eleven sounds** (ten agreed on 2026-10-09, `notify-error` added on 2026-10-11): one "click"
  (`nav-confirm`) for A, B, filters, switches, volume and on-screen keyboard; one sound for notices
  and successes (`notify`), one for notifications that need attention (`notify-error`), one for
  something just done that failed (`error`); game launch and Guide over a game share one;
  `startup` required. **One sound per button press.**
- Until the owner's final sounds arrive (before the public launch, after the legal review, roadmap
  7.7), the interface uses **CC0 placeholders by Kenney** (`frontend/sounds/`). Six of the owner's
  sounds were delivered on 2026-10-09 (FL Studio, GPL-3.0-or-later).
- Sound outputs never go to sleep, and the interface loops silence from its start, so the first
  sound is never late or cut.

Spec: [[interface-sounds-spec]]. Practice: [[sound-files]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-08 | Interface sounds planned (roadmap 3.12, list in [[interface-sounds-spec]]): WAV files provided by the owner. |
| 2026-10-09 | Interface sounds reduced to ten ([[interface-sounds-spec]]): one "click" (`nav-confirm`) for A, B, filters, switches, volume and on-screen keyboard; one sound for notices and successes, one for errors and warnings; game launch and Guide over a game share one; `startup` required. LT/RT switch filters only: no sub-tabs inside pages ([[controller-input-map]]). |
| 2026-10-09 | Demo 3.6 (home screen) approved. The owner made six of the ten sounds with FL Studio (GPL-3.0-or-later, `frontend/sounds/SOURCES.md`); the other four stay Kenney placeholders. |
| 2026-10-09 | The owner's final sounds are delivered before the public launch, after the legal review (roadmap 7.7); until then the interface uses CC0 placeholders by Kenney (`frontend/sounds/`). |
| 2026-10-11 | Demo 3.11 (notifications) approved: banners at the top right, a bell in the top bar, the list on Y from the home screen ([[controller-input-map]]: page-level option); nothing drawn over a game. Notifications that need attention get a sound of their own, `notify-error` (eleven sounds, [[interface-sounds-spec]]); `error` stays for something just done that failed. |
| 2026-10-11 | Step 3.12 (interface sounds) done; the first sound after boot needs the sound output running first (a looped silence). Demo 3.13 approved: animated start-up from the boot splash's wordmark; a **quick menu** (side panel from the right, as on SteamOS) with power options and a read-only "Controls and features" guide, opened by **B where there is nothing to go back to** (an accidental press only opens the menu). View stays reserved for screenshots in a later wave ([[controller-input-map]]). |
