---
type: decision
description: "The user brings emulators and games; OwneetOS ships, downloads, links and names none, and makes the user's work small: a folder per console with an Emulators and a Games folder in it."
area: games
status: active
decided: 2026-11-25
updated: 2026-11-25
tags: [decision, games, legal]
---
# The user's own emulators

- **The user brings everything** (owner, 2026-11-25): emulators, system files, games. OwneetOS ships no emulator (no RetroArch, no
  core), downloads none, links none, names none, and has no list of known ones. It gives nothing that may put its authors in
  legal trouble; it starts a program of the user's with a file of the user's.
- **OwneetOS only makes it simple**, as far as possible.
- **A folder per console**, named by the user, with two in it: the emulators and the games (`Emulators` / `Emulatori`, `Games` /
  `Giochi`, the console's languages, case does not matter). The user says this way which game goes with which emulator; the
  console does not guess.
- It replaces step 4.9's RetroArch with free cores ([[architecture-stack]], [[optional-apps]]).

Step: [[step-4.9-the-users-own-emulators]]. Research: [[retro-users-own-emulators]]. Guards: [[legal]], [[product-invariants]]. To the legal
review: [[step-7.5-legal-review-before-the-public-launch]].

## History

| Date | Decision |
|---|---|
| 2026-11-24 | The owner's wish: any emulator the user wants, in a folder, little work, no legal trouble for the authors. |
| 2026-11-25 | The user brings everything, RetroArch and free cores included: OwneetOS only simplifies the work (owner). |
