---
type: phase
wave: "[[wave-1]]"
legacy: "ROADMAP.md Phase 3"
tags: [phase]
---
# Phase 3 — Frontend (`owneet-frontend`, a Pegasus Frontend fork)

Up: [[wave-1]]

Legal requirements for the whole phase (checked 2026-10-08, [[legal-compliance]]):
Pegasus is GPL-3.0-or-later with additional terms: a significantly modified version must not use
"Pegasus Frontend", "Pegasus Launcher", "Pegasus" or Pegasus's logos as its title or logo (the fork
is `owneet-frontend`, the product is OwneetOS; copyright notices are kept and Pegasus is credited).
Pegasus's default theme (`pegasus-theme-grid`) is CC BY-NC-SA 4.0 and is never shipped. Pegasus's
Roboto fonts and button images are not used (own fonts and glyphs). Pegasus's online metadata
downloads (Steam store, GOG API, Play Store) are disabled: local data only.

Every screen step (home, library, settings, on-screen keyboard, notifications, and the pairing and
setup screens of phase 6) starts with an **interactive demo** approved by the owner before its
code is written ([[demo-before-code]]).

## Steps

| Status | Step |
|---|---|
| done | [[step-3.1-pegasus-study-and-fork\|3.1 Pegasus study and fork]] |
| done | [[step-3.2-build-and-package-the-frontend\|3.2 Build and package the frontend]] |
| done | [[step-3.3-theme-foundations\|3.3 Theme foundations]] |
| done | [[step-3.4-internationalisation\|3.4 Internationalisation]] |
| done | [[step-3.5-navigation-and-input-map\|3.5 Navigation and input map]] |
| done | [[step-3.6-home-screen\|3.6 Home screen]] |
| done | [[step-3.7-library-screen\|3.7 Library screen]] |
| done | [[step-3.8-frontend-daemon-bridge\|3.8 Frontend ↔ daemon bridge]] |
| done | [[step-3.9-settings\|3.9 Settings *(multi-prompt; demo approved 2026-10-09; approved 2026-10-10)*]] |
| done | [[step-3.10-on-screen-keyboard\|3.10 On-screen keyboard]] |
| done | [[step-3.11-notifications\|3.11 Notifications]] |
| done | [[step-3.12-interface-sounds\|3.12 Interface sounds]] |
| done | [[step-3.13-start-up-animation-and-power-options\|3.13 Start-up animation and power options *(owner's proposals, 2026-10-11; approved 2026-10-11)*]] |
