---
type: step
description: "Menu on a game (later on media) → 'Move to another disk': the disks with their free space, copy with progress and cancel, check, then…"
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.6"
status: done
legacy: "ROADMAP.md 6.6"
tags: [step, phase-6]
---
# 6.6 Moving games and media between disks *(added and approved for Wave 1, 2026-10-11)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **done**

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
- **Cancel asks first (owner, 2026-10-26):** Cancel or B during the copy pauses it and asks
  "Stop?" (the partial copy is removed and the game stays where it was): "Keep going" is selected
  by default and resumes, B on the question keeps going too, "Stop" cancels.
- **A failed check (owner, 2026-10-26):** a copy that is not the same as the original (or stops by
  itself: disk unplugged, full, read error) is removed; the original is never touched. One game:
  "The copy of {title} did not work", the check step crossed, "The original is still on {disk},
  untouched. {disk} may have a problem.", Close (selected by default) and Try again. Several games:
  the others go on, then "{ok} of {n} games copied" with Try again for the failed ones only. The
  cross uses the palette's colours (there is no error colour token). Demo key K: the next check fails.
- **Final demo approved by the owner (2026-10-26)** with the cancel question, the failed check and the
  switch that keeps the focus. The code after Danidepadawan's merge and [[step-6.5-automatic-disk-mounting]].
- **Code (owner, 2026-11-01)** on `feature/phase6`, after [[step-6.5-automatic-disk-mounting]]:
  - owneetd 0.22.0, package `moves`: `POST /v1/moves` `{games: [{dir, title}], to, remove}` (`to`:
    `internal`, the home's games folder, or a mounted disk's folder: its games folder, or a new
    `Games`; a name taken gets " (2)"), the copy with permissions and links and its progress in
    `moves.changed`, the check (every file's size and SHA-256, nothing more and nothing less), then
    the original removed only when asked; `pause`, `resume`, `stop` during the copy (stop: the
    partial copy removed). Failed or not passing: the copy removed, the original never touched, the
    others go on. Steam's storage settings: `open: "storage"` → `steam://settings/storage`.
  - owneet-frontend 0.31.0: `MoveSheet.qml` (Options → "Move to another disk", the disks, the
    confirmation with the switch, the steps, "Stop?", the failed check, Steam's games); a USB disk
    with games plugged in asks "Play from here / Copy to the console" (the notice stays when the
    question cannot come now); each cover says its disk when the console has several. Messages in
    the five languages; previews `move-game`, `move-game-fail` (`@movefail`), `plug-copy`.
  - Not as in the demo, for the owner: Steam's games carry no disk on their cover (the console does
    not know where Steam keeps them); `steam://settings/storage` to be checked with Steam on the test
    hardware.
- **Tested in the test VM (2026-11-01)** with the ISO of the branch and the test disk of 6.5 as a USB
  disk: a game made on its ext4 partition (40 MB of data, a program, a link) moved to the console
  through owneetd (the copy identical by SHA-256, the program still executable, the link kept, the
  original removed after the check); copied to the clean NTFS partition keeping the original (link
  and permissions there too); then moved from the screens (Options → Move to another disk, the
  disks with the read-only one off and why, the confirmation, the steps, the notice, the Library
  read again with each cover's disk). Found and fixed on the way: owneet-base's fix of 6.5 had no
  new version, so the ISO kept the old mounter (0.0.54). A game with Linux links cannot be copied
  to exFAT or FAT (they have no links): its copy fails its check safely, the original untouched.
  Steam's storage settings stay to be checked with Steam on the test hardware.
- **Owner (2026-11-01):** Steam's games without their disk on the cover: fine. "Open Steam's
  storage" (`steam://settings/storage`) to be tried as soon as possible on the test hardware.
  **Approved by the owner (2026-11-01): step 6.6 done.**
- **Steam's storage, checked (2026-11-05):** on FrankenPC "Open Steam's storage" showed Steam's home. In the test VM, with
  the owner signed in to Steam, `steam://settings/storage` opens the Storage page when Steam is ready. FrankenPC's log shows
  the address reaching Steam 1 s after its window, with its interface still starting, and no sign that Steam ran it. owneetd
  0.24.2 waited 5 s after the window for its settings pages; the VM has no gamescope, and the login was wiped from it after
  the test. **Owner's test on FrankenPC (2026-11-05):** Storage opens, after passing by Steam's home, with Steam's logo and a
  flicker on screen for some seconds. owneetd 0.24.3: Steam's window stays hidden 8 s more when the console starts it with an account,
  and the page goes 3 s before it shows. The button also plays the opening sound. **Waits for the owner's next test.**

- **The wait no longer depends on the computer (owner's question, 2026-11-05; owneetd 0.24.4):** the 8 s were fixed, so a slower computer would
  have shown the logo again. Steam's window now waits for the line Steam writes when its interface has started, the page goes then, and the
  window shows 3 s later, under "Preparing Steam…", with at most 30 s of waiting should the line never come
  ([[steam-loses-the-address-while-its-interface-starts]]). Only unit tests so far: gamescope runs only on real hardware. **Waits for the owner's test.**