---
type: meta
description: "Everything left before the first release (v0.1.0): the owner's open reports, agreed work not built, put-off tests and the roadmap steps not done, at a glance and then in detail. Read it at the start of a session; update it in the same change as any report or fix."
tags: [wave, open-items]
---
# Wave 1 — open items

What separates OwneetOS from its first release: the owner's reports and agreed work that are not
done yet, so that none is lost (owner, 2026-11-09: "do not lose track of the others"), and the
roadmap steps left. **Every report of the owner goes here at once**, in the same change that
records it in its step note; an item leaves this list only when the owner has confirmed it (or
dropped it): it then moves, with its whole history and its number, to [[closed-items]] (owner,
2026-11-13). The table at the top is kept in step with the details below. Order of work: the
owner's.

## At a glance

### Waits for the owner: a test, a look or an approval

| # | What | Where it stands |
|---|---|---|
| 3ad | A game installed in place keeps its cover while it installs | Built (owneetd 0.25.29, owneet-frontend 0.38.28), on OWNEETLOG: to test |
| 3ad | Covers' titles on one line, scrolling when highlighted | Demo `3.7b-cover-title-scroll.html`: to approve |
| 3ab | Home's big card with text size XL: buttons and title scroll | Built (owneet-frontend 0.38.27): to look at on the TV |
| 3l | Games installed straight on their installer's disk (The Witcher 2 on the SATA disk) | Linux version installed there on 2026-11-13: to start it; the Windows one was installing |
| 3v | Steam's shader preparation at a game's first start (Batman: Arkham Knight) | To test |
| 3h | The copy's check and the original's removal with their percentages | Built: to test with a move |
| 3o | Free space shown at once after a move, an uninstall, a deletion | Built: to test |
| 3i | The details window: a long installer name shortened in the middle | Built: to look at |
| 3m | No notification sound during the start-up animation | Fixed in the test VM: to check if it happens again |
| 3x | Brightness slider removed from Settings → Display | Built: to look at |
| 3d | Less room on the console's disk (2026-11-10) | Explained by 3l (the install went there by design): to close? |
| 5 | The authors at the top of the console's Credits (3.9b) | Demo `3.9b-credits-authors.html`: to approve |

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|
| 3b | Wine's own programs (`C:\windows\…`) counted as the game's | Fix proposed |
| 3e | A copy to a slow SMR disk looks stuck | Diagnosis done: what the console does about such disks |
| 3j | A failed removal of the original after a move is only logged | To propose |
| 3t, 3p | Junk on the disks (old prefixes, logs, packages' cache, core dumps) | A phase or step to plan together; nothing cleaned meanwhile |
| 7 | Waking the console with the controller (step 6.10, `needs-decision`) | "Let's try": the test with the dongle to prepare |

### To build or prepare (assistant)

| # | What | Where it stands |
|---|---|---|
| 4 | "Shutting down" screen at once (7.6b) | Demo approved: code to write |
| 2 | "Resume with the pointer" in the library | Demo to make |
| 6 | Cover pictures from a disk (step 6.9) | Demo to make |
| 8 | "Preparing" with a percentage for Steam downloads | Nice to have: demo first |
| 3c | Removing the original on a USB disk Windows left read only | To check in the test VM |
| 9 | GitHub pages with every website update | Text to prepare; the owner publishes |

### Others

| # | What | Where it stands |
|---|---|---|
| 3 | Netflix / YouTube not silent behind the home screen | Danidepadawan, with the web apps |
| 10 | Cyberpunk 2077: Steam's question at launch shown at once | Test put off by the owner |
| 12 | "Playing for" over an hour on the home screen | Test put off by the owner |

### Roadmap steps left before the first release

| Step | What | Status |
|---|---|---|
| [[step-5.0.1-optional-gaming-apps\|5.0.1]] | Gaming programs as optional apps (Steam, later Epic, GOG, RetroArch) | todo |
| [[step-5.5-spotify\|5.5]] | Spotify | todo |
| [[step-5.6-local-videos-and-music\|5.6]] | Local videos and music | todo |
| [[step-5.7-apps-page\|5.7]] | Apps page | todo |
| [[step-6.9-cover-images-from-a-disk\|6.9]] | Cover images from a disk (item 6) | todo |
| [[step-6.10-waking-the-console-with-the-controller\|6.10]] | Waking the console with the controller (item 7) | needs-decision |
| [[step-7.3-user-guide\|7.3]] | User guide | in-progress |
| [[step-7.4-hardware-testing-and-v0.1.0\|7.4]] | Hardware testing and v0.1.0 | todo |
| [[step-7.5-legal-review-before-the-public-launch\|7.5]] | Legal review before the public launch | in-progress |
| [[step-7.8k-website-more-languages\|7.8k]] | Website in German, French and Spanish | in-progress |
| [[step-7.8l-website-download-link\|7.8l]] | Website download link (at the release) | todo |
| [[step-7.9-console-more-languages\|7.9]] | Console in German, French and Spanish | in-progress |
| [[step-7.10-donations-choice\|7.10]] | The choice on donations | needs-decision |
| [[step-7.11-sourceforge-project\|7.11]] | SourceForge project | todo |

Not before the release: [[step-1.7-xbox-wireless-dongle-xone|1.7]] (moved to Wave 2). The steps'
status is kept in their own notes; this table follows them.

## The owner's reports, in detail

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
   **Owner (2026-11-12): "obviously the game must be installable straight on the SATA disk"; it should have been there
   by default: a fault, priority, built right after the current test** (The Witcher 2 moved to the SATA disk). How the
   disk is chosen (the installer's own disk, a choice, …) to agree with him first ([[games-on-disk]]).
   **Owner (2026-11-12): the user chooses where the installer goes; the game is installed where its installer is.**
   Texts approved by the owner (2026-11-12): "La console lo installa su {disk} (circa {size})…", "{title} richiede circa
   {size} su {disk}… oppure sposta l’installer su un altro disco.", "Su {disk} c’è già un gioco con questo nome.",
   "{disk} è pieno: …", in the five languages. **Built:** owneetd 0.25.27 (a games folder at the top of a mounted disk as
   the destination; free space of the installer's disk; read-only disk refused; installs cut short on an unplugged disk
   kept; Go test), owneet-frontend 0.38.20 (in place on the installer's disk unless read only; known games' key files
   fixed on any writable disk; the four texts). **Test VM:** an installer in "Disk Install: Test" on the second disk
   ("GamesVM Games", ext4): the question said "installs it on GamesVM Games (about 31 MB)"; the folder renamed without
   ":", the game installed there (nothing in the home folder), listed as "Disk Install: Test" on GamesVM Games, installed;
   uninstalled there (only the installer left). Waits for the owner's test: The Witcher 2 installed straight on the SATA
   disk.
3m. **The notification's sound during the start-up animation** (owner, FrankenPC, 2026-11-10): a controller plugged in while
   the animation played made the `notify` sound, which the owner had asked never to happen ("the other sounds removed while
   the start-up sound plays"); hard to repeat, so tested by the assistant in the test VM. **Fixed** (owneet-frontend 0.38.12,
   checked in the test VM with the sound recorded). [[step-7.6-final-logo-and-brand]]
3o. **The console's free space not updated after a move** (owner, FrankenPC, 2026-11-10 evening): the Windows version of
   The Witcher 2 could not be installed (not enough room, with a warning); he moved the Linux version to the SATA disk
   (original removed); the console's disk still showed 38 GB free, as before the move; much later it showed 50 GB ("very
   late, not good"); then the install ended and the game started; moved to the SATA disk too, it started. **Cause** (logs
   `out/test-logs/frankenpc-20261110-203820` and the test VM): btrfs frees the room of removed files only at its next
   commit (up to 30 s), and the library read the disks only when shown again. **Fixed:** owneetd 0.25.20 syncs the
   original's disk after removing it, owneet-frontend 0.38.15 reads the disks again with the games; checked in the test
   VM; waits for the owner's test. [[free-space-shown-late-after-removing-files]],
   [[step-6.6-moving-games-and-media-between-disks]]
   **Owner (2026-11-11):** add the same fix to uninstalling, then he tests. **Built:** owneetd 0.25.21 syncs the disk
   after uninstalling, deleting a game and deleting an installer; checked in the test VM (the free space right at once).
3p. **No junk on the disks** (owner, 2026-11-11): from the next test, the whole content of both disks (the console's
   SSD and the 2 TB SATA disk) is checked: no junk files of any kind may stay (leftovers of old downloads, traces of
   deleted things no longer needed); the disks must not fill up needlessly over time. Needs a full listing of each disk
   in the test logs (owneet-testlog), then a check after every test. **Built:** owneet-base 0.0.61: once per start
   owneet-testlog writes `<log>.files/`, one compressed listing per disk (type, bytes, date, path of every file, folder
   and link; the console's disk subvolume by subvolume, its snapshots only measured), at the lowest priority; checked in
   the test VM (about 2 minutes for 200 000 entries). The check follows each new log. **First real log (2026-11-11,
   `out/test-logs/frankenpc-20261111-101928`):** cut: the console was switched off about 90 s after its start and the
   listing wrote straight to the stick (mounted "sync", very slow): only the system's listing whole, `/home` cut, the
   SATA disk missing. **Fixed:** owneet-base 0.0.62 makes each listing in memory and copies it whole (about 3 s in the
   test VM instead of 2 minutes), and writes `complete.txt` at the end. **First whole listing (2026-11-11 10:49,
   `frankenpc-20261111-104856`), found:** (a) the console's disk: 13 Windows prefixes (about 4.9 GB) and 3 DOS folders
   of games that are no longer on any disk seen (kept on uninstall by design, for the saves; also left by deleting a game
   or by a game on a disk not plugged in); (b) Proton's logs of the testers' option `owneet.debug.windows_log`, 1.3 GB
   (1.09 GB for one game), never removed; (c) the packages' cache: 150 files, 0.51 GB (43 versions of owneetd, 39 of
   owneet-frontend), growing with every update; (d) Steam's own, on the SATA disk: an unfinished download of Batman:
   Arkham Knight (208650, 24.1 GB, 2026-11-09) and its shader cache (2.9 GB), Cyberpunk 2077's (1091500, 0.5 GB); on the
   console's disk: an unfinished download of Steamworks Shared (228980, 0.24 GB), the folders and shader caches of six
   games no longer installed, Proton 5.13 (1.8 GB) and `ubuntu12_32/steam-runtime.old` (0.19 GB). Nothing deleted: the
   owner decides what to clean and how (Steam's content only through Steam, [[user-data]]). (e) (2026-11-11, 12:36 listing)
   systemd's core dumps: `tenfoot-launcher`'s crash left a 26.8 MB core in `/var/lib/systemd/coredump`; systemd keeps
   them up to two weeks and up to 10% of the disk, so a game that crashes often fills the disk with them.
   **Disk check (2026-11-12 12:48, whole listings, read on the stick):** Steam's unfinished downloads (`steamapps/
   downloading`): BioShock Infinite (8870) 23.3 GB, Lies of P (1627720) 18.5 GB, STAR WARS Jedi: Fallen Order (1172380)
   0.6 GB, small leftovers of Steamworks Shared (228980), Dishonored 2 (403640), ELDEN RING (1245620) and 31 `state_*.patch`
   files; Steam's shader caches 5.2 GB; 13 Windows prefixes 5.5 GB (3p (a)); packages' cache 0.58 GB (173 files);
   core dumps 0.11 GB; the journal 0.30 GB (bounded). The Witcher 2's folder on the SATA disk was the move in progress
   when the listing was made. **Owner:** those Steam downloads are wanted (games he is installing to test them).
3t. **Junk on the disks: a new phase or step** (owner, 2026-11-11, from 3p's findings (a)-(d)): the system cannot find
   out by itself whether a save is still needed; so either a simplified file manager (needed anyway in wave 2) or a
   simple, elegant solution thought out together. A critical point just found: it gets a phase (or step) of its own.
   **Owner:** first he ends today's tests, then this is planned with him (where it goes in the plan and how it is
   built). Nothing is cleaned meanwhile. [[open-items]] 3p
   **Owner (2026-11-12):** (a) a Windows game on an internal disk removed through the console with its installer takes
   its prefix with it, saves included; on external disks prefix and saves stay, for the file manager ([[disks]]); the
   prefix already left on the FrankenPC's disk by a game deleted before this rule is removed once, apart. (b) the
   testers' option `owneet.debug.windows_log=on` stays on for the tests; its old logs are part of this cleaning. Not built
   yet: it goes with this step's plan.
3v. **Steam's shader compiling shows the library with no notice** (owner, FrankenPC, 2026-11-12): after installing
   Batman: Arkham Knight (Steam), at its first start, while Proton compiled its shaders, the console went back to the
   library's page with nothing saying the game was still being prepared; the owner had to open Steam again to see that
   the process had not ended. Not looked at yet (no logs of that start read). [[step-4.2c-steam-without-its-interface]]
3x. **The brightness slider does nothing** (owner, 2026-11-12): Settings → Display's brightness does not change
   anything; **owner: remove it**, brightness comes back in Wave 2 ([[settings-screens]], [[wave-2]]). **Built**
   (owneet-frontend 0.38.21, 2026-11-12): the slider removed from Settings → Display; owneetd keeps
   `/v1/display/brightness` for Wave 2. Waits for the owner's look on the console.
3ab. **The home's big card with text size XL: buttons out of the card** (owner, FrankenPC 1366×768, 2026-11-13,
   screenshot 10:21): with a game running, "Riprendi", "Riprendi col puntatore", "Chiudi il gioco" go past the card's
   right edge. **Owner:** clip them and make them scroll; the same for the game's title. A change of look: demo first.
   **Demo** `design/demos/3.6c-hero-card-fit.html` (2026-11-13): only when the card's content does not fit (after its
   rows came closer, 3w d): the buttons are clipped at the card's edge with a soft edge where one is cut, and slide so
   that the selected one is whole; the title goes on one line, ends with "…" and scrolls (3.3b's rule) while a button
   of the card is selected. **Approved** (owner, 2026-11-13). **Built** (owneet-frontend 0.38.27, `HomePage.qml`; checked
   with `tools/frontend-preview`, `home-card-fit.txt`: text size XL, a running game with a long title; with text size M the
   card is as before). On OWNEETLOG with owneet-base 0.0.70 (the "witcher" search now enters every disk).
   **Owner (2026-11-13), 3aa:** he deletes both copies of The Witcher 2 on the SATA disk and copies them again from the
   USB disk with OWNEETLOG in; corrections are weighed after that test. Next tests: that copy, then Batman: Arkham
   Knight's first start (3v). The logs on the stick name games not allowed: read, not kept; the owner cleans the stick.
3ad. **The Windows version vanished from the library while it installs** (owner, FrankenPC, 2026-11-13 12:12; log
   `owneet-20261113-111127`): at 11:12 he deleted the three Witcher 2 folders on the SATA disk, at 11:12:36 copied both
   from the USB disk (two folders with ":"), at 12:04 asked to install both. owneetd renamed each folder to " - "
   (`game folder renamed`) and queued them; the Linux one was installed at 12:12:20, then the Windows installer started
   (`/VERYSILENT`, 21 GB). The games list is read again only on `installs.changed`: at 12:12:20 the Windows folder
   already had `.owneet-installing`, which the disk games provider never lists, so its card ("In attesa" until then)
   vanished. Not lost: the folder and its installer are there, and the card comes back when the install ends. Cause:
   the rule "a folder being installed is not listed, its installer shows the progress" ([[owneetd-api-installs]])
   dates from installs into the home folder; since 2026-11-12 games install in place, the installer is inside that
   folder, so nothing shows the progress. Also seen (screenshot 12:11:57): on the first card the "Locale" badge sits
   over the three-line title "The Witcher 2: Assassin of kings". The 3aa cause confirmed: a copy keeps ":", the
   install renames to " - ". Fix to agree with the owner.
   **Owner (2026-11-13):** (1) do it: the cover stays while the game is installed in place. **Built:** owneetd 0.25.29
   writes the installer's kind and the game's title in `.owneet-installing`; owneet-frontend 0.38.28 lists a folder
   being installed in place as its installer (title and kind from the mark), so its cover shows the progress
   ([[owneetd-api-installs]], [[frontend-disk-games]]); checked with `tools/frontend-preview`
   (`installs-in-place.txt`: a Windows installer, then a Linux one queued; when the first ended and the library was
   read again, the second kept its cover, "Installing · 66%"). On OWNEETLOG (checked identical); waits for the owner's test. (2) the cover's title
   **scrolls**: one line, "…" when it does not fit, scrolling while the cover is highlighted (3.3b's rule), so the
   badge never sits over it; a change of look: **demo** `design/demos/3.7b-cover-title-scroll.html` waits for the
   owner's approval.

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
