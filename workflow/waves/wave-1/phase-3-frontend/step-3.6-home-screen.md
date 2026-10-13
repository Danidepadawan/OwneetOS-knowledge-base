---
type: step
phase: "[[phase-3-frontend]]"
step: "3.6"
status: done
legacy: "ROADMAP.md 3.6"
tags: [step, phase-3]
---
# 3.6 Home screen

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** home as in the approved mockup (continue playing, apps, jump back in, notices).
- **Demo:** `design/demos/3.6-home.html`. Proposals in it: the hero shows the last game played
  (Play, Details), or the running game when the home is opened with Guide (Resume, Close game
  with a confirmation), or a "no games yet" welcome on a new system (open the Steam Store, how to
  add games); X = details and Menu = options (play, details, favorites, show in library) on any
  game; one notice at a time in the side column (A opens it, X dismisses it, "+N" for the
  others); the prompt bar follows the selected item; the LB/RB glyphs beside the section tabs; no
  profile avatar (profiles come in a later wave); invented game names and generated covers (real
  covers come from local files).
- **Review 1 (2026-10-09):** sounds now play reliably (preloaded players); navigation in groups
  (hero, apps column, row of games): left/right go straight between the hero and the apps and come
  back to the item selected last, inside a group the selection stays on its row or column (to be
  built into `Nav` / `NavArea` as navigation groups with memory); windows have round buttons in a
  centred row, navigated left/right; more space between the hero buttons. With **more than six
  apps**, the sixth tile becomes "All apps", which opens the Apps page (step 5.7).
- **Demo approved** on 2026-10-09 (the sound timing in the browser stays an open point of 3.12).
- **Outcome:** the theme is now a shell with three sections on LB / RB (Home, Library, Settings)
  and the LB / RB glyphs beside the tabs. **Home** as in the demo: hero with the last game played
  (Continue playing / Ready to play, source, last played, play time; Play, Details) or the welcome
  on a system with no games (Open the Steam Store, How to add games); Apps grid; notice slot;
  Recently played (six covers and All games). X = details and Menu = options (Play, Details,
  favorites, Show in library) in compact windows with round buttons. Navigation groups with
  memory and one sound per press built into `Nav` / `NavArea`. Covers: the game's own image from
  local files, otherwise art generated from its title (Steam's local images in 4.1). Library is a
  plain list until 3.7; Settings holds Appearance until 3.9 (Y no longer opens it). Checked in
  the builder VM with `tools/frontend-preview` (`tools/preview-steps/home.txt`,
  `home-empty.txt`). **Still to come:** the running game in the hero (Resume / Close game) and
  launching through owneetd (3.8); notices (3.11); the apps (phase 5: until then their tiles and
  "Open the Steam Store" show "Coming in a later version"); "How to add games" describes disk
  scanning, which arrives in phase 6.
