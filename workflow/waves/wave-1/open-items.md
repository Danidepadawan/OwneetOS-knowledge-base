---
type: meta
description: "Every open item of Wave 1 in one list: the owner's reports not solved yet, decided work not built, postponed tests. Read it at the start of a session; update it in the same change as any report or fix."
tags: [wave, open-items]
---
# Wave 1 — open items

The owner's reports and agreed work that are not done yet, so that none is lost (owner, 2026-11-09:
"do not lose track of the others"). **Every report of the owner goes here at once**, in the same
change that records it in its step note; an item leaves this list only when the owner has confirmed
it (or dropped it), and its step note says so. Order of work: the owner's.

## The owner's reports, not solved yet

2. **"Resume with the pointer" in the library**: missing there. Demo first.
   [[step-6.8-games-on-disk-delete-and-progress]]
3. **Netflix / YouTube not silent behind the home screen**: left to Danidepadawan with the web apps
   (owner, 2026-11-09). [[step-4.5-windows-games-proton]]

3b. **Wine's own programs followed as the game's** (found in the owner's test log, 2026-11-09 21:50): the
   home screen at the game's end waited for `C:\windows\system32\explorer.exe` too, because it owns a window;
   there it ended before the game, but it could outlive it until Wine closes. Fix proposed: never count a
   program under `C:\windows` as the game's, even with a window. [[step-4.5-windows-games-proton]]

3c. **Removing the originals of single games, the read-only case** (6.6c, confirmed by the owner on
   2026-11-10: the original removed after a copy, with no error; the choice of
   games, item 1 of 2026-11-09, confirmed too): left, a USB disk that Windows left read only, to check
   in the test VM (the owner has no Windows disk). [[step-6.6-moving-games-and-media-between-disks]]

3d. **The console's disk has less room** (owner, 2026-11-10): about 57 GB free, about 80 the day before.
   Not explained by the logs (the report did not measure folders; Steam's Cyberpunk download is at
   1.3 GB; a stick update is about 216 MB). The owner installed The Witcher 2 the day before, perhaps on
   this disk by mistake. The test report measures the console's disk from owneet-base 0.0.60 (testers
   only, owner's condition): to read in the next logs. [[open-items]]
3e. **A copy stuck at 29 %** (owner, 2026-11-10 11:01-11:13): a copy from the USB disk "GAMES-320" to
   "2TB HDD SATA" stayed at 29 % and the owner stopped it (the partial copy was
   removed). **Diagnosis (no change made, owner's request):** the copy was never paused nor blocked
   (Stop worked in 130 ms); the USB disk read about 12 MB/s until 11:07:15, then stayed almost idle
   (0.2-2 s busy every 12 s, about 0.5 MB/s): the copy waited on its writes. The 2 TB disk is a
   Seagate ST2000DM008, a drive-managed SMR model: after a few GB written at once it slows down to
   well under 1 MB/s while it rewrites its tracks (about 3.7 GB had been written). The first guess (the
   wait at each file's end) is ruled out by the data. To confirm with the next logs (each disk's
   writes, the memory waiting to be written, /v1/moves: owneet-base 0.0.60); then what the console
   does about such disks is the owner's choice. [[step-6.6-moving-games-and-media-between-disks]]

3h. **"Checking the copy" says nothing while it works** (owner, 2026-11-10, moving The Witcher 2): it looked stuck, then
   ended. The check reads the original and the copy in full (SHA-256) with the percentage fixed at 100: as long as the
   copy, with no sign of life. Owner (2026-11-10): a demo first; **demo 6.6d** (`design/demos/6.6d-check-progress.html`:
   the check's own percentage and bar, as the copy) waits for the owner's approval. **Owner's corrections (2026-11-10):**
   (a) a progress for the removal of the original too; (b) when the original is kept, no step for it in the window;
   (c) in the demo, Cancel did not cancel the copy (perhaps only the demo's fault: to check the same in the code).
   **Demo corrected (2026-11-10):** (a) and (b) done; (c) the demo drew its window again every 160 ms, so a click fell
   on a button already replaced: now only the numbers change (the interface's Cancel is never rebuilt during the copy).
   **Owner (2026-11-10):** Cancel stops the copy of every chosen game: the "Stop?" window must let the user choose
   to stop the whole copy or only the current game's. Demo first. **In demo 6.6d:** with games left after the current
   one, "Keep going" (selected), "Stop this game" (its partial copy removed, the next games go on), "Stop all" (the
   games already copied stay); the last or a single game keeps one "Stop"; the final notice counts the games copied.
   **Approved by the owner (2026-11-10). Built:** owneetd 0.25.17 (the check's percentage counts the bytes read of
   both copies, the removal's the files removed; `POST /v1/moves/skip` stops only the current game's copy, `skipped` in
   the status; Go tests), owneet-frontend 0.38.11 (the window as in the demo; texts in the five languages); checked in
   the interface preview (`move-stop-one.txt`, `move-game.txt`). **Owner's test (2026-11-10, log 16:21):** "Stop this game"
   done (16:24:34: its partial copy removed, the next game went on) and "Stop" on the last game; the move with the check's and
   the removal's percentages not tried yet: the owner tests it after the chosen file and the prefix's copy are built (owner: build first, then test).
   [[step-6.6-moving-games-and-media-between-disks]]
3i. **The details window's text out of the window** (owner, 2026-11-10 12:32, "the installer's description"): most likely
   the installer's long file name in the facts (The Witcher 2): the facts' grid has no width limit and the window does not
   widen for it. Owner (2026-11-10): shortened in the middle with "…". **Built** (owneet-frontend 0.38.10, checked in
   the preview with a long installer name); waits for the owner's test. [[step-4.6-installers]]
3j. **The Witcher 2 after its move** (owner, 2026-11-10): it closed at once; the copy on the console's disk "was not
   removed" and does not start; "only the installer moved". Found in the code: a moved Windows game gets a new, empty prefix
   (the prefix is named after the game's folder: saves, settings and the installer's registry stay behind, and the old
   prefix keeps its room on the console's disk); a failed removal of the original is only logged, and the game counts as
   moved. **From the logs** (`out/test-logs/frankenpc-20261110-115130`): the move of 12:21 worked with no error and
   the original on the console's disk was removed; the copy went to "…Enhanced Edition (2)", because the installer's
   folder of the same name is already on that disk; the game that closed at 12:33 is that copy: its `Launcher.exe` did
   not load (`MSVCP100.dll` missing, c0000135), which the installer had put in the original prefix. The reinstall of
   12:42-12:57 went to the console's disk, into the original prefix. **Fixed** (owner, 2026-11-10: the prefix goes with
   the game): owneetd 0.25.16 renames the game's own folders (Windows prefix, DOS data) to the new place and points the
   install's link there; Go tests; waits for the owner's test. Left: a failed removal of the original is only logged
   (did not happen here); to propose to the owner. **Owner (2026-11-10, after the fix's stick):** "neither copy
   started" (the one moved to the 2 TB disk and the one reinstalled on the console's disk), so he uninstalled both;
   "I moved everything, and the tests failed"; he downloads The Witcher 2 again, both its Windows and its Linux
   version, to test both. The logs of that start to read. **Owner (2026-11-10, log 16:21):** both downloads on the disk, their
   names differ now ("The Witcher 2: Assassin of kings", the Linux `.sh`; "The Witcher 2: Win", the Windows installer); in the
   test before, with the same name, the second install got " (2)". The owner installs and moves them only after the chosen file and the prefix's copy
   are built. [[step-6.6-moving-games-and-media-between-disks]]
3l. **Installing The Witcher 2 "on the SATA disk"** (owner, 2026-11-10): an installer on any disk installs on the console's
   own disk (by design, [[step-4.6-installers]]), so the install of 2026-11-09 went there by design, not by mistake (3d);
   told the owner on 2026-11-10. Installing straight on another disk would be a new decision, if he wants one.
3m. **The notification's sound during the start-up animation** (owner, FrankenPC, 2026-11-10): a controller plugged in while
   the animation played made the `notify` sound, which the owner had asked never to happen ("the other sounds removed while
   the start-up sound plays"); hard to repeat, so tested by the assistant in the test VM. **Fixed** (owneet-frontend 0.38.12,
   checked in the test VM with the sound recorded). [[step-7.6-final-logo-and-brand]]
3n. **Home does nothing during a copy** (owner, 2026-11-10): while games are copied the window stays on screen and Guide
   ("Home") does nothing, so the user can do nothing else until the copy ends; the owner understands blocking some actions,
   not being stuck. The copy runs in owneetd, so it can go on behind the interface. What the user sees and may do meanwhile
   is the owner's choice; demo first. **Owner (2026-11-10):** agreed with the proposal (Home closes the window, the copy goes
   on, a sign shows it, only a second copy and starting the games being copied are blocked): **demo 6.6e**
   (`design/demos/6.6e-copy-behind.html`) waits for his approval. In it Guide is Home from every window of the console (an
   open window closes), as its prompt "Home" already says; a copy that fails with its window closed says it in a notice, on
   its cover and in the top bar, and A on the cover shows Close / Try again. [[step-6.6-moving-games-and-media-between-disks]]

## Decided, not built yet

4. **"Shutting down" screen at once** (7.6b): demo `design/demos/7.6b-shutting-down.html` approved;
   the code is missing. [[boot-experience]]
5. **The authors at the top of the console's Credits** (3.9b): demo
   `design/demos/3.9b-credits-authors.html` waits for the owner's approval. [[step-3.9-settings]]
6. **Cover pictures from a disk** (6.9): demo to do. [[step-6.9-cover-images-from-a-disk]]
7. **Waking the console with Guide** (6.10): the owner said "let's try"; the test with the dongle to
   prepare. [[step-6.10-waking-the-console-with-the-controller]]
8. **"Preparing" with a percentage for Steam downloads**: nice to have in Wave 1 if easy; demo first.
   [[step-4.2c-steam-without-its-interface]]
9. **GitHub pages with every website update**: README, the repositories' description and topics; the
   text is prepared here, the owner publishes it. [[website]]

## Tests the owner put off

10. Cyberpunk 2077: Steam's question at launch shown at once. [[step-4.2c-steam-without-its-interface]]
12. "Playing for" over an hour on the home screen ("1 h 5 min", "2 h"). [[step-4.2c-steam-without-its-interface]]
