---
type: step
description: "The owner's final sounds (interface-sounds-spec: names, format, lengths, licences) replace the placeholders of `frontend/sounds/`;…"
phase: "[[phase-7-updates-and-first-release]]"
step: "7.7"
status: done
legacy: "ROADMAP.md 7.7"
tags: [step, phase-7]
---
# 7.7 Final interface sounds *(Owner delivery)*

Up: [[phase-7-updates-and-first-release]] · Status: **done**

- **Deliverables:** the owner's final sounds ([[interface-sounds-spec]]: names, format, lengths, licences)
  replace the placeholders of `frontend/sounds/`; `CREDITS.md` updated with their authors and
  licences. After the legal review (7.5), before the public launch.
- **Delivered by the owner (2026-11-03):** all ten sounds in `frontend/sounds/` (WAV 16-bit, 44.1
  kHz, stereo; the package makes them 48 kHz mono and removes the silence around them).
  `notify-error` dropped (owner, [[interface-sounds]]): the notifications at the top right play
  `notify`, the "No internet" window `error`. Kenney's placeholders, their licence file,
  `tools/sounds/make-placeholders` and their credit removed; `CREDITS.md` and
  `frontend/sounds/SOURCES.md` list only the owner's sounds; owneet-frontend 0.34.0 (code commit
  bf1f93c on `feature/phase7`); the demos'
  `sounds.js` made again (the demos that played `notify-error` play `notify` or `error`).
  Waiting for the owner to hear them on the console.
- **Approved by the owner (2026-11-05)** after hearing them on FrankenPC.
