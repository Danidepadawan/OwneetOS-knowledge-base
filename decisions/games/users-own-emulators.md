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

- **The user brings everything** (owner, 2026-11-25): emulators, system files, games. OwneetOS ships no emulator,
  downloads none, links none, names none, and has no list of known ones. It gives nothing that may put its authors in
  legal trouble; it starts a program of the user's with a file of the user's.
- **OwneetOS only makes it simple**, as far as possible.
- **At the top of a disk, beside the games folder, a folder "Emulation"** (in the console's languages; owner, 2026-11-25): the
  consoles are only there, so no game's folder is looked into.
- **In it a folder per console**, named by the user, with two in it: the emulators and the games (`Emulators` / `Emulatori`, `Games` /
  `Giochi`, the console's languages, case does not matter). The user says this way which game goes with which emulator; the
  console does not guess.
- **Never named in anything that goes online** (owner, 2026-11-25): vault, code, comments, commit messages, website, guide: no
  emulator, and not even the consoles they are made for; invented names in examples and demos. In the conversation they may be named.
- **From 2026-11-25 no game and no emulator is named in the vault** (owner): tests and faults are described without them.
- It replaces step 4.9's first plan, an emulation program shipped with the console ([[architecture-stack]], [[optional-apps]]).

Step: [[step-4.9-the-users-own-emulators]]. Research: [[users-own-emulators-design]]. Guards: [[legal]], [[product-invariants]]. To the legal
review: [[step-7.5-legal-review-before-the-public-launch]].

## History

| Date | Decision |
|---|---|
| 2026-11-24 | The owner's wish: any emulator the user wants, in a folder, little work, no legal trouble for the authors. |
| 2026-11-25 | The user brings everything: OwneetOS only simplifies the work (owner). |
| 2026-11-25 | The consoles are in a folder "Emulation" beside the games folder (the owner's idea). |
| 2026-11-25 | No emulator and no console named in anything that goes online (owner): the research of 2026-11-24 taken out of the vault. |
| 2026-11-25 | From now on no game and no emulator is named in the vault (owner). |
| 2026-11-25 | Demo 4.9c approved; corrections never change what starts today; the pointer's rule and the closing stay (owner). |
