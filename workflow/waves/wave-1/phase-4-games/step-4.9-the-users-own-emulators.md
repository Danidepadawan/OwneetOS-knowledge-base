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

- **Built (2026-11-25): owneet-frontend 0.41.0, owneetd 0.27.0.** `owneet::Emulators` (the folders, what is an emulator, what is a game, the
  choices in `emulators.json`), the disk-games provider (extras `emu.*`), the windows in `theme.qml` (`emu*`), `owneet-emulator-run`
  (unpacks an AppImage or opens an archive once, in `~/.local/share/owneet/emulators/`), `POST /v1/pointer` with `"windows": "all"`.
  How: [[users-own-emulators-design]].
- **Checked:** unit test `test_Emulators` (the package's 25 tests pass), `tools/lint`, `owneet-emulator-run` in the builder VM with invented
  emulators (options with spaces and signs, no exec bit, archives, changed ones, errors, what is removed and what is kept), the
  previews `emulators.txt`, `emulators-add.txt`, `emulators-xl.txt` (German, XL). On OWNEETLOG.
- **Not in it:** Windows programs, uninstalling such a game from its options (the file manager deletes).
- **The owner (2026-11-25):** the pushed history with names stays as it is; a text for the pointer's card; moving a console between
  disks, absolutely; a folder "Emulation" beside the games folder, if better: **it is** (no game's folder looked into, no game of
  the PC's taken for a console, clear to the user).
- **Built (2026-11-25): owneet-frontend 0.41.1, owneetd 0.27.1:** `Emulation` / `Emulazione` / `Émulation` / `Emulación` at the top of a
  disk, the consoles only in it; the file manager shows it; the pointer's card says "It stays on until you close the emulator".
- **Moving a console (demo 4.9b, approved by the owner 2026-11-25):** `design/demos/4.9b-move-a-console.html`: the windows of moving games, the whole console
  (never one game alone); a disk with a console of that name already is off; a USB disk's consoles in "Which ones to copy?".
- **Built (2026-11-25): owneet-frontend 0.42.0, owneetd 0.28.0:** owneetd's moves take a console's folder (`internal/moves/consoles.go`): to the
  other disk's "Emulation" (made with the name it had), never over one of the same name in any case (409 `moves.name_taken`); what
  was chosen (`emulators.json`, its paths too) and what was unpacked for its emulators follow a move; a copy gets a copy of what
  its archives left. A disk unplugged takes its consoles' games out of the library (it did not). Checked: four Go tests, the
  previews `emulators-move.txt`, `emulators-move-xl.txt`. Not tried on real disks.
- **To do:** the FrankenPC with real emulators (named in the conversation only), then the owner's approval of the step.
