---
type: step
description: "Menu on a game (later on media) → 'Move to another disk': the disks with their free space, copy with progress and cancel, check, then…"
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.6"
status: in-progress
legacy: "ROADMAP.md 6.6"
tags: [step, phase-6]
---
# 6.6 Moving games and media between disks *(added and approved for Wave 1, 2026-10-11)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **in-progress**

- **Deliverables:** Menu on a game (later on media) → "Move to another disk": the disks with their
  free space, copy with progress and cancel, check, then the original is deleted (never before).
  A USB stick with games plugged in: a notice "Play from here / Copy to the console". Steam
  games: a link to Steam's own storage settings (Steam moves them). Demo first.
- **Demo (2026-10-26):** `design/demos/6.6-moving-games.html`, on the approved games-on-disk demo:
  Menu → "Move to another disk" (the other disks with their free space; one without room or read
  only, as a Windows disk left dirty, is off and says why); the copy with its progress and Cancel
  (Cancel removes the partial copy and changes nothing); "Checking the copy"; only then "Removing
  the original"; the notice when done. A Steam game: "Steam moves its own games" with a button to
  Steam's storage settings. A USB disk with games plugged in: "Play from here / Copy to the
  console" (a copy keeps the originals). Waiting for the owner's approval. Branch
  `feature/step6_installer`; the code after Danidepadawan's merge and [[step-6.5-automatic-disk-mounting]].
