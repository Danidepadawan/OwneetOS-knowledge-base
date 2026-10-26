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
  console" (a copy keeps the originals). Branch
  `feature/step6_installer`; the code after Danidepadawan's merge and [[step-6.5-automatic-disk-mounting]].
- **Second round (owner, 2026-10-26):** the check and the removal of the original made visible and
  a choice: after the disk, a confirmation with the switch "Remove the original after the copy is
  checked" (on by default; off, a copy), then the steps listed and ticked one by one (copy with
  Cancel, check, removal only after). "Copy to the console" asks which disk, the one with the most
  room first, never forced onto the system SSD (the FrankenPC: a 96 GB SSD and a 2 TB HDD). Each
  game's cover says its disk when the console has more than one (also in Details).
- **Demo approved by the owner (2026-10-26)** once the steps no longer stopped at the end (a fault
  of the demo) and B cancels during the copy (the check and the removal are never stopped half
  way). The code after Danidepadawan's merge and [[step-6.5-automatic-disk-mounting]].
