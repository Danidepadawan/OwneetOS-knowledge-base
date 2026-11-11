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
  ([[steam-loses-the-address-while-its-interface-starts]]). Only unit tests so far: gamescope runs only on real hardware. **Owner's test on FrankenPC (2026-11-05):** Steam's start no longer shows; a flicker still does, and the owner keeps it, the notice before Steam covers it; about 31 s from the press (click 15:33:22, window 15:33:53), accepted; the sound back on the home passes. B from Steam's home goes to an endless loading: closed for Wave 1 by the owner, back in [[wave-2]] ([[steam-loading-for-ever-after-b]]).- **Reported by the owner (2026-11-08), open, recorded late (2026-11-09: it had been left out):** when a disk with games is
  plugged in, the question "Play from here / Copy to the console" gives no way to choose one game or all of them; "it must be
  looked at now". Needs a demo first (a change to the approved screen); waits for the owner's turn in the order of work.
- **Demo 6.6b (2026-11-09, code `22f449a`):** `design/demos/6.6b-choose-games-to-copy.html`, on the approved 6.6 demo. After
  "Copy to the console", a disk with more than one game asks "Which games to copy?": a switch per game with its size and
  "All games" above, all on at first; A switches the selected row; the button copies the games that are on ("Copy 3 games
  (5.85 GB)", "Copy Lantern Keep (1.2 GB)"), is dimmed with "Choose at least one game" when none is, and is selected at first
  (one A copies them all, as before); then the disk; B goes back one window. A disk with one game skips the question.
  Demo address: `#lang=it&open=plug` (the question at once). Waits for the owner's approval.
- **Demo 6.6b approved by the owner (2026-11-09); built (owneet-frontend 0.38.8, code `9b131b6`):** `MoveSheet.qml` asks
  "Which games to copy?" after "Copy to the console" when the disk has more than one game: `SettingRow` switches (new
  `aside`: the size after the title, on its line, as in the demo), "All games" above, all on at first; the button (Dialog's
  new `dim`: dimmed but selectable, A gives the edge sound when no game is on) is selected first; many games scroll inside
  the window (as VersionsSheet), the selection kept in sight; B goes back one window, the choice kept. Messages in the five
  languages. **Also fixed, to match the approved demo 6.6:** after the disk, the copy of a plugged-in disk's games starts at
  once with the originals kept; the code opened the one-game "Move … to …" confirmation (first game's name only, with the
  remove switch). Checked in the interface preview (`tools/preview-steps/plug-copy.txt`, a disk with 12 games): switches,
  "All games", none chosen, scrolling, the disk's title for 10 games, B back with the choice kept, two games copied
  ("Copying Ashen Gate (1 of 2)", "2 games copied to Internal disk"). Waits for the owner's test on FrankenPC.
- **Asked by the owner (2026-11-10), open:** "add the feature to remove single games from the original" (the copy from a
  plugged-in disk); its exact meaning is being asked; demo first ([[open-items]] 3c).
- **The owner's choice (2026-11-10): game by game.** Demo 6.6c (`design/demos/6.6c-move-single-games.html`, code
  `bc627ba`), on the approved 6.6b: each row of "Which games to copy?" has two switches under two headings, "Copy" and
  "Remove the original" (off at first; only for a copied game, so switching "Copy" off switches it off too; "All games"
  switches a whole column); left / right move between them. A note under the list says what happens to the originals ("The
  originals stay on the USB disk." / "After the check, the original of Cayne is removed…" / "…the originals of 2 games…");
  the disk window says it again; in the steps each game says "Remove the original from …" or "Keep the original on …". An
  original is removed only after its copy passed the check ([[user-data]]). A read-only USB disk (Windows not shut down
  completely) keeps its originals: the second column is off, the note says why. The window is 720 px wide (620 in 6.6b) to
  hold the two headings. Building it needs owneetd's moves to take "remove" game by game. Waits for the owner's approval.
- **Demo 6.6c approved by the owner (2026-11-10); built (owneetd 0.25.15, owneet-frontend 0.38.9, code `b281b0d`):**
  `MoveSheet.qml` draws "Which games to copy?" as a table: headings "Copy" and "Remove the original", then a row per game
  (and "All games") with two `SwitchCell`s (new: SettingRow's switch on its own, dimmed and skipped when not available);
  `originalsNote()` under the list and in the disk window; the steps and the title follow the game being copied; the last
  notice says which originals were removed. A read-only disk keeps its originals: "Read only: Windows was not shut down
  completely. …" when that is the reason, "Read only: the originals stay on the USB disk." otherwise. owneetd: each game of
  `POST /v1/moves` carries its own `remove` (the request's `remove` still means all of them); `Status.remove` is the current
  game's. The demo's last notice was corrected to say what happened to the originals (it said "they stay" in every case).
  Checked: Go tests (game by game: only the asked original removed, after its check); the interface preview (the pretend
  disk is read only: the column off, the right reason); **the test VM** with a writable FAT stick holding Alpha and Beta,
  unplugged and plugged in again: "Copy" both, "Remove the original" on Beta, Internal disk: both copied, Beta's original
  removed from the stick, Alpha's kept, notice "2 games copied to Internal disk / Copy checked, the original of Beta removed
  from the USB disk". A disk with one game skips the choice (as approved); its original can go with Menu → Move to another
  disk. Waits for the owner's test on FrankenPC.
- **Owner's test of 6.6c (FrankenPC, 2026-11-10; logs `out/test-logs/frankenpc-20261110-105950`):** the choice of games and
  the switches work. A copy from "GAMES-320" (USB, ext4) to "2TB HDD SATA" started at 11:01:06;
  it stayed at 29 % and the owner stopped it at 11:13:18 (the partial copy removed). No disk
  error in the journal (only correctable PCIe messages). Open ([[open-items]] 3e). The read-only case is left to the test
  VM: the owner has no Windows disk.
- **Owner (2026-11-10):** an original was removed from the USB disk after its copy, with no error: 6.6c
  confirmed (and the choice of games, 6.6b). **Diagnosis of the copy at 29 %** (no change, owner's request), from the
  report's snapshots (sectors read and ms reading per disk, every 12 s): no pause, no blocked task, Stop in 130 ms; the
  source USB disk read about 12 MB/s until 11:07:15, then stayed almost idle (about 0.5 MB/s while busy, busy 0.2-2 s
  every 12 s): the copy waited on its writes. The target "2TB HDD SATA" is a Seagate ST2000DM008 (boot log), a
  drive-managed SMR disk, which slows down to well under 1 MB/s after a few GB written at once (about 3.7 GB here). The
  first guess (each file's sync at its end) is ruled out. To confirm: owneet-base 0.0.60's report has each disk's writes,
  the memory waiting to be written and /v1/moves.
- **Owner's test (FrankenPC, 2026-11-10, around 12:30; logs not read yet: OWNEETLOG still in use):** a copy to
  "2TB HDD SATA" finished; The Witcher 2 moved from the console's disk to it. Reports ([[open-items]] 3h-3j, 3l): (1) "Checking
  the copy" shows nothing that says whether it works or is stuck; (2) after the move The Witcher 2 closed at once, and the
  copy on the console's disk "was not removed" and does not start; only the installer seems to have moved. **Found in the code (no change yet):** the check reads the original and the copy in full
  (SHA-256 of every file) with the percentage fixed at 100, so it lasts about as long as the copy; a removal of the
  original that fails is only logged, and the game still counts as moved; a Windows game's prefix (its saves, settings and
  what its installer wrote) is named after the game's folder, so a moved game gets a new, empty prefix and the old one stays
  on the console's disk.
- **Owner (2026-11-10):** the prefix goes with the game; "Checking the copy" gets a progress, demo first; a long value in the
  details window is shortened in the middle. **The logs** (`out/test-logs/frankenpc-20261110-115130`; the report had no
  new diagnostics yet: owneet-base 0.0.60 was installed during that start): The Witcher 2's move (12:21) worked and removed
  the original; the copy is "…(2)" on the 2 TB disk (the installer's folder has the plain name there); it closed at once
  because its new, empty prefix lacks what the installer wrote (`MSVCP100.dll`). **Built:** owneetd 0.25.16 (a moved game's prefix and DOS data renamed to its new
  place, its install's link pointed there; never over a folder already there; Go tests, the name checked against the
  real prefix names in the log); owneet-frontend 0.38.10 (details window, [[step-4.6-installers]]); demo
  `design/demos/6.6d-check-progress.html` waits for approval. Open: [[open-items]] 3h-3j.
- **Demo 6.6d approved by the owner (2026-11-10)**, after his corrections: the check and the removal of the original with
  their own percentage and bar; no step for a kept original; copying several games, "Stop?" offers "Stop this game" or
  "Stop all" while games are left after the current one. **Built:** owneetd 0.25.17 (`POST /v1/moves/skip`, `skipped` in
  `GET /v1/moves`; the percentage of the check counts the bytes read of both copies, the removal's the files removed),
  owneet-frontend 0.38.11; Go tests; checked in the interface preview. Waits for the owner's test.
- **Owner's test of 6.6d (FrankenPC, 2026-11-10, log 16:21):** "Stop this game" works (its partial copy removed, the next
  game went on). **Reported:** during a copy Guide ("Home") does nothing and the window stays: the user cannot do anything
  else until it ends ([[open-items]] 3n, the owner's choice, demo first). **Owner:** the chosen file and the prefix's copy are built first, then he tests moving and copying The Witcher 2 (Windows and Linux).
- **Demo 6.6e** (`design/demos/6.6e-copy-behind.html`, 2026-11-10, after the owner agreed with the proposal): Guide (Home)
  closes the copy's window and shows the home screen, the copy goes on; Guide is Home from every window; the top bar shows the
  copy (step, percentage, "2 of 3"), the covers of its games their state ("Copying · 45%", "Waiting to be copied"); A on one
  shows the window again ("Show the copy"), so those games are never started meanwhile; one copy at a time ("A copy is already
  running"); its end, or a failure, with the window closed in a notice; a failed game's cover and the top bar say it, A on the
  cover shows Close / Try again. Waits for the owner's approval.
- **Demo 6.6e approved by the owner (2026-11-10)** with a correction: Home closes only the copy's window (Guide keeps its
  meaning elsewhere: with an app open it goes back to it); a shutdown or restart during a copy asks first. **Built:** owneetd
  0.25.18: Guide on the home screen with nothing to go back to sends `home.requested`; `Abort` stops the copy and its check
  before a shutdown or restart (`/v1/power`, up to 60 s) and when owneetd stops (20 s), removing the partial copy, the original
  untouched (an original whose copy passed its check is removed to the end first); Go tests. owneet-frontend 0.38.14: the
  window closes on Home, the copy shown in the top bar and on its games' covers ("Show the copy" on A), one copy at a time
  (a disk plugged in meanwhile gives its notice), its end or failure in a notice, the power windows say the copy stops; texts
  in the five languages. Checked in the interface previews (`move-behind.txt`, `move-behind-fail.txt`) and in the test VM
  (shutdown during the check of a 3 GB copy: the partial copy gone, the original's SHA-256 the same). Waits for the owner's
  test.
- **The chosen file and the copy of the own folders built (2026-11-10):** owneetd 0.25.19. After a game's
  copy passed its check, the file chosen to start it (owneet-frontend's `disk-games.json`) is given to the new folder, and a
  moved game's old entry goes; a copy (the original kept) gets a copy of the original's own folders (Windows prefix, DOS
  data), which, like the check, only a shutdown stops; when the games go to the console's disk, the room needed counts
  those folders too. **Confirmed by the owner (2026-11-10):** when the own folders cannot be copied, the game's copy
  counts as "did not work" (removed with what was copied, the original untouched), since without its prefix a Windows game
  may not start (3j). Go tests; checked in the test VM: a game with two files to start and "Start B.exe" chosen, copied to
  the console's disk and moved back to a disk: the choice followed both times, the prefix was copied (files and links the
  same) and then moved, and the interface, reading the games again, started both from `Start B.exe` without asking. Waits
  for the owner's test (The Witcher 2, Windows and Linux).
- **Owner's test of 6.6e and the chosen file (FrankenPC, 2026-11-10 evening, logs `out/test-logs/frankenpc-20261110-203820`):** all
  works (Home on the copy, top bar, covers, A, the shutdown's question; The Witcher 2 Windows installed, moved to the SATA
  disk, started; a copy keeping the original starts with the same file); the Linux version's start is tested on
  2026-11-11. **Reported:** after a move the console's free space showed the new value much later ([[open-items]] 3o).
  **Fixed:** owneetd 0.25.20 (syncfs of the original's disk after its removal), owneet-frontend 0.38.15 (the library reads
  the disks again with the games); Go tests, interface preview, test VM
  ([[free-space-shown-late-after-removing-files]]). Waits for the owner's test.
- **Owner (2026-11-11):** the same fix for uninstalling. **Built:** owneetd 0.25.21 (`syncdisk` after uninstalling,
  deleting a game, deleting an installer), checked in the test VM. The owner also asked that the whole content of both
  disks be checked for junk after every test ([[open-items]] 3p): owneet-base 0.0.61 lists every disk in the test logs.
