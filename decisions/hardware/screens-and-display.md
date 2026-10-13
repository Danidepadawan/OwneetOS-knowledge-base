---
type: decision
description: "One screen, others off; Keep this? after 15 s (30 s for a new screen); brightness only where possible."
area: hardware
status: active
decided: 2026-10-08
updated: 2026-10-10
legacy: "PROJECT_RULES.md §13 (2026-10-08, 2026-10-10)"
tags: [decision, hardware, display]
---
# Screens and display

- **One screen.** The console uses one screen, chosen in Settings among all detected screens;
  **the other screens are turned off** (replaces the 2026-10-08 choice of not turning them off).
  Showing the logo on the other screens becomes an optional choice after Wave 1 ([[wave-2]]).
- Moving the console to another screen restarts the display for a few seconds, so it **waits
  until no game is open**.
- **"Keep this?"**: a new resolution or refresh rate goes back to the previous one after
  **15 seconds** without an answer (a TV may show no picture). Moving to another screen waits
  **30 seconds**, counted from the moment the console is up there (a monitor waking from standby
  may stay black for a while); before moving, a window warns that the new screen may stay black
  for up to 30 seconds.
- **Brightness** is shown only on screens that allow it (laptop backlight through logind, monitors
  through DDC/CI with `ddcutil`; TVs usually not).
- **Picture dimming** for screens without a brightness control: a proposal for Wave 2, not
  confirmed ([[wave-2]]).

Technical design: [[owneetd-api-display]]. Settings screen: [[settings-screens]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-08 | Several screens: the console uses one (choice in Settings, step 3.9); the others are not turned off by default, a use for a second screen may come later. |
| 2026-10-10 | Display (step 3.9, part 3): the console uses **one screen**, chosen in Settings among all detected screens; **the other screens are turned off** (replaces the 2026-10-08 choice of not turning them off). Showing the logo on the other screens becomes an optional choice after Wave 1. Moving the console to another screen restarts the display for a few seconds, so it waits until no game is open. |
| 2026-10-10 | A new screen, resolution or refresh rate asks "Keep this?" and goes back to the previous one after **15 seconds** without an answer (a TV may show no picture). |
| 2026-10-10 | Moving the console to another screen waits **30 seconds** for "Keep" (from the moment the console is up there: a monitor waking from standby may stay black for a while); resolution and refresh rate keep 15 seconds. Before moving, a window warns that the new screen may stay black for up to 30 seconds. |
| 2026-10-10 | Step 3.9 (Settings) approved after the owner's tests on the NiPoGi and the desktop (two graphics cards). Picture dimming for screens without a brightness control stays a proposal for Wave 2 (not confirmed). Next: demo 3.10 (on-screen keyboard). |
