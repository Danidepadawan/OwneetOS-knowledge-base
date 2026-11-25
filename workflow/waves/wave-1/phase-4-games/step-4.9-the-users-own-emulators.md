---
type: step
description: "The user's own emulators: a folder per console with the user's emulators and games in it, the games in the library; OwneetOS ships, downloads, links and names no emulator and makes the user's work small. Before the legal review."
phase: "[[phase-4-games]]"
step: "4.9"
status: in-progress
tags: [step, phase-4]
---
# 4.9 The user's own emulators *(added 2026-11-21, changed 2026-11-25)*

Up: [[phase-4-games]] · Status: **in-progress**

- **Origin:** moved from Wave 2 (item 11b of [[wave-2]]) by the owner on 2026-11-21: the idea of "ownership" has to come
  across in the first release. Then an emulation program shipped with the console was planned.
- **When (owner):** at the end of the games' tests, before the legal review ([[step-7.5-legal-review-before-the-public-launch]]),
  so that the review covers it. Before [[step-5.0.1-optional-gaming-apps]] (owner, 2026-11-24).
- **Changed by the owner (2026-11-25): "the user brings everything, we only make their work as simple as possible".** Nothing shipped,
  downloaded, linked or named. Decision: [[users-own-emulators]]; how: [[users-own-emulators-design]].
- **Never named (owner, 2026-11-25):** no emulator and no console in anything that goes online (vault, code, comments, commits,
  website, guide); only in the conversation.
- **The user's own discs** (the owner's idea; GitHub's issue 2, 2026-11-22): what an emulator of the user's does with a disc is its own;
  the console does nothing.

## Demo (approved by the owner, 2026-11-25)

`design/demos/4.9-users-own-emulators.html` (invented names).

- **The pointer's rule approved (owner, 2026-11-25):** on by itself with "Open the emulator", for every window of it until it ends
  ([[controller-input-map]]).
- **The owner's question (2026-11-25):** do the options need other characters (space, semicolon)? **Yes:** the demo has now the
  console's whole keyboard (every ASCII sign, a space with Y); "one or more options", a space between them, double quotes for a name with
  spaces. **Approved.**

## Building

To do.
