---
type: decision
description: "The user brings emulators and games; OwneetOS ships, downloads, links and names none, and makes the user's work small: a folder per console with an Emulators and a Games folder in it."
area: games
status: active
decided: 2026-11-25
updated: 2026-11-27
tags: [decision, games, legal]
---
# The user's own emulators

- **The user brings everything** (owner, 2026-11-25): emulators, system files, games. OwneetOS ships no emulator,
  downloads none, links none, names none, and has no list of known ones. It gives nothing that may put its authors in
  legal trouble; it starts a program of the user's with a file of the user's.
- **OwneetOS only makes it simple**, as far as possible.
- **Beside the user's own emulators, one emulation program comes with OwneetOS as an optional app** (owner, 2026-11-27,
  [[optional-apps]]): already installed, or at most unpacked from the ISO as the browser is; it joins the apps. Its name stays out
  of the vault. The way of this note stays as it is, as one more choice for the user. The user still brings the games and the
  system files.
- **Its details (owner, 2026-11-27):**
  - **When:** after the fixes of step 4.9's fourth test; which step builds it is still to be decided.
  - **Its name in the code:** what names it (the list of its packages) is kept out of git until the legal review, as the
    emulator cards are.
  - **Its logo and its menu's images:** included as they are; the console's own interface never shows them (guard [[legal]],
    edited by the owner on 2026-11-27).
  - **Its parts (one licence each):** a list for the owner to approve; only licences that allow commercial use and
    redistribution (guard [[legal]]). Later the user may add the missing parts, and that too must be plug and play.
  - **Its menu:** it opens as an app with its own interface, as Steam does; in a game, Guide as over Steam: a short press
    opens its menu (owneetd asks the program; the program never sees Guide), holding 1 s comes back to the console
    ([[guide-button]], [[controller-input-map]]; owner, 2026-11-27).
- **The console recognises some emulators and prepares them** (owner, 2026-11-26, "way B", after the first tests: "Owneet was made
  to be plug and play"): their controller, how they start, the install of a system file the user put there. Only where the user has
  no settings of their own; the others work as before. The user still brings emulators, system files and games; nothing is
  shipped or downloaded. Four to start with (chosen by the owner), more after their tests; the console's way stays as general as it can
  (common patterns, solutions already used elsewhere).
- **Which ones, only after the legal review** (owner, 2026-11-26): names may go into the public code after
  [[step-7.5-legal-review-before-the-public-launch]], when development is finished. Until then the code is general and what it
  knows of each emulator is kept out of git (`frontend/emulator-cards/*.json`, ignored); never in the vault, the website, the guide.
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
| 2026-11-26 | Way B: the console recognises some emulators and prepares them; their names in the code only after the legal review (owner). |
| 2026-11-27 | One emulation program comes with OwneetOS as an optional app, installed or unpacked from the ISO; the user's own emulators stay as one more choice (owner). |
| 2026-11-27 | Its images included (guard [[legal]] edited by the owner); its in-game menu on a short Guide press, as over Steam (owner). |
| 2026-11-27 | The emulation program after the fourth test's fixes; the list of its packages out of git until the legal review; a list of its parts to approve, the missing ones added later by the user, plug and play (owner). |
