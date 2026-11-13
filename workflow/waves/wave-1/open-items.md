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
3n. **Home does nothing during a copy** (owner, 2026-11-10): while games are copied the window stays on screen and Guide
   ("Home") does nothing, so the user can do nothing else until the copy ends; the owner understands blocking some actions,
   not being stuck. The copy runs in owneetd, so it can go on behind the interface. What the user sees and may do meanwhile
   is the owner's choice; demo first. **Owner (2026-11-10):** agreed with the proposal (Home closes the window, the copy goes
   on, a sign shows it, only a second copy and starting the games being copied are blocked): **demo 6.6e**
   (`design/demos/6.6e-copy-behind.html`). **Approved (2026-11-10) with a correction:** Home only on the copy's window,
   not on every window ("it would break the logic of the open apps"); and a shutdown or restart during a copy asks first.
   **Built:** owneetd 0.25.18 (`home.requested` when Guide is pressed on the home screen with nothing to go back to; before
   a shutdown or restart, and when owneetd stops, the copy and its check stop and the partial copy is removed), owneet-frontend
   0.38.14 (the window closes on Home, the top bar and the covers, A shows it again, one copy at a time, the notices, the
   power windows say the copy stops). Checked: Go tests; interface previews `move-behind.txt`, `move-behind-fail.txt`;
   test VM: a shutdown during the check of a 3 GB copy removed the partial copy, the original intact (SHA-256). Waits for
   the owner's test. **Owner's test (FrankenPC, 2026-11-10 evening):** works (Home, top bar, covers, A, the shutdown's
   question). [[step-6.6-moving-games-and-media-between-disks]]
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
3u. **The Witcher 2 (Linux) does not start** (solved 2026-11-12) (owner, FrankenPC, 2026-11-11, after installing it with owneetd 0.25.22):
   four tries, only "Starting The Witcher 2: Assassin..." on screen; the last two showed a change of screen for a split
   second (maybe a window, too quick to tell). **From the logs** (`out/test-logs/frankenpc-20261111-110726`): the install
   worked (11:10-11:17, the ZIP64 fix of 3q works). The console starts GOG's `start.sh`, which runs the game's
   `desktop-launcher` (a 32-bit GTK 2 window); the system has no 32-bit GTK 2 (`libgtk-x11-2.0`, `libgdk-x11-2.0`,
   `libcairo`, `libgdk_pixbuf` not found, only 32-bit OpenGL and Vulkan), so the launcher ends at once, `start.sh`
   with it, and owneetd sees the game end "with success" (nothing tells the user). The launcher is also a desktop window
   (it needs the pointer). Whether the game's own program (`witcher2`) misses libraries too is not known yet:
   owneet-base 0.0.63 lists, once per start, every program of the Linux games and the libraries it misses. Options to
   discuss with the owner once that is known: add the needed 32-bit libraries; start Linux games with Steam's runtime
   already on the console; start the game's own program instead of GOG's launcher. No decision yet.
   **Disk check (11:07 listing):** nothing new since 10:49 but the packages' cache (+12 MB, owneetd 0.25.22, 3p (c)).
   **The libraries (owneet-base 0.0.63, `frankenpc-20261111-113345`):** all the game's programs are 32-bit. `witcher2`
   (the game) misses only `libSDL2-2.0` and `libSDL2_image-2.0` (`libopenal-eon` is in its folder); `tenfoot-launcher`
   (the game's own launcher for the TV and the controller) misses `libSDL2`, `libSDL2_image`, `libSDL2_ttf`; GTK 2 is
   needed only by GOG's `desktop-launcher` (a desktop window), the `configurator` and the crash reporter. The console
   has SDL2 and SDL2_image in 64-bit only. Arch's multilib (snapshot 2026-10-03) has `lib32-sdl3` only (3.5 MB): no
   32-bit SDL2, SDL2_image, SDL2_ttf or GTK 2. Steam's own runtime on the console (`ubuntu12_32/steam-runtime`) has all
   of them in 32-bit, but Steam downloads it at its first start (internet, [[hard-constraints]] C9). Options for the
   owner: (A) OwneetOS builds 32-bit SDL2 (sdl2-compat over Arch's lib32-sdl3), SDL2_image and SDL2_ttf from source,
   as DOSBox Staging; (B) 32-bit Linux games start with Steam's runtime; (C) no 32-bit Linux games (the Windows version
   through Proton). And which file starts this game (GOG's `start.sh` runs the desktop launcher): the TV launcher or the
   game. **Disk check (11:33 listing):** +24.1 GB, the installed game; nothing else.
   **Owner (2026-11-11): option A** (32-bit SDL2, SDL2_image, SDL2_ttf built by OwneetOS), and The Witcher 2 tried with
   its `tenfoot-launcher` ([[games-on-disk]]). **Built:** packages `lib32-sdl2-compat` 2.32.72 (over Arch's `lib32-sdl3`),
   `lib32-sdl2_image` 2.8.12 (PNG and JPEG with stb_image) and `lib32-sdl2_ttf` 2.24.0, from the signed releases (good
   signatures, the same SHA-512 as Arch's recipes), each checked by starting a 32-bit program; owneet-base 0.0.64
   depends on them (about 0.3 MB, plus 3.5 MB for lib32-sdl3); installed through the stick's update in the test VM, the
   libraries all resolve. Waits for the owner's test: Options → the file to start → `game/tenfoot-launcher`.
   **Owner's test (2026-11-11):** with `game/tenfoot-launcher` chosen, a black screen for a couple of seconds, then it
   closes with no message. **From the logs** (`frankenpc-20261111-122626`): the 32-bit SDL2 works (the launcher starts and
   shows its window, the black screen), then it aborts: `std::logic_error: basic_string::_S_construct null not valid`
   (a text made from a value that is not there), right after "reading .../cdprojektred/witcher2/GameDocuments/Witcher
   2/config/User.ini failed" (never made yet); or an environment variable it expects from Steam (Big Picture). Not
   enough to tell: owneet-base 0.0.65 copies each Linux game's small scripts and the variable-like names inside its
   launchers to the stick, and its test log now starts after the update (no second start needed). OWNEETLOG cleaned
   (2026-11-11): its 17 logs checked identical to `out/test-logs` (six of 2026-11-09 copied then) and removed;
   `owneet-debug.txt` kept (`owneet.debug.windows_log=on`, the source of 3p (b)).
   **Start of 12:36 (`frankenpc-20261111-123623`):** the update installed owneet-base 0.0.65 at that start, after its
   old test log had started (the new order holds only from the start after it is installed: my mistake, I told the
   owner one start was enough), so no scripts yet: one more start is needed. The libraries report: `witcher2` now finds
   SDL2 and SDL2_image (only `libopenal-eon`, in its own folder, is not found by ldd); `tenfoot-launcher` misses nothing.
   The launcher made `~/.local/share/cdprojektred/witcher2/GameDocuments/Witcher 2/config` and left it empty.
   **Start of 12:42 (`frankenpc-20261111-124235`, the scripts collected):** `game/launcher` runs `./saferun.sh
   ./desktop-launcher`; GOG's `support/postinst.sh` joins the files listed in `support/split_files`, and the console
   never runs it: the game's main data `game/CookedPC/pack0.dzip` (10.5 GB) stayed in three parts (`.split00`-`.split02`),
   most likely why the launcher aborted. **Fixed:** owneetd 0.25.23 joins them after the extraction
   ([[gog-linux-game-files-left-in-parts]]); Go tests; test VM (3 GB in three parts: same SHA-256, 9 s, no space used
   twice). Waits for the owner's test: uninstall The Witcher 2 (Linux) and install it again, then start it with
   `tenfoot-launcher`.
   **Owner's test (2026-11-11):** after uninstalling and installing again, "exactly what I saw before" (black screen,
   then it closes). The owner offers a copy of The Witcher 2 to test in the VM instead of blind tests on the console.
   **In the test VM (2026-11-11, the owner's copy of the installer, installed by owneetd 0.25.23; the host's copy
   deleted after the transfer, checked by SHA-256):** three faults found. (1) `tenfoot-launcher` reads its language files
   (`game/bin/config/lang/*.ini`, GLib key files) and builds a C++ string from every value: `IK_Backslash=\ (Backslash)`
   is an escape today's GLib (2.88) refuses, `g_key_file_get_string` returns NULL and the launcher aborts (found with
   gdb: group `[InputEditor]`, key `IK_Backslash`); with the backslashes escaped it runs, writes `User.ini`, and A starts
   `witcher2`; then the launcher itself crashes (segfault, a recursion out of stack). (2) `witcher2` stops at once with
   "eON failed to initialise!": eON's log (`~/.local/share/cdprojektred/witcher2/eon.txt`) says it cannot load ICU's
   data (`icudt52l.dat`, error 4) from the game's folder: ICU takes ":" as the separator of its data folders, and the
   folder is "The Witcher 2**:** Assassin of kings". In a folder without ":" eON starts (OpenGL 4.2 through the VM's
   virgl), sound and Direct3D 9 over OpenGL start, then the game crashes after about 8 s (BREAKPAD; maybe the VM's GPU:
   to be seen on the console). (3) `witcher2` needs its own folder in `LD_LIBRARY_PATH` (`libopenal-eon.so.1`), as GOG's
   `start.sh` sets it; started directly without the launcher it makes its own settings and reaches the same point.
   Decisions for the owner: the folder's ":" (the console's install folder without ":"), how this game starts (directly,
   or the TV launcher with its language files fixed).
   **Owner (2026-11-11):** install folders without ":" (": " → " - "); for a game folder on the console's disk (an
   install in place, as on the FrankenPC), the folder is **renamed** first (not a new folder next to it); the game starts
   directly, named by a **list of known games** (by GOG id), with its folder in `LD_LIBRARY_PATH` ([[games-on-disk]],
   [[linux-game-fails-in-a-folder-with-a-colon]], [[witcher-2-tenfoot-launcher-aborts-on-its-language-files]]).
   **Built:** owneetd 0.25.24 (`installs.FolderName`; a name with ":" refused; the in-place folder renamed when the
   request names it without ":"; the title in `.owneet-installed`; Go tests), owneet-frontend 0.38.16 (the install folder
   without ":", `disk.install.folder` for the progress, the title from the mark, `known-games.json` with The Witcher 2 →
   `game/witcher2`, `LD_LIBRARY_PATH` for ELF programs). **Test VM:** uninstalled, the folder named back with ":", the
   interface's new request (dest without ":"): owneetd renamed the folder, installed the game in 9 min 2 s, the mark
   holds the title; the interface shows "The Witcher 2: Assassin of kings" and starts `game/witcher2`; launched through
   owneetd with that command, eON starts (OpenGL 4.2, D3D9 over OpenGL), then the same crash after about 9 s as before
   (the VM's GPU, to be seen on the console). The owner's choice of `tenfoot-launcher` in Options is saved under the
   old folder name, so it no longer applies (a stale line in `disk-games.json`, see 3t). Waits for the owner's test:
   uninstall The Witcher 2 (Linux), install it again (its folder is renamed), start it.
   **Owner's test (2026-11-11, `frankenpc-20261111-165318`): the game starts.** Three new reports: (1) without the
   launcher the game's language cannot be changed, not even from its settings; (2) after Guide, the game's sound is
   heard on the home screen; (3) the game had to be selected a couple of times: no full-screen "starting" screen, only
   the banner, gone after a second (maybe the first start was a long load). **From the logs:** uninstall, the folder
   renamed, install 16:54-17:02 (8 min), the library shows the title with ":" and starts `game/witcher2` through
   `env LD_LIBRARY_PATH=…`; one launch only (17:06:10), the game's window on screen 13 s later; Guide at 17:07:14,
   back to the game, home again, closed 17:07:43. (3) Linux games show only the banner "Starting {title}…"
   (`toast.launch`); the full-screen "Preparing {game}…" until the first picture is for Windows and Steam games
   only, so for 13 s nothing showed the game was starting; the other presses of A found it running (no second
   launch). (2) The game keeps running behind the home screen ([[guide-button]], 2026-10-07), its sound with it.
   (1) The game keeps its languages in `~/.local/share/cdprojektred/witcher2/GameDocuments/Witcher 2/config/User.ini`,
   section `[linux]`, `Language=EN` (texts) and `Speech=EN`, written by its launchers; the owner's copy has texts in
   CZ DE EN ES FR HU IT JP PL RU TR ZH and speech in DE EN FR PL RU (no Italian speech). Choices for the owner.
   **Disk check (17:03 listing):** the listing ran during the install (the game's folder half written, with
   `.owneet-installing`), not junk; new: two core dumps of `tenfoot-launcher` from the morning (23.6 MB each, 3p (e))
   and owneetd 0.25.23 in the packages' cache (3p (c)). The 2 TB disk unchanged.
   **Owner (2026-11-11):** (1) the launcher comes back ("the cleanest"); (2) the game's sound off while the home screen
   is shown; (3) the full-screen "Starting {game}…" for Linux games too. (2) was already decided on 2026-11-09 and
   built: it failed because the game's sound stream has no process id, only its client
   ([[game-sound-heard-behind-the-home-screen]]). **Built:** owneetd 0.25.25 (the client's process id), owneet-frontend
   0.38.17 (`known-games.json`: The Witcher 2 → `game/tenfoot-launcher` and `fix-key-files` for its language files;
   "Starting {game}…" for games on a disk until their first picture or their end). **Test VM:** the 14 language files
   fixed when the library was read (only the `IK_Backslash` line), the library starts `game/tenfoot-launcher`, the
   launcher stays open (no abort); its screen cannot be seen in the VM (3D, no screenshot) and neither the virtual pad
   nor the keyboard reached it, so its language choice, the start of the game from it, and the silence after Guide
   (the VM's cage session ignores a short Guide) wait for the console. Seen in the VM: after the game crashed, its
   `CrashReporter` kept running for 26 minutes, so owneetd kept the game "running" (to watch on the console).
   OWNEETLOG: the test's logs copied and checked identical, but their removal from the stick was blocked by a safety
   check (files at the top of a drive): left on the stick.
   **Owner's test (2026-11-11, owneet-frontend 0.38.17):** "Starting …" was shown (step 2's first part fine), then a
   black screen; the launcher never showed; closing it from the home screen was not immediate; a second start changed
   nothing. **From the logs (`frankenpc-20261111-173334`):** the 14 language files fixed at the library's reading, the
   launcher started (only "Joystick added: 0" in its output, no abort), its window on screen; closing waited the 10 s
   limit and the launcher was killed (it ignores the request to end): hence the slow close. **Test VM, without 3D**
   (screenshots possible; window caught with `xwd`): the launcher's window is all black there too, so not gamescope's
   fault; under gdb it loads its font (`linux/tenfoot/mplus-2m-medium.ttf`) and makes its renderer, but in 25 s it loads
   no image and never presents a frame (`SDL_RenderPresent` never called): it waits for something before drawing.
   **Found (test VM, 2026-11-12; reproduced under gamescope, headless):** (1) **black screen:** the launcher's main loop
   updates only when one turn lasts more than 10 ms (`now - last > 10`, else `last = now`), and each turn waits with
   `SDL_WaitEventTimeout(NULL, 1)`; old SDL2 polled every 10 ms, so a turn lasted at least 10 ms; SDL3 (through
   sdl2-compat) waits 1 ms, so the update never runs (a pause, as gdb's, unblocks it). A prototype library restoring
   the old wait (10 ms when nothing comes, `LD_PRELOAD`, game files untouched) shows the menu at once; the pad moves
   through it; Options has "Text Language" and "Voice-over Language". (2) **crash on Start Game:** a recursive tree
   walk (a `std::map` being destroyed) runs out of stack before the game starts; it depends on the memory addresses:
   with address randomisation off (`setarch -R`, as under gdb) the launcher saves, starts `./witcher2` and ends
   normally. (3) **the game closed with the launcher:** the launcher ends after starting the game; owneetd's unit
   (`Type=exec`, `KillMode=control-group`) ends with its main program and stops `witcher2` at once (eON: "Log system
   shutdown"). (4) **slow close:** the launcher logs `SDL_QUIT` and ignores it, so it is killed after the 10 s limit.
   **Correction (6 runs, 2026-11-12):** the crash does not depend on address randomisation (2 crashes in 3 runs with it,
   2 in 3 without): it happens in the launcher's own clean-up **after** it has started the game (the game started in all 6
   runs); the game seemed not to start because owneetd's unit stopped it with the launcher. Address randomisation stays
   on. **Prototype 2** (one small 32-bit library, `LD_PRELOAD`, game files untouched): the old 10 ms wait; the launcher
   ends at once (`_exit`) once it has started the game, skipping its crashing clean-up (its settings are saved before);
   `SDL_QUIT` ends it at once. 3 runs: no crash; closed from its menu in 37 ms (10 s before). With the launcher in a unit
   kept while any of its programs runs (`ExitType=cgroup`), the game goes on after the launcher ends (eON reaches sound
   init; in the VM it then crashes, the VM's GPU, and its `CrashReporter` keeps the unit alive). Owner asked for a
   fuller explanation before choosing.
   **Owner (2026-11-12):** the library is built; the "while any program runs" rule only for this game, to be reviewed
   over his ~90 games ([[games-on-disk]]). **Built:** `lib32-owneet-compat` 0.1.0 (`compat/old-sdl2-launcher`, with
   its own checks), owneetd 0.25.26 (`handover` in the launch request: `ExitType=cgroup`; no home screen while the
   unit has a process; Go test), owneet-frontend 0.38.18 (`launchers` in `known-games.json`: The Witcher 2's
   `game/tenfoot-launcher` with `old-sdl2-launcher`, hands over), owneet-base 0.0.66 (depends on the library). **Test
   VM, started from the library with the virtual pad:** the command carries the library, the unit `ExitType=cgroup`;
   the launcher's menu shows; A on Start Game: the launcher ends with 0 (no crash, no core dump), the app stays,
   `./witcher2` runs in its unit (it draws, even in the VM without 3D); closed from the API in 96 ms, home screen back.
   Waits for the owner's test: the language in Options, Start Game, the game's sound behind the home screen (Guide).
   Seen while building: the guard hook blocked a shell command that only wrote a PKGBUILD's text (a false positive,
   reported to the owner; the files were written with the editor instead).
   **Owner's test (2026-11-12):** the launcher shows, but it is clearly broken: navigating works badly; after changing the
   text language a couple of times the console went back to the home screen (no crash); it is not clear how to apply or
   cancel the changes. Start Game not tried. Being looked at in the logs.
   **From the logs (`owneet-20261112-113319`, read on the stick):** the "home screen" was the launcher crashing twice while
   the options were changed (same tree walk, stack overflow), not only after Start Game. **valgrind (test VM, 32-bit,
   Arch's debuginfod):** the launcher reads a `std::map` node right after deleting it (use after free in its own code);
   old glibc left freed blocks intact, today's writes into them at once. `GLIBC_TUNABLES=glibc.malloc.tcache_count=0`
   does not help (6 crashes in 6 runs with or without it); keeping deleted memory (`operator delete` does nothing in the
   library) does: 0 crashes in 3 runs of ~20 language changes. **Controller:** B changed values instead of going back
   (its own 2014 mapping list, `SDLGamepad.config`). **Owner (2026-11-12): the launcher MUST stay; drive it with the
   controller pointer**, turned on by hand as today. Built in `lib32-owneet-compat` 0.2.0: deleted memory kept, the
   controller hidden from the launcher (one meaning per button), its cursor shown. **Test VM (gamescope, headless):** the
   pad no longer acts on it; the pointer cannot be tried there (headless gamescope gets no virtual mouse); a mouse click
   (xdotool) on its buttons does **nothing**: the TV launcher ignores the mouse; the **keyboard works well** (arrows move
   and change values at once, Enter opens, Esc goes back keeping the choices; the settings are written at Start Game).
   Asked to the owner: the controller turned into the launcher's keys by the library, since the pointer cannot work.
   **Owner: "let's try".** **Built:** `lib32-owneet-compat` 0.3.0 (the library opens the controllers itself and hands the
   launcher key events: D-pad and left stick = arrows, A = Enter, B = Esc; joystick and controller events hidden; the
   cursor left as the launcher wants it; checks for buttons, stick, hidden events). **Test VM (gamescope, headless, the
   virtual pad):** down + A opened Options, right twice set the text language to German at once, B went back to the
   main menu (in German), A on Start Game saved `Language=DE` in `User.ini`, the launcher ended with 0 and `./witcher2`
   ran in its unit. Waits for the owner's test with his controller.
   **Owner's test (2026-11-12): all checks passed** (launcher, language, Start Game, the game, Guide) **until he quit the
   game**: a window on a black background titled "CrashReporter": "CrashReporter.x86_64 failed to start due to the
   following dependancy problems: Inconsistency detected by ld.so: dl-version.c: 204: _dl_check_map_versions: Assertion
   `needed != NULL' failed!"; closed from the home screen. **From the logs (`owneet-20261112-122336`):** the game crashed
   while quitting (`BREAKPAD CRASH`, 12:25:47); its crash handler ran `CrashReporter` (a script: its 64-bit
   `CrashReporter.x86_64` from 2015 cannot load on today's glibc), whose script showed the error with **zenity** (a
   desktop window). Closing from the home screen stops the game cleanly (no crash). **Owner (2026-11-12): a second
   library** ([[games-on-disk]]). **Built:** `lib32-owneet-compat` 0.4.0 (`compat/no-crash-reporter`: `execv` of
   `CrashReporter` ends at once; the launcher's library hands it to the game through `OWNEET_GAME_PRELOAD` in place of
   itself), owneet-frontend 0.38.19 (`game-compat` in `known-games.json`). **Test VM (gamescope, headless):** the game
   had only the new library in `LD_PRELOAD`; a crash (SIGSEGV) → `BREAKPAD CRASH`, no reporter, no zenity, the app
   ended in about 1 s and the home screen came back. Waits for the owner's test (quit from the game's menu).
   **Owner's test (2026-11-12, `owneet-20261112-124235`): all passed, "finally playable".** The game crashed again when
   quit from its menu (`BREAKPAD CRASH`): no reporter, no window, the app ended (success), home screen back. **Solved**
   with the game on the console's own disk (owner: not tried yet with the game on the SATA disk).
   **Owner's test (2026-11-12):** moved to the SATA disk, started fine from there, then uninstalled. Next: installing it
   straight on the SATA disk (3l), once built.
   **Disk check (that log's listings, read on the stick):** cut (no `complete.txt`: the console was switched off before
   they ended; `/home`'s listing stops after ~100 000 lines, the SATA disk and `/var/log` missing); readable part: the
   packages' cache 0.58 GB in 173 files (was 0.51 GB, 3p (c)), 5 core dumps, 0.11 GB (3p (e)).
3v. **Steam's shader compiling shows the library with no notice** (owner, FrankenPC, 2026-11-12): after installing
   Batman: Arkham Knight (Steam), at its first start, while Proton compiled its shaders, the console went back to the
   library's page with nothing saying the game was still being prepared; the owner had to open Steam again to see that
   the process had not ended. Not looked at yet (no logs of that start read). [[step-4.2c-steam-without-its-interface]]
3w. **Parts of the interface cut off** (owner, 2026-11-12): the final "S" of the logo, and in some cases the library's
   filter bar. Not looked at yet (which screens and screen sizes to find out). [[design-tokens]]
   **Looked at (test VM, 2026-11-12, 1280×800 and 1920×1080 with `OWNEET_VM_RES`, English and Italian, text M and XL):**
   neither cut reproduced (the S measured whole; the filter bar whole, "Giocati di recente" on its right). The logo's
   canvas was a fractional width (e.g. 209.6 px) with the word ending exactly at its edge: owneet-frontend 0.38.22
   gives it whole pixels and 2 more (no visible change). **Other cuts found with text XL:** (a) the settings' side list:
   "Controllers and Bluetooth" overflows its row when highlighted and is cut without "…" when not (3s's rule:
   highlighted texts scroll, the others end with "…"); (b) the prompt bar: "Menu" runs into "LB" in Italian; (c) a
   list's highlighted row (the language picker) grows and its ring is cut at the top by the list's edge; (d) the home's
   "CONTINUA A GIOCARE" label touches the hero card. Asked the owner: a photo of his cuts (logo, filter bar) with the
   TV's resolution and the text size, and whether (a)-(d) are fixed now (a with 3s).
   **Owner (2026-11-12):** a screenshot in the next tests: **the test log takes one every 30 seconds** ([[test-pcs]]);
   (a) with 3s's demo; (b) the prompt bar: asked to be explained better (what gives way when it does not fit).
   **Owner (2026-11-12):** option 1, only when the bar does not fit, the prompts on the right (Sections, Home) keep
   their buttons and lose their words ([[design-direction]]); demo first: `design/demos/3.3c-prompt-bar-fit.html`
   **approved** (owner, 2026-11-12). **Built** (owneet-frontend 0.38.24, `PromptBar`; checked with `tools/frontend-preview`,
   `prompt-bar-fit.txt`: the library in English with text size XL keeps only [LB][RB] and Home on the right).
   (c) and (d): the owner asked to fix them (2026-11-12), no change of look. **(c) built** (0.38.24): windows (`Sheet`)
   leave 22 px at the sides and 14 px above and below their content for the ring and the lift, the rows where they
   were; the language picker's first row now shows its ring whole. **(d) cause:** with text size XL and a title on two
   lines, the hero card's text is taller than the card, so its label goes above the card's top; how to make room is
   a change of look: asked the owner (title on one line with "…" only then, or less space between its lines).
   **Owner (2026-11-12): less space between the card's rows. Built** (owneet-frontend 0.38.25): 12 px between them,
   down to 4 px only when they do not fit with 30 px above and below; checked with `tools/frontend-preview`
   (`home-long-title.txt`, `@longtitle`): at text size XL with a two-line title the label stays inside the card,
   about 8 px from its top edge on the 1280×720 grid (4 px is the least space between rows). Waits for the owner's look.
   **Owner's test (2026-11-12 18:06, `owneet-20261112-180643`, FrankenPC, 1366×768):** the long texts that scroll and
   the prompt bar work; the screenshots every 30 s work (seven saved, 31 to 82 s apart while the log's other work ran);
   the home's card not checked (the Steam game he started did not come to the front: 3z); the display area at the next
   test. **New cut, from his screenshots:** in the library, with the grid scrolled down, the covers scrolled up cut the
   bottom edge of the filters: the grid started 2 px over the filter bar. **Fixed** (owneet-frontend 0.38.26): the grid
   starts right under the filters, the covers 16 px below as before (no change of look).
   **Screenshot every 30 seconds built** (owneet-base 0.0.67): `owneet-testlog` asks gamescope
   (`gamescopectl screenshot`) and keeps the last 240 in `owneet-<start>.screens/HHMMSS.png` on the stick; checked in
   the test VM (one every 31-32 s; the VM's pictures are black, it has no graphics card).
   `tools/frontend-preview` waited a fixed 7 s at the start, shorter than the start-up animation since 2026-11-05 (the
   first buttons were ignored): it now waits for the theme's "The start-up animation is over".
3x. **The brightness slider does nothing** (owner, 2026-11-12): Settings → Display's brightness does not change
   anything; **owner: remove it**, brightness comes back in Wave 2 ([[settings-screens]], [[wave-2]]). **Built**
   (owneet-frontend 0.38.21, 2026-11-12): the slider removed from Settings → Display; owneetd keeps
   `/v1/display/brightness` for Wave 2. Waits for the owner's look on the console.
3y. **"Show TV safe area" does nothing** (owner, 2026-11-12): Settings → Appearance → "Show TV safe area" seems to have
   no effect, or works wrongly. To be reviewed (what it should show, and on which screens). [[settings-screens]]
   **Looked at (test VM, 2026-11-12):** it draws a 1 px solid outline in the muted colour at 70 % (`theme.qml`, Theme.safeX
   64 px at the sides), barely visible on a TV, on the very edge of the content (the logo starts on it, the clock touches
   it, the focus ring goes past it on the right); it only shows the area, it changes nothing in the layout. The approved
   demo 3.3 (`design/demos/3.3-theme-foundations.html`) has it **dashed** with the label "safe area 5%" at the top right:
   the code does not match the demo. Screenshot sent to the owner; what it should do asked.
   **Owner (2026-11-12):** a TV safe area that works as on common devices; the outline was useless in the demo
   too, so not that way. **Decided:** Settings → Display → "Display area", a full-screen adjustment (an arrow in
   each corner, the D-pad until their tips touch the screen's edges, X whole screen, A confirm, B cancel), the
   console's screens drawn inside the area; "Show TV safe area" leaves Appearance ([[screens-and-display]]).
   **Demo** `design/demos/3.9c-display-area.html` (on a simulated TV that cuts its edges): **approved** (owner,
   2026-11-12). **Built** (owneet-frontend 0.38.23): Settings → Display → "Display area" (`DisplayArea.qml`), the
   theme drawn inside the area (`Theme.areaX` / `areaY`, saved; the frontend's `main.qml` places the theme, the
   background painted to the screen's edges), "Show TV safe area" removed; checked with `tools/frontend-preview`
   (`tools/preview-steps/display-area.txt`). Waits for the owner's look on the TV.
3z. **A Steam game started, never shown** (owner, FrankenPC, 2026-11-12 18:09): My Little Puppy (Steam, on the SATA
   disk) "did not start". **From the logs:** it did start and ran almost 4 minutes, its window behind Steam's page;
   Steam's new client starts games in a systemd scope of their own, out of Steam's unit, so owneetd never noticed the
   game ([[steam-game-runs-hidden-behind-steam]]). **Fixed** in owneetd 0.25.28 (`unitOfCgroup`). Waits for the
   owner's check. May also explain 3v.
   **Disk check (2026-11-12 18:06 listings):** nothing new since 12:48: the same 13 Windows prefixes and Proton logs
   (3p a, b), the packages' cache 0.60 GB in 176 files (3 more, 3p c), 5 core dumps 0.11 GB (3p e); on the SATA disk
   Steam's wanted downloads (42.5 GB), shader caches 5.0 GB, the new game's prefix (Steam's `compatdata`), The Witcher
   2's installer.
3aa. **The Witcher 2's folder doubled** (owner, FrankenPC, 2026-11-13): the Linux version is now in two folders, one
   whose name has ":" and one with " - ", by mistake. Not in the logs yet: on 2026-11-12 at 18:06 the SATA disk had
   only "The Witcher 2 - Assassin of kings" with its installer. **owneet-base 0.0.68** (checked in the test VM with two
   such folders): once per start the test log writes in its report each games folder as its name really is, its size,
   its top and the console's own files in it (install marks, game.txt, gameinfo), the user's start choices
   (`disk-games.json`) and owneetd's installs; the journals of the five previous starts (were three), to find when it
   happened. On OWNEETLOG; waits for the owner's start with the stick, before his tests of The Witcher 2.
3q. **The Witcher 2 Linux version does not install** (owner, FrankenPC, 2026-11-11): "the game could not be installed",
   twice (the second time with OWNEETLOG plugged in while the console ran: the logs start only with a stick in at the
   start, so neither attempt is on the stick; the console still ran yesterday's versions, the update comes from the
   stick at the start). Its journal is on the console's disk: owneet-base 0.0.62 copies the whole journals of the three
   previous starts to the stick, so the next start with the stick brings it (if no more than two starts come first).
   **Owner's retry with the stick (2026-11-11 10:51, `frankenpc-20261111-104856`):** A on Install at 10:51:39, no install
   in owneetd's log: the check of the installer (`/v1/installs/inspect`) failed, and its error was not logged (the
   0.0.62 test log missed this start: the update installed it one second after the log started). **Cause:** a GOG Linux
   installer over 4 GB has a ZIP64 archive after its script, whose ZIP64 records do not count the script; Go's
   `archive/zip` cannot follow them ("zip: not a valid zip file"; reproduced with 70 000 entries and with a 4.3 GB
   archive). **Fixed:** owneetd 0.25.22 reads such an archive from where it really starts (`zipStart`), and logs an
   installer that cannot be read; Go tests (`TestZip64AfterTheScript`, and a one-off 4.3 GB check). Waits for the owner's
   test. [[step-4.6-installers]]
3r. **Owner's tests of 2026-11-11 (logs `frankenpc-20261111-101811`, `-101928`):** (2) he moved The Witcher 2's installer
   to the SATA disk: the change of free space is too small to see on screen; in the session without the stick, so not
   logged yet (3q's journals). (3) a deletion on the SATA disk (10:18:46, owneetd 0.25.21, "game deleted from
   its disk"): the library shows 1.9 TB before and after (rounded to 0.1 TB); the SATA disk is ext4 (frees at once);
   owneet-base 0.0.62 writes every disk's room in bytes in each report, to read such changes. (4) the restart done.
   **Owner (2026-11-11), on (2):** he had moved the Linux installer to the SATA disk for lack of room, and moved it back
   to the console's disk this morning (deleting the Windows version for that) to install it from there: so it is right
   that the 10:49 listing shows it on the console's disk.
3s. **Long texts scroll instead of "…"** (owner, 2026-11-11): where a text is cut with "…", make it scroll so it can be
   read whole, everywhere in the project (28 places in the theme, 12 files, `elide`). A change of look and behaviour:
   demo first ([[demo-before-code]]); open questions for the demo: when it scrolls (only the selected item, or every cut
   text), speed and pauses. **Owner (2026-11-11):** only the highlighted texts scroll ([[design-direction]]). Open: the
   texts never highlighted (e.g. the details window's long installer name, shortened in the middle since 2026-11-10).
   **Owner (2026-11-11):** texts never highlighted keep "…". Next: the demo.
   **Demo** `design/demos/3.3b-scrolling-text.html` (2026-11-12, Settings with text size XL, also 3w (a)): the
   highlighted text that does not fit waits 1.5 s, scrolls at 45 px/s on the 1280×720 grid, waits 1.5 s at its end,
   fades back to the start and repeats; soft edges while it moves; speed and pauses can be changed in the demo.
   **Approved** (owner, 2026-11-12), with these values. **Built** (owneet-frontend 0.38.23): `foundation/FitText.qml`
   in every one-line text that was cut with "…" and in Settings' list of sections (3w a); it scrolls while the
   selectable item around it is highlighted. Checked with `tools/frontend-preview` (`long-texts.txt`). Texts on two
   or more lines (e.g. covers' titles) keep "…" for now: asked the owner. Waits for the owner's look on the TV.

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
