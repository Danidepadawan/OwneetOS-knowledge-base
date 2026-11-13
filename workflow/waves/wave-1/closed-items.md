---
type: meta
description: "The Wave 1 open items that are closed: the owner's reports solved and confirmed, with their whole history. Read it when an old item number (e.g. 3u) is named; the open ones are in open-items."
tags: [wave, open-items]
---
# Wave 1 — closed items

The items of [[open-items]] the owner has confirmed (or dropped), moved here with their whole
history when they are closed; they keep their number, so "[[open-items]] 3u" in older notes is
found here. Newest closings are added at the end.

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
   **Closed** (2026-11-13): the owner's test (FrankenPC, 2026-11-10 evening) works.
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
   **Closed** (2026-11-13): the owner's tests (2026-11-12): "finally playable", also from the SATA disk.
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
   **Closed** (2026-11-13): the owner's test (2026-11-13): text size XL all right apart from 3ab (an item of its own).
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
   **Closed** (2026-11-13): the owner's test (2026-11-13): the display area all right on his TV.
3z. **A Steam game started, never shown** (owner, FrankenPC, 2026-11-12 18:09): My Little Puppy (Steam, on the SATA
   disk) "did not start". **From the logs:** it did start and ran almost 4 minutes, its window behind Steam's page;
   Steam's new client starts games in a systemd scope of their own, out of Steam's unit, so owneetd never noticed the
   game ([[steam-game-runs-hidden-behind-steam]]). **Fixed** in owneetd 0.25.28 (`unitOfCgroup`). Waits for the
   owner's check. May also explain 3v.
   **Disk check (2026-11-12 18:06 listings):** nothing new since 12:48: the same 13 Windows prefixes and Proton logs
   (3p a, b), the packages' cache 0.60 GB in 176 files (3 more, 3p c), 5 core dumps 0.11 GB (3p e); on the SATA disk
   Steam's wanted downloads (42.5 GB), shader caches 5.0 GB, the new game's prefix (Steam's `compatdata`), The Witcher
   2's installer.
   **Closed** (2026-11-13): the owner's test (2026-11-13): the Steam game started and came to the front.
3aa. **The Witcher 2's folder doubled** (owner, FrankenPC, 2026-11-13): the Linux version is now in two folders, one
   whose name has ":" and one with " - ", by mistake. Not in the logs yet: on 2026-11-12 at 18:06 the SATA disk had
   only "The Witcher 2 - Assassin of kings" with its installer. **owneet-base 0.0.68** (checked in the test VM with two
   such folders): once per start the test log writes in its report each games folder as its name really is, its size,
   its top and the console's own files in it (install marks, game.txt, gameinfo), the user's start choices
   (`disk-games.json`) and owneetd's installs; the journals of the five previous starts (were three), to find when it
   happened. On OWNEETLOG; waits for the owner's start with the stick, before his tests of The Witcher 2.
   **Owner (2026-11-13):** he downloaded it last night, without the stick; check every folder about The Witcher 2,
   then, once the tests are over, find a fix for the doubled folder. **owneet-base 0.0.69** (checked in the test VM):
   the report also lists everything named after The Witcher 2 on every disk (each folder: size, files, date, top, the
   console's own files; each file with "witcher" in its name). On OWNEETLOG.
   **Cause found (owner's start of 2026-11-13 10:10, `owneet-20261113-101059`, journal of 2026-11-12 18:44):** not a
   download. At 18:44 the owner plugged in the USB disk SSD-256GB-D, whose `Giochi` had "The Witcher 2: Assassin of
   kings" (the Linux installer) and "The Witcher 2: Win" (the Windows one); the console offered to copy them ("Disco USB
   collegato: 2 giochi") and copied both to the SATA disk (owneetd `moves`, 18:44:59). The copy keeps the source
   folder's name (`filepath.Base`, ":" included) and only adds " (2)" when the same name is there: it did not see that
   the SATA disk already had the same game as "The Witcher 2 - Assassin of kings" (the name the console gives it,
   `installs.FolderName`, 3u). The library now shows three local games. The test log's search for "witcher" did not
   enter the disks (`find -xdev` from `/run/media/owneet`): fixed in the next owneet-base. Fix to agree with the owner.
   **Closed** (owner, 2026-11-13): after deleting the three folders and copying both again from the USB disk, no
   folder is doubled; no fix needed now (a copy keeps ":", the install renames it to " - ", 3ad).
3ac. **Owner's test of 2026-11-13:** the Steam game started and came to the front (3z works); next, a game whose shaders
   take long the first time (as Batman: Arkham Knight, 3v). The display area: all right. Text size XL: all right apart
   from 3ab. The Witcher 2 on the SATA disk: after 3aa's fix.
   **Closed** (2026-11-13): a record of that test; what is left is in 3v and 3ab.
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
   **Closed** (2026-11-13): the install worked at the owner's next try (2026-11-11 11:10-11:17, 3u).
3r. **Owner's tests of 2026-11-11 (logs `frankenpc-20261111-101811`, `-101928`):** (2) he moved The Witcher 2's installer
   to the SATA disk: the change of free space is too small to see on screen; in the session without the stick, so not
   logged yet (3q's journals). (3) a deletion on the SATA disk (10:18:46, owneetd 0.25.21, "game deleted from
   its disk"): the library shows 1.9 TB before and after (rounded to 0.1 TB); the SATA disk is ext4 (frees at once);
   owneet-base 0.0.62 writes every disk's room in bytes in each report, to read such changes. (4) the restart done.
   **Owner (2026-11-11), on (2):** he had moved the Linux installer to the SATA disk for lack of room, and moved it back
   to the console's disk this morning (deleting the Windows version for that) to install it from there: so it is right
   that the 10:49 listing shows it on the console's disk.
   **Closed** (2026-11-13): a record of that test; nothing left to do.
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
   **Closed** (2026-11-13): the owner's test (2026-11-12 18:06): the texts that scroll work. Texts on more lines (covers' titles): 3ad (2).
