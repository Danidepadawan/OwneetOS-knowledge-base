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
   **Closed** (2026-11-13): the owner's test (2026-11-13): every test of The Witcher 2 passed, both versions installed straight on the SATA disk and started.
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
   **Closed** (2026-11-13): the owner's test (2026-11-13): the home's card at text size XL (buttons and title that scroll) solved.
3d. **The console's disk has less room** (owner, 2026-11-10): about 57 GB free, about 80 the day before.
   Not explained by the logs (the report did not measure folders; Steam's Cyberpunk download is at
   1.3 GB; a stick update is about 216 MB). The owner installed The Witcher 2 the day before, perhaps on
   this disk by mistake. The test report measures the console's disk from owneet-base 0.0.60 (testers
   only, owner's condition): to read in the next logs. [[open-items]]
   **Closed** (2026-11-13): closed by the owner (2026-11-13): explained, the install of 2026-11-09 went to the console's disk by design (3l).
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
   **Closed** (2026-11-13): closed by the owner (2026-11-13), with the tests of The Witcher 2.
3i. **The details window's text out of the window** (owner, 2026-11-10 12:32, "the installer's description"): most likely
   the installer's long file name in the facts (The Witcher 2): the facts' grid has no width limit and the window does not
   widen for it. Owner (2026-11-10): shortened in the middle with "…". **Built** (owneet-frontend 0.38.10, checked in
   the preview with a long installer name); waits for the owner's test. [[step-4.6-installers]]
   **Closed** (2026-11-13): closed by the owner (2026-11-13), with the tests of The Witcher 2.
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
   **Closed** (2026-11-13): closed by the owner (2026-11-13), with the tests of The Witcher 2 (the failed removal only logged: not proposed further).
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
   **Closed** (2026-11-13): closed by the owner (2026-11-13), with the tests of The Witcher 2.
3v. **Steam's shader compiling shows the library with no notice** (owner, FrankenPC, 2026-11-12): after installing
   Batman: Arkham Knight (Steam), at its first start, while Proton compiled its shaders, the console went back to the
   library's page with nothing saying the game was still being prepared; the owner had to open Steam again to see that
   the process had not ended. Not looked at yet (no logs of that start read). [[step-4.2c-steam-without-its-interface]]
   **Cause found (2026-11-13, 3ae):** at a game's first start Steam runs its install script with a launcher of the
   game's id (`reaper SteamLaunch AppId=N Install=1`); owneetd took it for the game, stopped watching Steam's launch,
   and when the script ended counted the game as closed (home screen), while Steam, hidden, went on to its shader
   cache ("waiting for user response to ProcessingShaderCache"). **Fixed** in owneetd 0.25.30: the install script is
   not a game, so Steam's launch is still watched and Steam (its shader page) is shown when it waits
   ([[steam-game-loses-the-screen-at-its-first-start]]). Waits for the owner's test.
   **Closed** (2026-11-13): the owner's test (2026-11-13 13:55, owneetd 0.25.30): Steam was shown while it prepared the shaders, then the game started and stayed in front.
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
   **Owner (2026-11-13):** every test of The Witcher 2 passed, (1) included (the Windows version installed in place on
   the SATA disk, its cover kept): (1) closed. Demo 3.7b **approved**. **Built** (owneet-frontend 0.38.29,
   `foundation/Cover.qml`: the title is a `FitText`; checked with `tools/frontend-preview`, `cover-titles.txt`: titles
   end with "…", the highlighted one scrolls). On OWNEETLOG; waits for the owner's look.
   **Closed** (2026-11-13): the owner's test (2026-11-13): (1) with The Witcher 2, (2) the covers' titles all right.
3ae. **Batman: Arkham Knight at its first start** (owner, FrankenPC, 2026-11-13; log `owneet-20261113-124039`): (a) started
   with Steam closed, it "closed unexpectedly"; (b) started again with Steam open, it paused and could not be opened,
   neither from the console nor from Steam; (c) leaving Steam (still running), the start sound played twice.
   **From the logs:** (a) 12:59:25 owneetd logged "Steam game started" for Steam's install script (`reaper SteamLaunch
   AppId=208650 Install=1 … iscriptevaluator.exe`), its window came at 12:59:39 and went at once, owneetd counted the
   game as ended (12:59:40) and showed the home screen, while Steam, hidden, went on to "ProcessingShaderCache" and
   waited: the game itself never started (3v). (b) 13:00:25 the game's window came, gamescope focused it, and 35 ms
   later the home screen: Steam had written what gamescope shows using the ids it read back from the windows, which
   owneetd sets (`STEAM_GAME`: 2124305299, the game, not 208650); owneetd did not know them, left the game out and
   kept only Steam (hidden) and the home screen; the game paused without focus, and Steam's "resume" used the same
   unknown id. (c) 13:01:34, after Guide held over Steam: Steam took the screen back for 6 ms before owneetd put the
   home screen back; each "on screen" change was announced and the interface plays its sound on each return home.
   **Fixed** (owneetd 0.25.30, Go tests): the install script is not a game; Steam's requests in owneetd's own ids are
   understood, and a Steam game in front stays in front unless Steam names it; a focus gamescope shows for a moment
   after someone else's write is not announced; Steam's requests are logged
   ([[steam-game-loses-the-screen-at-its-first-start]]). On OWNEETLOG; waits for the owner's test (Batman: Arkham
   Knight from the console, Steam closed first).
   **Disk check (12:42 listing, during the Windows install):** nothing new: 14 Windows prefixes 7.9 GB (the 14th is The
   Witcher 2's Windows version, in use), Proton's logs 1.4 GB (3p b), packages' cache 0.63 GB in 186 files (3p c), 5
   core dumps (3p e); on the SATA disk The Witcher 2's two folders (installers kept by design), Steam's games and its
   wanted downloads.
   **Closed** (2026-11-13): the owner's test (2026-11-13, log `owneet-20261113-132101`): Batman: Arkham Knight started from the console with Steam closed (Steam shown at 13:55:21 while it waited, the game at 13:55:42, in front at 13:55:54), Guide and Resume, Steam left: all passed.
3m. **The notification's sound during the start-up animation** (owner, FrankenPC, 2026-11-10): a controller plugged in while
   the animation played made the `notify` sound, which the owner had asked never to happen ("the other sounds removed while
   the start-up sound plays"); hard to repeat, so tested by the assistant in the test VM. **Fixed** (owneet-frontend 0.38.12,
   checked in the test VM with the sound recorded). [[step-7.6-final-logo-and-brand]]
   **Closed** (2026-11-13): the owner (2026-11-13): it has not happened again in his tests.
3x. **The brightness slider does nothing** (owner, 2026-11-12): Settings → Display's brightness does not change
   anything; **owner: remove it**, brightness comes back in Wave 2 ([[settings-screens]], [[wave-2]]). **Built**
   (owneet-frontend 0.38.21, 2026-11-12): the slider removed from Settings → Display; owneetd keeps
   `/v1/display/brightness` for Wave 2. Waits for the owner's look on the console.
   **Closed** (2026-11-13): the owner's look (2026-11-13): the slider is gone from Settings → Display.
5. **The authors at the top of the console's Credits** (3.9b): demo
   `design/demos/3.9b-credits-authors.html` **approved** (owner, 2026-11-13). **Built** (owneet-frontend 0.38.29: the
   new "Authors" table of `CREDITS.md`, `SystemInfo::authors()`, `CreditsSheet.qml`; checked with
   `tools/frontend-preview`, `credits-authors.txt`). On OWNEETLOG; waits for the owner's look. [[step-3.9-settings]]
   **Owner's test (2026-11-13): the names are not shown.** Cause: `CREDITS.md` reaches the console in **owneet-base**
   (`/usr/share/doc/owneetos/CREDITS.md`), which was not built again, so the console had the file without the Authors
   table (the preview reads the repository's). **owneet-base 0.0.71** (the new `CREDITS.md` checked inside the
   package), on OWNEETLOG; waits for the owner's look. Watch: a change of `CREDITS.md` needs a new owneet-base.
   **Closed** (2026-11-13): the owner's look: the two authors shown at the top of the console's credits (owneet-base 0.0.71).
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
   **Closed** (2026-11-13): the owner's choice: nothing to do, a slow disk stays slow.
7. **Waking the console with Guide** (6.10): the owner said "let's try"; the test with the dongle to
   prepare. [[step-6.10-waking-the-console-with-the-controller]]
   **Owner (2026-11-13):** see whether it is feasible without too much work: assessment given to the owner the same day.
   **Owner (2026-11-13): prepare the test.** owneet-base 0.0.72's test log with `owneet.debug.bt_wake=on` (added to
   `owneet-debug.txt` on OWNEETLOG) ([[step-6.10-waking-the-console-with-the-controller]]). Waits for the owner's test:
   sleep, then Guide.
   **Owner's test (2026-11-13 15:23, log `owneet-20261113-152306`): it did not wake.** But the test had set nothing: no
   `.wake.txt`; the test log tried once at its start, when BlueZ did not answer yet, and would have tried again only
   after its first report (about two minutes), while the console went to sleep 25 s after the start (sleep 15:23:33,
   woken 15:24:24 by other means). **owneet-base 0.0.73:** the test runs on its own as soon as BlueZ has its
   adapter (at most a minute) and writes what it did or why not; checked in the test VM (no adapter there: the
   message written after a minute). On OWNEETLOG; to try again: wait a minute on the home screen before sleep.
   **Owner's second try (2026-11-13 15:49, log `owneet-20261113-154908`, owneet-base 0.0.73): not woken; again nothing
   set** (no `.wake.txt`): the test came after the start's other work (the previous starts' journals, the minute's
   wait), minutes on the FrankenPC, and the console slept at 15:51:21. Reproduced in the test VM with a real restart.
   **owneet-base 0.0.74:** the test right after the journal starts; checked in the test VM with a real restart (the
   file at once). On OWNEETLOG. The adapter has not been tried yet.
   **Owner's third try (2026-11-13 16:13, log `owneet-20261113-161302`, owneet-base 0.0.74): "the PC restarted by
   itself".** This time the test set everything at 16:13:02 (`.wake.txt`): wakeup enabled on the Bluetooth adapter's
   USB device, its hub and the USB controller (XHC enabled in `/proc/acpi/wakeup`), `WakeAllowed` true on the paired
   Xbox Wireless Controller. Sleep at 16:15:05, **woken at 16:15:16** (11 s later: the owner's Guide, most likely),
   the controller connected again at 16:15:31; the log on the stick stops at 16:15:34 with no shutdown in it. What
   happened then is only in the console's own journal: one more start with the stick (nothing else) brings it
   (`.previous`). Asked the owner what he saw.
   **Owner (2026-11-13): he did not press Guide, and the controller turns off when the console sleeps.** So the PC
   woke by itself 11 s after sleeping, once the test had allowed USB devices to wake it (the first two tries, with
   nothing set, stayed asleep): which device is not known (the FrankenPC has two Bluetooth adapters, on USB ports 1
   and 10, and a USB Wi-Fi stick). **owneet-base 0.0.75:** the test also writes, at the start and after every sleep,
   the USB devices allowed to wake the PC with their wake counts, the last wake's IRQ and the wake sources (checked in
   the test VM). On OWNEETLOG. Next: a start with the stick (it also brings the console's journal of the 16:13 start,
   for the "restart"), a minute, sleep without touching anything, then Guide if it stays asleep.
   **Owner's fourth try (2026-11-13 16:24, log `owneet-20261113-162428`, owneet-base 0.0.75):** the screen went off,
   about ten seconds later the fans and disks stopped, and a fraction of a second later the console came back to the
   home screen as after a normal sleep; the controller had turned off and he turned it on by hand. **From the logs:**
   S3 entered and left in the same instant (16:26:58); no USB device counted the wake, no IRQ, no wake source. The
   FrankenPC has two Bluetooth adapters: the TP-Link UB500 (USB 1-1, RTL8761BU, the paired controller's) and an
   unused Intel one (USB 1-10, 8087:0a2a, with its Wi-Fi card), which failed a command as the console went to sleep
   (`hci1: Opcode 0x0c24 failed: -112`); the test had allowed both to wake the PC. **owneet-base 0.0.76:** only the
   adapters with a paired device (and the USB devices above them) may wake the PC; the others are kept from it. On
   OWNEETLOG. **Disk check (16:24 listings):** nothing new (packages' cache 192 files).
   **Owner's fifth try (2026-11-13 16:33, log `owneet-20261113-163350`, owneet-base 0.0.76): no change**, woken the
   instant it slept (16:36:11), with only the TP-Link adapter (1-1), its hub and XHC allowed and the Intel adapter
   (1-10) kept from waking it; the Intel adapter still failed its command as the console went to sleep. Left: the
   Intel adapter dropping off the bus (a change the hub wakes for), or the TP-Link adapter waking at once (known of
   some Realtek adapters). **owneet-base 0.0.77, in stages, one per wake:** stage 1 the unused adapters switched off
   in BlueZ; stage 2 their USB devices taken off the bus; stage 3 the adapter in use kept from waking too (if it still
   wakes, the cause is not Bluetooth). On OWNEETLOG. **Disk check (16:33 listings):** nothing new (193 packages).
   **Owner's sixth try (2026-11-13 16:51, log `owneet-20261113-165112`, owneet-base 0.0.77): it stayed asleep only at
   stage 3, and then the controller could not wake it** (as expected). Stage 1 (the Intel adapter off) and stage 2
   (taken off the bus) still woke at once (16:53:35, 16:54:02); stage 3 (the TP-Link adapter kept from waking) slept
   until the power button (16:56:03). **Found:** the TP-Link UB500 (Realtek RTL8761BU) wakes the PC the instant it
   sleeps whenever it is allowed to; no wake source records it. Feasibility on this hardware: not with little work
   (the adapter's own behaviour). The test left the Intel adapter switched off in BlueZ (stage 1, kept by BlueZ) and
   `WakeAllowed` on the controller. **Disk check (16:51 listings):** nothing new. The owner decides how to go on.
   **Owner (2026-11-13): moved to Wave 2** ([[wave-2]] 22); restore what the test left (the controller, BlueZ, the
   built-in adapter): owneet-base 0.0.78 with `owneet.debug.bt_wake=restore` (set on OWNEETLOG) switches every adapter
   on and allows no paired device to wake the PC, at the next start with the stick (checked in the test VM).
   **Closed** (2026-11-13): moved to Wave 2; the restore waits for the next start with the stick (then the switch is
   taken off the stick).
2. **"Resume with the pointer" in the library**: missing there. Demo first.
   [[step-6.8-games-on-disk-delete-and-progress]]
   **Demo** `design/demos/3.7c-library-resume-pointer.html` (2026-11-13; today the library's Options on the running
   game offer "Play, Details, Move, Favorite"): Options on the running game offer what the home screen's card offers,
   "Resume" first (instead of "Play"), then "Resume with the pointer" ("Turn the pointer off" while it is on), then the
   usual options; the pointer's help the first time, as from the home screen. Two extras, off unless the owner wants
   them: "Close game" in Options too; on the library's cover the "Running" badge and A = "Resume" in the prompt bar, as
   on the home screen. Waits for the owner's approval.
   **Owner (2026-11-13): approved; "Close game" added too (with the home screen's question, Cancel selected); the
   cover's badge and A = "Resume" dropped.** Second round of the demo (the same file): Options on the running game
   offer "Resume", "Resume with the pointer", "Close game", then the usual options. Waits for the owner's approval.
   **Owner (2026-11-13): second round approved. Built** (owneet-frontend 0.38.30, `theme.qml` `showOptions`; checked with
   `tools/frontend-preview`, `library-running-options.txt`: Resume, Resume with the pointer, Close game with its
   question, then the usual options; another game keeps Play). The window lays its buttons out as every Options
   window does (in rows that fill its width). On OWNEETLOG; waits for the owner's look.
   **Closed** (2026-11-13): the owner's test (2026-11-13): Resume, Resume with the pointer and Close game in the library's Options.
4. **"Shutting down" screen at once** (7.6b): demo `design/demos/7.6b-shutting-down.html` approved;
   the code is missing. [[boot-experience]]
   **Owner (2026-11-13): go. Built** (owneet-frontend 0.38.31: `PoweringOff.qml`, `powerNow` in `theme.qml` for every
   shutdown and restart, the splash's colours as tokens `Theme.splashLogo` / `splashInk`; checked with
   `tools/frontend-preview`, `shutting-down.txt`). On OWNEETLOG; waits for the owner's look (a shutdown and a restart).
   **Closed** (2026-11-13): the owner's test (2026-11-13): "Shutting down" at once, shutdown and restart.
3ag. **Guide does nothing while nothing runs** (owner, FrankenPC, 2026-11-14): the Home button does nothing unless Steam
   is open. **Owner's fix (2026-11-14, no demo):** while Steam, a media app or a game runs, the Home prompt leaves the
   prompt bar; otherwise Guide really goes back to the home screen. **Built** (owneet-frontend 0.38.33: `guideHome()`
   on owneetd's `home.requested` closes the windows over the pages and goes to the Home section; `Nav.homePrompt` follows
   the running apps; [[controller-input-map]]); checked with `tools/frontend-preview` (`guide-home.txt`). On OWNEETLOG;
   waits for the owner's test.
   **Closed** (2026-11-17): the owner's test (2026-11-17): Guide goes back to the home screen; and, asked by the owner, no Home prompt on the home screen itself (owneet-frontend 0.38.35).
3ah. **A cut cover in the library's grid, and the navigation goes wrong** (owner, FrankenPC, 2026-11-14): left of
   Borderlands 2 a game's cover is cut (the screen left on for more than 30 s: in the test log's screenshots); while
   the covers sit like that, moving between them goes wrong. **To reproduce (owner):** filter "All", the first game
   selected, RT twice, then LT back to "All". **Owner (2026-11-14): first in the list of fixes; not to be started
   before his next message.**
   **Looked at (2026-11-17, log `owneet-20261114-134014`):** library sorted by name, 89 games, 4 favourites; the
   screenshots show the selected cover drawn at the left of a row, one column before the first, one row below its
   place (the game before Borderlands 2), and the grid scrolling around it. Not reproduced in `tools/frontend-preview`
   (new `@manygames`: about ninety invented Steam games, four favourites; `library-filter-shift.txt`; also at
   1366×768 and with the buttons pressed at once). Most likely cause: the grid followed a filter change row by row
   (dozens of moves at once), and GridView misplaces an item there. **Fixed** in owneet-frontend 0.38.34: a new filter
   or sort fills the grid again; only the same list changing is followed row by row (the covers kept after an
   uninstall, 2026-11-08). On OWNEETLOG; waits for the owner's test (the same steps).
   **Closed** (2026-11-17): the owner's test (2026-11-17): the grid stays right after RT, RT, LT, LT (owneet-frontend 0.38.34).
3c. **Removing the originals of single games, the read-only case** (6.6c, confirmed by the owner on
   2026-11-10: the original removed after a copy, with no error; the choice of
   games, item 1 of 2026-11-09, confirmed too): left, a USB disk that Windows left read only, to check
   in the test VM (the owner has no Windows disk). [[step-6.6-moving-games-and-media-between-disks]]
   **Checked in the test VM (2026-11-17):** a USB disk "WINUSB", NTFS with Windows' Fast Startup left on (`hiberfil.sys`
   starting with "hibr"), two games: owneet-mount mounted it read only, reason `windows`. owneetd asked on purpose to
   copy Alpha to the console's disk **and** remove its original (the interface never asks: the column is off): the copy
   done and identical (same SHA-256), the original untouched, owneetd only warned "the original could not be removed
   … read-only file system". Ready to close (the owner's word).
   **Closed** (2026-11-17): the owner's word, after the check in the test VM.
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
   **Disk check (2026-11-13 13:21 listings):** nothing new: 14 Windows prefixes 7.6 GB, Proton's logs 1.5 GB (12), packages'
   cache 188 files, 5 core dumps; Steam's wanted downloads and its shader caches. At 14:06 the owner uninstalled The
   Witcher 2's Windows version and deleted its folder (SATA disk): whether its prefix (`the-witcher-2-win-b264e729e7`)
   went with it (3t (a)) is seen in the next listing.
   **Disk check (2026-11-13 14:41 listings):** that prefix stayed (2.06 GB): expected, 3t (a) (an internal disk's
   Windows game takes its prefix with it) is not built yet; it joins the junk to clean in 3t. Otherwise nothing new:
   14 prefixes 7.6 GB, Proton's logs 1.5 GB, packages' cache 189 files, 5 core dumps; on the SATA disk only The Witcher
   2's Linux version and Steam's library (its wanted downloads grew by about 13 GB).
   **Disk check (2026-11-13 15:23 listings):** cut (no `complete.txt`, the home folder's listing ends early: the
   console went to sleep and was switched off before they ended); the readable part has nothing new (packages' cache
   189 files, 5 core dumps).
   **Disk check (2026-11-13 17:23 listings):** nothing new (packages' cache 196 files: from owneet-base 0.0.79 the
   console keeps two versions of each).
   **Disk check (2026-11-13 19:59 listings, owneet-base 0.0.79):** the packages' cache went from 196 files to 55 (two
   versions of each package: the hook works); 14 prefixes 7.6 GB, Proton's logs 1.4 GB, 5 core dumps; on the SATA disk
   Steam's wanted downloads 39.4 GB, shader caches 6.1 GB, `compatdata` 2.1 GB.
   **Disk check (2026-11-14 13:40 listings):** 13 prefixes 7.3 GB and no Proton logs (the owner deleted them with the
   file manager), packages' cache 55 files, 5 core dumps; SATA disk as before (downloads 40.0 GB).
   **Disk check (2026-11-13 15:49 listings, the console's disk whole, the SATA disk's not made: the console slept
   first):** nothing new: 14 prefixes 7.6 GB, Proton's logs 1.5 GB, packages' cache 190 files, 5 core dumps.
   **Disk check (2026-11-17 14:22 listings, whole):** nothing new: 13 Windows prefixes 7.3 GB (the owner's to clean with
   the file manager), no Proton logs, packages' cache 55 files, the same 5 old core dumps; the SATA disk holds only
   Steam's library, `lost+found` and The Witcher 2 (Linux) with its installer and `.owneet-installed`.
   **Closed** (2026-11-17) with step 6.11 (owner); the disks are still checked after every test.
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
   **Owner (2026-11-13):** a new entry in Settings → "Advanced": a **very simplified file manager**, only to go through
   the folders and delete; Wave 2 adds downloading from the browser, moving the downloaded files, extracting zip
   archives and renaming folders ([[wave-2]] 21). To agree next: how it is shown (proposal to the owner, then a demo),
   which folders it shows, and where it goes in the plan.
   **Owner (2026-11-13):** the proposal (places, a list, Delete with a question) is right; the console cleans its own
   system leftovers by itself (packages' cache: the last 2 versions kept; core dumps); a new step, 6.11, at the end of
   phase 6: [[step-6.11-simplified-file-manager]]. Asked by the owner first: what about Steam's leftovers? (answered
   the same day, waits for his choice).
   **Owner (2026-11-13): all approved** (Steam's leftovers as proposed: a place "Steam's leftovers" with the shader
   caches, Windows data and orphan unfinished downloads of games no longer installed, deleted only with Steam closed;
   downloads still queued cancelled from the console as today; old Proton and runtime left to Steam), **plus a first
   question before deleting Windows data: they may hold saves.** **Demo** `design/demos/6.11-file-manager.html`
   waits for the owner's approval ([[step-6.11-simplified-file-manager]]).
   **Owner (2026-11-13), on the demo: not like that** (a list): a file manager like Windows' or Linux's, folder-shaped
   icons in a grid, in the console's colours; the functions are right. **Second round** of the demo (the same file):
   folders in the console's accent, documents with their kind, a grid, a bar under it with the selected item's size
   and date. Waits for the owner's approval.
   **Owner (2026-11-13): the second round of the demo is approved** ("perfect"). Building it is step 6.11's work:
   waits for the owner's go.
   **Owner (2026-11-13): build it after item 4.** Built in owneet-frontend 0.38.32 (the file manager) and owneet-base
   0.0.79 (the packages' cache and crash dumps cleaned by the console), details in
   [[step-6.11-simplified-file-manager]]; on OWNEETLOG; waits for the owner's test. Left: the prefix removed with a
   Windows game on an internal disk (3t (a)).
   **Owner's test (2026-11-14): all passed** (the file manager, the places, the deletions). Left in step 6.11: the
   prefix removed with a Windows game on an internal disk.
   **3t (a) built (2026-11-17, owneetd 0.25.32):** a game and its installer both gone through the console (its folder
   deleted, or uninstalled once its installer was deleted) take their own folders on the console's disk with them:
   prefix with its saves, DOS data, Windows logs; not while the installer stays, never on a USB disk. Go tests; test
   VM: a game on the VM's internal disk deleted, its three folders gone; the USB stick seen as external (`/sys` path
   through `usb2`). **Asked the owner:** the uninstall question when the installer is gone does not say the saves go
   too (text proposal). Not on OWNEETLOG yet (waits for the text). The prefixes already left on the FrankenPC by
   games deleted before: removed with the file manager ("Game no longer here").
   **Owner (2026-11-17): text approved.** owneet-frontend 0.38.36: uninstalling a Windows or DOS game whose installer
   is gone, on a disk inside the console, says "…, with its saves and settings" (five languages); Storage's volumes
   tell a USB disk (`usb`). On OWNEETLOG with owneetd 0.25.32. Step 6.11 all built: waits for the owner's approval.
   **Closed** (2026-11-17): the owner closes step 6.11.
3ai. **The Home prompt on the home screen** (owner, 2026-11-17): there Guide does nothing, so the prompt is to go.
   **Built** (owneet-frontend 0.38.35: `Nav.homePrompt` also false on the home screen while no window is over it;
   [[controller-input-map]]); checked with `tools/frontend-preview` (`guide-home.txt`). On OWNEETLOG. The log of
   2026-11-17 10:09 on the stick lasts 37 s (no disk listings): the disk check waits for the next one.
   **Closed** (2026-11-17): the owner's test (FrankenPC, owneet-frontend 0.38.35).
6. **Cover pictures from a disk** (6.9): demo to do. [[step-6.9-cover-images-from-a-disk]]
   **Demo (2026-11-17):** `design/demos/6.9-cover-images.html`, waits for the owner's approval.
   **Owner (2026-11-17): demo approved** (the sub-folders, the preview as the cover, not on a read-only disk),
   on the condition that moving down in the Options window goes down on the console (it does: the
   console's windows move by place, `Nav.find`; only the demo moved along the list). **Built** in
   owneet-frontend 0.38.37, checked in the preview (`tools/preview-steps/cover-images.txt`); on
   OWNEETLOG, waits for the owner's test. Open: WebP needs `qt5-imageformats` (owner's decision).
   **Owner (2026-11-17): WebP left out; covers at most 1200 px on their longest side** (a bigger picture saved
   smaller). Built in owneet-frontend 0.38.38, on OWNEETLOG; waits for the owner's test.
   **Owner's test (2026-11-17): the option did not show** (two pictures in `Images` on OWNEETLOG). Cause: the testers'
   stick is never one of the user's disks (the disks' udev rule and owneet-mount leave it alone; owneet-testlog mounts
   it at `/run/owneet-testlog`), so the console finds no pictures there, as built; the test instructions were wrong to
   name it. One of the two files also has no extension (a JPEG): only `.png`, `.jpg` and `.jpeg` are listed. To test
   again with another stick or disk, together with 3b (owner).
   **Owner's test (2026-11-17), again: passed.** **Closed** (2026-11-17) with step 6.9.
3b. **Wine's own programs followed as the game's** (found in the owner's test log, 2026-11-09 21:50): the
   home screen at the game's end waited for `C:\windows\system32\explorer.exe` too, because it owns a window;
   there it ended before the game, but it could outlive it until Wine closes. Fix proposed: never count a
   program under `C:\windows` as the game's, even with a window. [[step-4.5-windows-games-proton]]
   **Owner (2026-11-13): apply it. Built** (owneetd 0.25.31, `closing.go` `wineProgram`: a window of a program in
   `C:\windows` no longer makes it the game's; test in `TestHomeWhenTheGamesProgramsEnd`). On OWNEETLOG; it shows only
   when such a program outlives the game, so it is checked with the next Windows games.
   **Owner's test (2026-11-17 16:04-16:06, The Witcher 2 for Windows, newly installed on the SATA disk; log
   `owneet-20261117-154734`):** owneetd followed only the game's own programs (`Launcher.exe`, `bin\Configurator.EXE`,
   `bin\witcher2.EXE`), never Wine's `C:\windows` ones (its `explorer.exe` was running); `witcher2.EXE` ended at
   16:06:52.674 and the home screen came at .678. Works: closed on the owner's word.
   **Closed** (2026-11-17): the owner's word, after the test (the Linux version's short start at 15:48 was opened by
   mistake).
8. **"Preparing" with a percentage for Steam downloads**: nice to have in Wave 1 if easy; demo first.
   [[step-4.2c-steam-without-its-interface]]
   **Found (2026-11-17):** Steam's content log names each phase before a download (Reconfiguring, Verifying Installed,
   Preallocating, the shader cache) but never how far it is; the sizes come only when the download begins. Another way
   would be Steam's internal state or undocumented APIs ([[legal]]: no). On FrankenPC these phases lasted 1-17 s (Arkham
   Knight: 13 s + 1 s); the minute of "Waiting" seen on 2026-11-09 was almost surely the fault fixed in owneetd 0.25.5. Left:
   while Steam prepares, owneetd says "queued", so the cover reads "Waiting" as for a game in line.
   **Owner (2026-11-17): proposal agreed:** a state "preparing" in owneetd; the cover "Preparing…" with the moving bar of
   Windows installers (no percentage); Details the same bar, without downloaded, speed and time left; "Waiting" only for
   a game in line or a download Steam paused. **Demo** `design/demos/4.2c-steam-preparing.html` (also Home's notice,
   "Preparing {title}…" instead of "Downloading {title} · 0%"): waits for the owner's approval.
   **Owner (2026-11-17): demo approved, Home's notice included. Built:** owneetd 0.25.33 tells "preparing" for a new
   game Steam prepares (`steamlib.go`; "Stopping" no longer read as preparing, `steamprogress.go`; Go tests);
   owneet-frontend 0.38.39: the cover, Details (moving bar, no downloaded / speed / time left), Home's notice, Options
   can cancel it; texts in five languages. Checked with `tools/frontend-preview` (`steam-preparing.txt`, with
   `@steamprepare`; and the change to "Downloading · %"). On OWNEETLOG: waits for the owner's test (a Steam game
   installed: "Preparing…" for the first seconds, then "Downloading · %"). Found on the way: the update test
   `TestCheckThenApply` failed once (its fake wrote the state file in place; it now writes it as owneet-update does,
   300 runs passed); the preview steps `library-steam.txt` stopped at the notice "Before Steam opens", added after them: rewritten
   for today's interface (owner, 2026-11-17), every shot checked.
   **Owner's test (2026-11-17 18:22, FrankenPC): passed.** Steam's log: Silksong (1030300) prepared from 18:25:43 to
   18:25:50, then downloaded. Disk check of the same log: nothing new (no Windows data left, packages' cache 55 files,
   the 5 old core dumps, Steam's wanted downloads).
   **Closed** (2026-11-18): the owner's test.
14a. **BioShock's controls and the controller pointer's click** (part of [[open-items]] 14, owner, 2026-11-19): BioShock
   (Steam) did not take the controller, Steam's keyboard-and-mouse layouts made every button open its quit menu, and the
   console's pointer could move but not click in it. **Causes:** the game's own controller option was off
   (`Bioshock.ini`: `UseController=False`, `UseJoystick=False`; it supports the Xbox 360 controller once turned on in its
   options); the pointer's click was the button down and up in the same instant, never seen by the game's menu. The
   owner turned the option on with a real mouse: the game works perfectly with the controller. **Built:** owneetd 0.25.47,
   A and X hold the mouse's buttons as long as they are held ([[controller-input-map]]). Proton's Xalia was ruled out
   (switch `steam_xalia=off`, no change). History in [[open-items]] 14.
   **Closed** (2026-11-19): the owner's test, the pointer clicks in BioShock's menu.
15. **The library's disks not updated when a disk is taken out** (owner, 2026-11-19): after taking the external SSD out,
   the library still showed 3 disks until he went to Home and back. **Cause (code):** the disks in the library's header
   are read when the library is shown (`LibraryPage.refreshVolumes`); a disk plugged in or out read the games again
   (`checkDisks`, "Disks changed: reading the games again, quietly" at 21:18:53) but not the header. **Built:**
   owneet-frontend 0.38.43, the header read again on every change of the disks too. Other users: only that header.
   Seen in the log: the SSD was taken out while mounted, and the kernel reported writes it could not finish
   (21:18:52, "device offline error … WRITE", ext4 journal aborted). On OWNEETLOG: to test.
   **Closed** (2026-11-20): the owner's test passed.
3af. **A test of owneetd failed once** (2026-11-13, while building owneetd 0.25.31): `TestStopAndSourceGone`
   (`daemon/internal/installs`) timed out (5 s) waiting for an event during the package's build; the next build
   passed, and 80 more runs (with and without the race detector) did not fail. A test that fails by chance: its
   cause to be found (assistant).
   **Owner (2026-11-17):** if it does not come back by the end of the tests, it is closed (users would open a ticket).
   **Closed** (2026-11-20): dropped by the owner (it never came back).
13a. **Cyberpunk 2077 (from item 13: Steam games with their publisher's launcher)** (owner, 2026-11-18): the owner installs games for a batch of tests
   and expects problems above all with external launchers: EA (STAR WARS Jedi: Fallen Order), Rockstar (Red Dead
   Redemption 2), CD Projekt Red (Cyberpunk 2077, with item 10) and Ubisoft (Assassin's Creed Unity, not bought yet: later).
   Launchers made for a mouse are driven with the controller pointer ([[controller-input-map]]). What fails is
   recorded here per game after the test. [[step-4.2c-steam-without-its-interface]]
   **Owner's test (2026-11-18), Cyberpunk 2077: failed.** No Steam question at launch this time; the game never
   started, not once: only its launcher (REDlauncher) was seen. **From the log** (`owneet-20261118-175931`, FrankenPC,
   GeForce GTX 1660 SUPER, NVIDIA driver): two starts (18:03:34, 18:05:04), both through `REDprelauncher.exe`. First:
   the prelauncher's window at 18:04:02; between it and the launcher's window (18:04:28) Steam's own window was on screen
   for 14 s (no game window: owneetd shows Steam); at 18:04:47 a shader of the game itself was being compiled
   (vkd3d-proton's "Unsupported: … extractelement" from Steam's children), and at 18:04:48 every process of the game
   ended, Steam saying "success". Second: launcher at 18:05:12, game at 18:05:22, all ended at 18:05:24. So the game
   itself most likely starts and dies within a second. Not in the log: why. Proton's own log is written only for the
   console's Windows games (`owneet.debug.windows_log`), not for Steam's: proposal to the owner, the same testers' switch
   for Steam's games too.
   **Owner (2026-11-18): approved; he pressed "Play" in the launcher with the controller.** Built: owneetd 0.25.34 starts
   Steam with `PROTON_LOG=1` and `PROTON_LOG_DIR=/tmp/owneet-proton-logs` when `owneet.debug.windows_log=on` (in memory:
   nothing stays on the disk); owneet-base 0.0.80's test log copies each `steam-APPID.log` to the stick
   (`<log>.games/proton-steam-APPID.log`). On OWNEETLOG: Cyberpunk 2077 to start again, then its log.
   **Owner's test (2026-11-18, owneetd 0.25.34):** (a) Cyberpunk 2077 started from the console with Steam closed: it
   stayed on the console's "Starting …" screen; it seemed Steam's Vulkan shader processing had not even begun (owner not
   sure). (b) Started again from Steam itself: the Vulkan shaders were processed, starting at once at 89% (maybe begun the
   first time and cut off); then an abrupt return to the console's home screen; then the launcher came, "Play" pressed
   with the controller; the game started and closed after a few seconds. (c) STAR WARS Jedi: Fallen Order (the only one
   the owner can try now): the same as Cyberpunk at its first try; back on the home screen, Steam opened again asked to
   choose a folder or a file, for what the owner could not tell (the EA app's install?); he closed Steam and switched the
   console off. Logs on OWNEETLOG: to read.
   **From the log (`owneet-20261118-182054`):** one launch of Cyberpunk, not two (the owner opened Steam meanwhile).
   (1) **Cyberpunk 2077 closing: not ours.** Proton's log: exception 0xc000001d in NVIDIA's shader compiler
   (`libnvidia-gpucomp.so.615.71.09`, `vkCreateComputePipelines`), a known bug of NVIDIA's driver on Turing cards with
   this game: [[nvidia-turing-shader-compiler-crash-in-vkd3d-games]] (open: a fix waits in vkd3d-proton, it comes with
   a Proton update). (2) **Steam's long preparation shown only as "Starting …":** Steam prepared Cyberpunk's Vulkan
   shaders from 18:22:20 to 18:29:56 (7.5 min) and owneetd kept Steam hidden ("preparing the game's shaders: still
   hidden"), as built for Silksong's 45 s ([[step-4.2c-steam-without-its-interface]]); no progress on screen, so it
   looked stuck. Steam's `shader_log.txt` gives the percentage ("Still replaying 1091500 (69%, 1022/11995)").
   (3) **Jedi: Fallen Order's install script hidden while it waits for the user:** from 18:32:00 Steam ran the game's
   install script (EA's, 4 steps) hidden ("preparing the game: still hidden"); its window, a Windows "Open" file
   dialog on `C:\Program Files` (a Steam window, appid 769), was on screen only when the owner opened Steam
   (18:36). What it asks for is not in the logs: Steam's `installscriptevalutor_log.txt` is not copied by the test
   log, and the game's `__Installer` folder holds only `vc/` and `LOC/` (no EA app installer seen). Proposals to the
   owner.
   **Owner (2026-11-18):** (1) Cyberpunk must not stay without a solution. Found: the fix is NVIDIA's (the vkd3d change
   was refused on 2026-11-02; NVIDIA has a fix, bug 7014466): OwneetOS ships the fixed driver in an update as soon as it
   is out; meanwhile Steam's beta "2.31" of the game is reported to work (saves of a newer version may not open):
   [[nvidia-turing-shader-compiler-crash-in-vkd3d-games]]; told to the owner. (2) **Demo** of the percentage:
   `design/demos/4.2c-steam-shaders.html` ("Steam is preparing the game's graphics: 69%", a bar, "The first time, or
   after an update, it can take a few minutes"; "shaders" never named), waits for the owner's approval. Found on the
   way: item 3v's fix (Steam's own shader page shown when Steam waits on ProcessingShaderCache) no longer happens:
   owneetd keeps Steam hidden while `fossilize_replay` runs (Silksong's rule), so the demo's percentage replaces it.
   (3) **(a) approved, built:** owneetd 0.25.35 shows Steam at once when a window of a game's install script
   (`reaper SteamLaunch AppId=N Install=1`) comes on screen while Steam is hidden (Go tests). (b) (the install
   script's log on the stick) not approved: not built.
   **Owner (2026-11-18): when does the fix come out? Without a date we rely on chance.** Checked: NVIDIA gives no date
   (its forum thread has no NVIDIA reply; bug 7014466 named only in vkd3d-proton's issue). Linux drivers out: 615.78.08,
   620.70.06 (in Arch since 2026-11-13; still reported broken), 620.73.04 (2026-11-17, "minor bug fixes", not in Arch
   yet, unknown whether it holds the fix). Our pinned packages: nvidia 615.71.09 (snapshot 2026-10-13). Ways that do
   not depend on chance, told to the owner: Steam's beta 2.31 now; each new NVIDIA driver tried on the FrankenPC
   through the update stick; or a fix of our own (the console repairs the failing shader on the PC itself), heavy.
   **Owner (2026-11-18): demo `4.2c-steam-shaders` approved; 3(a) confirmed.** The approach to Cyberpunk is not
   accepted: see item 14.
   **Closed** (2026-11-20): dropped by the owner: a fault of NVIDIA's driver on that card (Turing), not of OwneetOS
   ([[nvidia-turing-shader-compiler-crash-in-vkd3d-games]]); the rest of item 13 stays open.
10. Cyberpunk 2077: Steam's question at launch shown at once. [[step-4.2c-steam-without-its-interface]]
    **Owner (2026-11-18):** tested in the batch with 13; nothing to build (owneetd 0.25.6 shows Steam as soon as its log
    says it waits for the user).
    **Closed** (2026-11-20): dropped by the owner with Cyberpunk 2077's tests.
12. "Playing for" over an hour on the home screen ("1 h 5 min", "2 h"). [[step-4.2c-steam-without-its-interface]]
    **Owner (2026-11-18):** tested in the batch with 10 and 13: a game left open over an hour, then Guide.
    **Closed** (2026-11-20): the owner's test passed (a game open over an hour).
16. **Dota 2 not in the console's library while it downloads** (owner, 2026-11-21): Steam's library shows it, its download
   has begun (not "preparing"), but the console's library does not list it. Test log on OWNEETLOG to read.
   **From the logs already on the stick (`owneet-20261120-195103`) and the code:** owneetd sees the download (app 570,
   queued, 1.18 of 114 GB); the interface found "93 games owned (400 apps in the licences)" without it. Dota 2 is in
   package 0, the package every account gets (with Spacewar and Team Fortress 2), which the library leaves out on
   purpose (decided 2026-10-14, [[steam-integration]]: `SteamOwned.cpp`); an installed game comes from Steam's
   manifests, so Dota 2 should show once its download is complete. **Proposal to the owner:** a game of package 0 is
   listed as soon as Steam downloads it or has it installed (never the others of package 0). No new log needed.
   **Owner (2026-11-21): approved** (also Guide on the Videos, Music and Apps pages: back to the home page). Built:
   owneet-frontend 0.39.1 (`SteamOwned.cpp`: a package-0 game with a manifest in one of Steam's libraries is listed).
   **2026-11-22:** Arch's archive back; the merged interface previewed (Home, the Apps, Videos and Music pages: no
   QML error); owneet-frontend 0.39.2 shows the Home prompt on those pages (Guide works there). On OWNEETLOG: to test.
   **Closed** (2026-11-22): the owner's test passed (Dota 2 in the library and running).
17. **Danidepadawan's web apps cannot be installed on the FrankenPC** (owner, 2026-11-22, first test of the merged
   packages): every install (Netflix, YouTube, Spotify) fails at once. **From the log (`owneet-20261122-094913`):**
   `owneet-apps-install@brave` exits 1 within 35 ms; the console has no `/usr/share/owneet/bundled/` (the offline
   repository with Brave that the ISO build adds, step 5.0.0): the FrankenPC was installed from an ISO older than
   phase 5, and the update stick brings packages only. Not a fault of the merged code. **Ways, for the owner:** (A) the
   update stick also carries the bundle (Brave from `out/repo`), copied by `owneet-update` into
   `/usr/share/owneet/bundled/` on a tester system that has none; (B) the FrankenPC installed again from a new ISO
   (the console's disk erased). Also seen: the interface's version is not shown in Settings (my wrong instruction).
   **Owner (2026-11-22): A.** Built: owneet-base 0.0.84 (`owneet-update` copies the stick's bundle into
   `/usr/share/owneet/bundled/` when missing or different, at start-up or from Settings, even with no package to
   install), `tools/update-extras` makes the bundle as the ISO build does (brave-bin, 194 MB), `tools/make-update-stick`
   copies it. On OWNEETLOG: the first start installs 0.0.84, the second copies the bundle; then a web app.
   **Owner's test (2026-11-22): passed** (Netflix and Spotify installed and opened, log `owneet-20261122-183607`).
   **Closed** (2026-11-22): the owner's test passed (web apps installed from the bundle).
18. **Beneath a Steel Sky never started after Apex Legends** (owner, 2026-11-22): Dota 2 runs; Apex Legends does not start
   (Steam says SteamOS does not support it: EA blocked Linux and the Steam Deck in October 2024, [[game-test-matrix]],
   expected, for step 4.8); Beneath a Steel Sky (GOG, Linux) stayed on "Starting…". **From the log
   (`owneet-20261122-183607`) and the code:** Apex was asked for at 19:00:37 and Steam never launched it (its window
   "Starting…" until 19:12, no `app.started`); the interface starts one game at a time (`ApiObject`) and waits for the
   one it started to end, which never came: Beneath a Steel Sky's start was ignored without a word (no "Starting through
   owneetd" line). **Built:** owneet-frontend 0.39.3, a new game takes the place of a Steam game that has not started;
   started games and games on disks as before. On OWNEETLOG: Apex, then Beneath a Steel Sky (its first start in the
   Steam Runtime, step 3). Disk check: nothing new but Steam's sniper runtime (Dota 2) and the web apps' caches.
   **Owner's test (2026-11-22 19:33, owneet-frontend 0.39.3):** Apex showed Steam's window saying SteamOS does not
   support it; closed from the console (19:34:44). **The fix works:** Beneath a Steel Sky started at 19:34:51, in the Steam
   Runtime (scout), but ended at once: GOG's `scummvm/start.sh` sets `LD_LIBRARY_PATH` to its own `libs/x86_64` only, so
   the runtime's libraries are gone and ScummVM misses `libjpeg.so.8` (the scout runtime has it: read on the development
   PC's Steam). With the system's libraries (the old way) Arch provides it. Any native game whose script replaces
   `LD_LIBRARY_PATH` loses the runtime the same way. Ways proposed to the owner. Then **the FrankenPC froze** (item 19).
   **Owner (2026-11-22): way A.** Built: owneetd 0.26.1, inside the runtime the game's bash scripts get a `BASH_ENV`
   (`owneet-runtime-bashenv`) whose `export` puts the runtime's folders back at the end of `LD_LIBRARY_PATH` when a
   script removed them; the game's own libraries still first. Builder VM: a GOG-like script found `libjpeg.so.8` in the
   runtime; without the runtime nothing changes. The Witcher 2 starts its programs directly (no bash script): not
   affected. On OWNEETLOG: Beneath a Steel Sky, then The Witcher 2 (Linux) to check nothing changed. Apex's window
   ("SteamOS does not support it") is the game's own: EA blocks Linux and SteamOS; the console does not make it.
   **Owner's test (2026-11-22 19:53): passed.** Beneath a Steel Sky and The Witcher 2 (Linux) start (twice each); Apex
   still does not, as expected. Seen: Apex's own program (EA's) went on after Beneath a Steel Sky took its place, until
   the owner ended it (19:57:07): the console lets go of the launch but does not close what Steam had started; the
   owner accepts it. Powering off from Steam's own menu works (owner: not a fault).
   **Closed** (2026-11-22): the owner's test passed.

21. **The Fractured But Whole: Ubisoft Connect stays after the game** (owner, 2026-11-22): the game quit, yet the
   console still offered Resume / Resume with the pointer / Close. **From the log:** the game (`SouthPark_TFBW.exe`)
   was quit at about 20:20:37; Ubisoft Connect (`upc.exe`, `UplayService.exe`, `UplayWebCore.exe`) stayed, so Steam
   kept the game running (`steam:488790`) until the power-off at 20:21:41: the console shows what Steam says. Known on
   SteamOS too; closing Ubisoft Connect at once may cut its cloud-save sync (ProtonDB). Ways to weigh with the owner.
   **Owner (2026-11-22): try it.** Built: owneetd 0.26.2 closes the game when only the launcher is left (`upc.exe`,
   `UplayService.exe`, `UplayWebCore.exe`, `UplayCrashReporter.exe`), the game's own programs having run with a window,
   and nothing of it on screen, as Proton's proposed fix does (ValveSoftware/Proton pull request 10356, not merged:
   cloud saves sync while a window shows). Go tests. On OWNEETLOG: The Fractured But Whole, then (owner) Red Dead
   Redemption 2, STAR WARS Jedi: Fallen Order and Cyberpunk 2077 (its working beta) to check their launchers.
   **Owner's test (2026-11-23):** the first two launches did not start; the third did; quitting closed everything
   and the console came home, **but Ubisoft's cloud save failed**. **From the log (`owneet-20261123-091932`):** first
   launch 09:19:59: Steam ran the game's install script (4 steps) from 09:20:15; its window appeared at 09:20:27 (the
   pointer on) and was gone by 09:23 (only Steam's home mapped); the second launch, from Steam's page at 09:29, waited
   on the same script ("Starting…"); it ended at 09:37:09, after Paladins was started; the third launch's script took
   1 s and the game ran from 09:39:28. Why the script waited 16 minutes is not in the logs (Steam's install-script log
   is not copied: [[open-items]] 13 (b), not approved). The game was quit at about 09:41:49 and owneetd closed Ubisoft
   Connect at 09:41:50, one second later: most likely before its cloud sync (hypothesis; when the failure message
   appeared: asked to the owner).
   **Owner (2026-11-23):** the failure showed in a Ubisoft window after the game closed; copying the logs approved.
   Built: owneet-base 0.0.85 copies Ubisoft Connect's own logs (`<log>.games/ubisoft/APPID/`) and Steam's install
   script logs (`installscript*_log*.txt`); owneetd 0.26.3 has the testers' switch `owneet.debug.launcher_close=off`
   (the launcher left alone after the game). On OWNEETLOG with the switch on (to remove after the test): The Fractured
   But Whole played and quit, Ubisoft Connect left to sync, then closed from the console: its log says when the sync
   ends, to close it on that event instead of at once.
   **Owner's test (2026-11-23, 10:45):** the first launch had to be closed from the console (the testers' switch left
   Ubisoft Connect running, as meant); the second launch, right after, did not start ("NOT OK"). **From the log
   (`owneet-20261123-104214`):** game played 10:47:12-10:48:47; Ubisoft Connect showed its window 10:48:48-10:49:05
   (no cloud-save line in its log this time, no error), then no window: owneetd left it alone (switch), closed from
   the console at 10:50:08. The second launch stuck at Steam's install script (10:50:22 until Steam closed at 10:52):
   owneetd had paused Proton's Xalia for a script window gone within seconds, and the script does not end while Xalia
   is paused; the same explains the stuck launches at 09:20 (16 minutes, ended 11 s after Xalia went on), 10:18 and
   10:50: our fault ([[steam-install-script-stuck-with-xalia-paused]]). Built: owneetd 0.26.4 turns the
   install script's pointer off (Xalia goes on) once none of its windows is on screen. On OWNEETLOG.
   Seen also: Ubisoft Connect's window comes 1 s **after** the game's end; owneetd 0.26.2's rule (close when nothing
   of it is on screen) would have closed it in that second, before the window: most likely why the cloud save failed
   at 09:41 (hypothesis). Proposed to the owner: close the launcher once its window after the game has come and gone,
   or after a limit when none comes; then remove the switch. **Owner (2026-11-23): yes, fix first, then the test.**
   Built: owneetd 0.26.5 ([[steam-integration]]); the switch line removed from OWNEETLOG's `owneet-debug.txt`. To test:
   The Fractured But Whole played and quit (Ubisoft's window, then home by itself, the cloud save fine), then started
   again at once (it must start).
   **Owner's test (2026-11-23, owneetd 0.26.5): first and second launch both fine.** From the log
   (`owneet-20261123-111322`): the install script's pointer went off within 1 s each time (its window gone), the
   game started; after each quit Ubisoft Connect's window came (11:15:58, 11:17:36) and went (11:16:00, 11:17:37),
   then owneetd closed it (11:16:01, 11:17:38) and the console came home; no error in Ubisoft's log. To close: the
   owner's call.
   **Closed** (2026-11-23): the owner's test passed (two launches in a row, Ubisoft Connect closed after its window).

20. **Paladins: stuck at the first text field, the keyboard's text not read** (owner, 2026-11-22). Tyrian 2000 and South
   Park: The Stick of Truth start (passed). **From the log (`owneet-20261122-200648`):** while Steam ran Paladins'
   install script (20:08-20:10) the pointer was on and the console's keyboard opened by itself three times (a text field
   clicked: 20:08:39, 20:08:49, 20:09:09), each time back to the window within 1-4 s, with no typing logged; the game
   then ran (20:10:05-20:11:46; its interface is CoherentUI, Proton started `tabtip.exe`, Windows' touch keyboard), the
   pointer on for 6 s, no keyboard asked for. No screenshot before 20:13 (they started late). Which field, and what
   was done there: asked to the owner.
   **Owner (2026-11-22): the field was inside the game, and no keyboard showed.** The console's pointer opens its
   keyboard by itself only when the pointer turns into the text "I" (an X cursor); Paladins draws its own cursor, so
   the field is not seen. Ways with no code, to try first: Y with the pointer on (the console's keyboard, then the text
   is typed into the game, [[controller-input-map]]); Steam's own keyboard (Guide + X, as Steam + X on SteamOS).
   **Owner's test (2026-11-23):** "Resume with the pointer" showed a black screen (09:38:41, the pointer on for
   `steam:444090`); Steam's keyboard typed nothing into the field. Online: no report of this exact fault found
   (ProtonDB, GamingOnLinux); other Proton games lose typed keys in text fields. Open: to look into (Paladins'
   CoherentUI fields under Proton, the black screen with the pointer).
   **From the screenshots (`owneet-20261123-091932`):** at 09:38:17 Steam's own keyboard was open over Paladins'
   "Create your player name" field (the caret in it): Steam showed its keyboard, the game took no letter from it; at
   09:38:51 (after Guide and "Resume with the pointer") the screen was black. Searched online: no report of this exact
   fault; known causes elsewhere are keyboard layouts / input methods (`XMODIFIERS=`) and games that go black when they
   lose the screen (fixed with borderless windowed mode). Nothing of the console touches the keys of a running game
   (owneetd reads Guide only, no grab); not excluded: the session (gamescope's keyboard focus, the "it" layout,
   Steam's XIM failing: "XOpenIM() failed, LANG = C.UTF-8"). Tests proposed to the owner: plain Resume with Steam's
   keyboard, a physical USB keyboard (whether the game takes any key), the game in borderless windowed mode.
   **Owner's test (2026-11-23, afternoon):** a physical USB keyboard types into the game; "Resume with the pointer"
   shows a black screen, and the game stays black even after the pointer is turned off. **From the log
   (`owneet-20261123-111322`):** Guide 11:20:45, back with the pointer 11:20:47, Guide 11:20:53, back without it
   11:20:55, closed 11:21:06; no screenshot in that minute (one every ~40 s). Paladins runs in exclusive full screen:
   at each leave and return DXVK logs "Restoring display mode" then "Setting display mode" (the game leaves and
   retakes the screen); the pointer is not the cause (black without it too). Online: black screens after leaving a
   full-screen game under Proton are reported for other games, worked around with borderless / windowed mode; none
   for Paladins. **Steam's keyboard (hypothesis, to check):** in gamescope Steam types into games through
   gamescope's private input-method protocol, reached on gamescope's Wayland socket; owneetd starts Steam without
   `GAMESCOPE_WAYLAND_DISPLAY` on purpose ([[steam-integration]], 2026-10-11: with it Steam takes over what is on
   screen), so Steam's keyboard may reach no game at all: a class problem, not Paladins'. Physical keys and the
   console's own keyboard (virtual device) do reach games. Asked the owner: Paladins in borderless mode, and a black
   screen left for a minute (screenshot and window list); Steam's keyboard in another game's text field.
   **Owner's test (2026-11-23):** with Paladins in borderless window mode the return works (no black screen); back
   in full screen, black again, with or without the pointer. So the black screen is the game's exclusive full screen.
   **Owner's test (2026-11-23), Steam's keyboard in Dota 2's hero search:** writing showed a "FATAL ERROR" (Dota 2's
   own window), log `owneet-20261123-113756`: "FATAL ERROR: Unable to load layout file
   'file://{resources}/layout/textinput/text_input_daisy.xml'" (Dota 2's own controller text entry, the "daisy
   wheel"). My first reading (the error at the console pointer's click) was wrong: **owner:** it came after trying to
   type with Steam's keyboard. **Repeated (`owneet-20261123-115817`):** Guide + X at 12:11:16 (Steam's chord layout
   loaded), Dota 2's error at 12:11:18, and Steam marked Dota 2 "Files Corrupt" at the same second (content_log):
   Dota 2 asked for its daisy-wheel layout, which it could not load from its files, and told Steam its files are
   damaged. Online: no report of this file. Not known yet whether the file is really missing from this install (a
   download problem) or from Dota 2 itself; Steam's check of the files tells. No screenshot from 12:08 to 12:11 (the
   test log's screenshots paused while Dota 2 loaded: to watch). Test asked: Steam's "Verify integrity of game files"
   for Dota 2, then Guide + X in the hero search again.
   **Owner's test (2026-11-23 13:06, `owneet-20261123-130602`): nothing changed.** Steam verified Dota 2 (13:07-13:14,
   "No Error": its files are whole, the layout is missing from Dota 2 itself). The error came at 13:19:27, **in the same
   instant as the console pointer's click on a text field** (owneetd: "pointer: the keyboard", reason field), before
   any letter; the screenshot at 13:19:17 shows no Steam keyboard. Steam's "chord" layout loads at every Guide press,
   so it does not tell Guide + X. So Dota 2 fails as soon as one of its text fields takes the focus while the
   controller is in use: it opens its own controller text entry, whose layout it no longer has (Dota 2's own fault,
   hypothesis on what makes it choose that entry: Steam in Big Picture). Online: nothing on this file. Dota 2 cannot
   tell whether Steam's keyboard types. Asked the owner: what clicked the field at 12:11 (the pointer, a mouse, or
   nothing: Guide + X alone); the console's keyboard in Paladins in borderless mode.
   **Owner (2026-11-23):** all three give the same error (the console's pointer, a mouse, Guide + X alone): Steam's
   keyboard asked for in Dota 2 also ends in Dota 2's own missing text entry. Next: the console's keyboard in Paladins
   (borderless), first.
   **Owner's test (2026-11-23):** no black screen (borderless), but the name cannot be entered with the console's
   keyboard; only with a physical keyboard plugged in. The console's keyboard did not open by itself at the field's
   click (Paladins draws its own cursor, the pointer never turns into the text "I"). **With Y after clicking the field,
   the console's keyboard opens and the name is typed into Paladins (owner, 2026-11-23): it works.**
   Left: (a) the black screen of games in exclusive full screen when the console comes back to them (borderless avoids
   it; to study whether the console can prevent it for every game); (b) Steam's keyboard reaches no game in this session
   (Paladins: shown, nothing typed; Dota 2: hands it to its own missing text entry): hypothesis, Steam without
   gamescope's Wayland. Which first: the owner's choice. **Owner:** (a) first. (In the test before, "the field gone"
   meant Paladins' name window had closed.)
   **(a), research (2026-11-23):** Valve's Wine (`dlls/winex11.drv`, branch bleeding-edge) under gamescope (window
   manager "steamcompmgr") deactivates the game when its window loses the focus (`focus_out`: foreground to the
   desktop; a game in exclusive full screen then leaves it: DXVK "Restoring display mode"), and ignores FocusIn for
   almost every game (`X11DRV_FocusIn` returns early with `use_take_focus`; "Gamescope doesn't support WM_TAKE_FOCUS");
   it takes the window back to the front from the root's `_NET_ACTIVE_WINDOW`. Paladins did take the screen back
   (DXVK "Setting display mode" at each return), yet showed black: why is not known. The test log's window list did not
   show `_NET_ACTIVE_WINDOW`, `WM_STATE` or hidden windows. Built: owneetd 0.26.6 (owneet-xprobe shows them), on
   OWNEETLOG. Test asked: Paladins back in full screen, Guide, Resume (no pointer), a minute on the black screen.
   Also seen: owneetd tags Paladins' windows with its own app id, gamescope logs "appid clash was 444090 now ..."
   (owneetd's choice, [[owneetd-design]]); whether that matters here is open.
   **Owner's test (2026-11-23 14:49, owneetd 0.26.6, `owneet-20261123-144334`):** during the black screen (14:51:36
   on) Paladins' window was mapped, on top, focused (`GAMESCOPE_FOCUSED_WINDOW`, `_NET_ACTIVE_WINDOW`) and composited
   (`FOCUSED_APP_GFX`): the console and gamescope did their part; the game draws black after leaving and retaking its
   full screen. Valve's Wine: `focus_out` makes the desktop the foreground under gamescope (`ignore_focus_hack`,
   unless `WINE_IGNORE_FOCUS_HACK` is set; then only when gamescope does not list `_NET_ACTIVE_WINDOW` as supported);
   its comment "Gamescope will restore window when attempting to iconify it", skipped for two games only. Hypothesis:
   Paladins, iconified and restored at once, stays black. Proposed to the owner: (A) testers' switch for Steam games
   with `WINE_IGNORE_FOCUS_HACK=0` (and the probe showing `_NET_SUPPORTED`); (B) if not enough, the home shown over
   the game without taking its focus, as SteamOS's Steam menu (big change: the game's controller input while the home
   is shown, [[controller-input-map]] guard to weigh; demo first).
   **Owner (2026-11-23): A; B rejected** ("too drastic, it would break everything else"). Built: owneetd 0.26.7, testers'
   switch `owneet.debug.wine_focus_hack=off` (Steam's games started with `WINE_IGNORE_FOCUS_HACK=0`; to remove after the
   test) and the probe shows `_NET_SUPPORTED`; on OWNEETLOG with the switch on. Test: Paladins in full screen, Guide,
   Resume, a minute if black.
   **Owner's test (2026-11-23 15:23, `owneet-20261123-152245`): nothing changed** (switch on: "Wine's gamescope focus
   handling off" in the journal). gamescope lists `_NET_ACTIVE_WINDOW` in `_NET_SUPPORTED`, so with the switch Wine
   follows gamescope's active window, which becomes the console's when the home is in front: the game is deactivated
   either way while the home takes the screen. Switch removed from OWNEETLOG. (Paladins' Proton log not copied this
   time; only two screenshots in the session.) Next idea, hypothesis to research before any build: on SteamOS the games
   draw through gamescope's own Vulkan layer (WSI, reached on gamescope's Wayland socket), here not, because Steam (and
   so its games) gets no `GAMESCOPE_WAYLAND_DISPLAY`: the same root suspected for Steam's keyboard (b).
   **Owner (2026-11-23):** research it; **borderless window mode as the answer for the games that need it is not
   approved**: the console must make exclusive full screen games come back.
   **Research (2026-11-23), gamescope's WSI layer** (`layer/VkLayer_FROG_gamescope_wsi.cpp` and its json, gamescope
   master): the Vulkan loader turns it on with `ENABLE_GAMESCOPE_WSI=1`; the layer itself works only when
   `GAMESCOPE_WAYLAND_DISPLAY` names gamescope's socket (no default; `isRunningUnderGamescope`), and then presents a
   game's X11 window straight to gamescope ("XWayland Bypass", `gamescope_swapchain` protocol) instead of through
   Xwayland. Steam's games here have no `GAMESCOPE_WAYLAND_DISPLAY` (owneetd removes it from Steam on purpose,
   2026-10-11), so the layer is off for them. Our socket: `gamescope-0` (journal). Whether the bypass ends the black
   screen is not known: test asked with Paladins' own Steam launch options
   `ENABLE_GAMESCOPE_WSI=1 GAMESCOPE_WAYLAND_DISPLAY=gamescope-0 %command%` (testers only, removed after). Only if it
   works: how to give it to every game without giving it to Steam itself (ways to weigh with the owner).
   **Owner (2026-11-23): does not like this approach at the moment**; the WSI test is not done; (a) paused, Dota 2
   (item 23) next.
   **Owner (2026-11-23): Paladins dropped.** Valve rates it "Unsupported" on Steam Deck (GamingOnLinux's database and
   ProtonDB show Valve's rating; not read on Steam's own page). What it showed, to reopen if another game shows it:
   (a) a game in exclusive full screen draws black when the console comes back to it (the console's side checked
   correct; Wine's focus switch changed nothing; gamescope's WSI not tried, owner); (b) Steam's keyboard typed nothing
   into a game (hypothesis: Steam without gamescope's Wayland); the console's keyboard (pointer + Y) works.
   **Closed** (2026-11-23): dropped by the owner.

3. **Netflix / YouTube not silent behind the home screen**: left to Danidepadawan with the web apps
   (owner, 2026-11-09). [[step-4.5-windows-games-proton]]
   **Owner (2026-11-23): not a fault, a feature**: with the video apps playing on behind the home screen, a user can
   listen to music or a podcast while playing. Built: owneet-base 0.0.86, the catalogue no longer marks Netflix and
   YouTube `silentBehindHome` (games still go silent behind the home screen).
   **Closed** (2026-11-23): decided by the owner.

23. **Dota 2: Steam's shader processing stays at 0%** (owner, 2026-11-23): at every start the owner skips it, because
   even after 10 minutes the percentage stays at 0%. To read in the logs (Steam's `shader_log.txt`).
   **From Steam's `shader_log.txt` (2026-11-23):** not stuck. Steam replays Dota 2's Vulkan pipeline cache
   (`fossilize_replay`, `shadercache/570/fozpipelinesv6`): about **2.15 million** pipelines; 11:39-11:44 it reached
   4 255, 12:06-12:09 12 538, 13:15-13:17 again (about 15-100 a second): a few hours in all, so the percentage rounds to
   0%. Each skip ends the replay ("exit code -10 … Considering it killed"); whether the work done is kept is not clear.
   The replay ran only at launches, not while the console was idle. Steam's own process, not the console's; reported
   elsewhere as hours long. Skipping is harmless (the game prepares its shaders while playing). Ideas for the owner:
   Steam's background processing while the console is idle; the approved shader demo (`4.2c-steam-shaders`, real
   numbers instead of 0%); Steam's undocumented `unShaderBackgroundProcessingThreads` not proposed (Valve's internal
   debug setting).
   **Owner (2026-11-23): both** (Steam's background processing while idle, and the approved shader demo built), after
   cleaning open-items of what moved to Wave 2.
   **Before building (2026-11-23):** (A) Steam's "Allow background processing of Vulkan shaders" (Settings →
   Downloads) is not documented and its key in Steam's files was not found online; owneetd already writes Steam's
   `config.vdf` for the compatibility tool, so it can, once the key is known; the processing needs Steam open while the
   console is idle. Asked the owner to look at the setting on the FrankenPC; to find the key, the test log could copy
   only the lines naming shaders from Steam's config files (no account data). (B) The approved demo (2026-11-18) shows
   a percentage (Dota 2: 0% for hours), says "a few minutes" and has no way to skip (today Steam's own page has Skip):
   it does not fit Dota 2; a revised demo (real numbers, the time left, a way to start at once) proposed to the owner
   before any code ([[demo-before-code]], no change to an approved look without the owner).
   **Owner (2026-11-23):** (A) the option does not exist in the Steam the console shows (my claim was not checked: it is
   in Steam's desktop interface, reported missing from the controller interface on Steam Deck too); A parked. (B) go:
   revised demo being made.
   **Revised demo made (2026-11-23):** `design/demos/4.2c-steam-shaders.html` (code `87d192e`): real numbers with the
   percentage, the time left, a long-wait line, X "Start now", B hides. Waits for the owner's approval; then X on this
   screen goes into [[controller-input-map]] before any code, and how owneetd starts the game at once (as Steam's Skip)
   is checked first.
   **Owner (2026-11-23): demo deleted, item dropped**: the player sees Steam's own page with its real controls; the
   console's own screen would only make things harder.
   **Closed** (2026-11-23): dropped by the owner.

9. **GitHub pages with every website update**: README, the repositories' description and topics; the
   text is prepared here, the owner publishes it. [[website]]
   **Prepared (2026-11-18):** the code's README follows the website (its description, slogan, features and
   requirements; status "almost here"; the website's address; no vault link, which does not work on GitHub; the folders
   as they are; the trademark note), committed on `feature/phase7`. The website's README: its Structure section names
   today's components (play-tour, guide-drawing, rich-text; no console-screen), not committed yet (which branch: the
   owner's). Both repositories' description and topics: in [[website]]. Waits for the owner.
   **Owner (2026-11-23): closed**; the update of the GitHub pages is a standing routine of every website update, written
   in [[website]].
   **Closed** (2026-11-23): moved to the website's note as a routine (owner).

19. **The FrankenPC froze, inputs ignored** (owner, 2026-11-22, right after Apex's window and Beneath a Steel Sky's
   failed start): switched off by hand. The session's log on the stick stops at 19:35:18 (Steam's update check, nothing
   wrong before it); the whole journal of that boot comes with the next start with OWNEETLOG (`.previous`).
   **From that journal (`owneet-20261122-195300.previous`, boot -2):** the system was running: after Beneath a Steel Sky
   ended (19:34:57) nothing was logged until the stick was pulled out at 19:35:37 (FAT write errors: that session's
   screenshots and games folder were lost), and the power button shut it down cleanly at 19:37:00. So the interface,
   not the PC, stopped answering for about 40 s; no error says why. Tried in the preview (a disk game that ends at once
   without a window): the interface kept answering. Not seen again in the next session. **To watch:** if it happens
   again, leave the stick in until the console is off (the screenshots show what was on screen).
   **Closed** (2026-11-23): not seen again in the sessions of 2026-11-22 and 2026-11-23 (owner); reopened if it happens
   again.

22. **Steam has network problems, the console does not** (owner, 2026-11-23, starting The Fractured But Whole for item
   21's test): the console is online, Steam says it is not. Logs to read (Steam's `console_log.txt`, `bootstrap_log.txt`).
   **Owner:** no message, only an exclamation mark on Steam's Wi-Fi icon, and not every time. Not found online for
   this exact sign (Steam's network indicator outside SteamOS). To read in the next log: NetworkManager's connectivity
   and Wi-Fi in the journal at those moments, Steam's own logs.
   **From the logs (`owneet-20261123-091932`, `owneet-20261123-100208`):** the Wi-Fi drops. The FrankenPC uses its USB
   Realtek RTL8822BU adapter (`rtw88_8822bu`, `wlp0s20f0u2`; the board's Intel 7265 is not used): 64 "beacon loss"
   events and 6 reconnections in 25 minutes (10:02-10:27), and many on 2026-11-23 at 09:21-09:41. Downloads resume after
   a drop, a launch does not: at 10:17:47 the Wi-Fi dropped while the game started; Ubisoft's game starter could not
   get the account from Steam (10:17:53, "Failed receive local steam response for account"), the game closed (10:18:17),
   Ubisoft Connect started again and waited until the power-off. On 2026-11-23 at 09:41 Ubisoft's request to its servers
   failed during a drop (09:41:44, "Http status code is none"), before owneetd closed it: the cloud save's failure is at
   least partly the Wi-Fi's. No driver error (no "failed to leave lps state"). Ways, for the owner: (a) a test with the
   Intel card or a cable, to confirm; (b) Wi-Fi power saving off in NetworkManager (`wifi.powersave = 2`), reported to
   stop beacon losses with Realtek adapters: a change for every console (no battery to save).
   **Closed** (2026-11-23): the drops come from the FrankenPC's USB Realtek Wi-Fi adapter, not from the console; the
   later tests (The Fractured But Whole's cloud save too) went well (owner). Kept for other testers: turning Wi-Fi power
   saving off (`wifi.powersave = 2`) is the known remedy for Realtek beacon losses.

24. **Dota 2 closes with "FATAL ERROR" as soon as a text field takes the focus** (owner, 2026-11-23; was in item 20, see
   [[closed-items]] 20): "Unable to load layout file 'file://{resources}/layout/textinput/text_input_daisy.xml'" (Dota 2's
   own controller text entry); with the console's pointer, a real mouse or Guide + X alike. Steam's check of its files
   found nothing (the layout is missing from Dota 2 itself). Not seen on SteamOS, where Dota 2 is Verified (hypothesis:
   there Steam gives its own keyboard; here Dota 2 falls back to its old one). **Owner (2026-11-23): go on with it.**
   **Research (2026-11-23):** Dota 2's own fault, known to Valve since 2022: ValveSoftware/Dota2-Gameplay issue 3698
   ("Unable to load layout file '…/textinput/text_input_daisy.xml'", with a controller connected, on Windows too, also
   with the Create Lobby window or Steam Link), no reply from Valve, closed by a bot as "not planned" (2026-07-22). On
   Steam Deck Dota 2 asks Steam for its keyboard instead (`steam://open/keyboard`, ValveSoftware/Dota-2 issue 2301),
   so it does not reach the missing layout (hypothesis: it does so when Steam says it runs on a Steam Deck). The only
   lever found is Steam's `-steamdeck`, tried on 2026-11-19 (Steam restarted itself twice and joined the
   `steamdeck_stable` beta by itself) and set aside. Proposed to the owner: Dota 2's text fields as a known limit of the
   game (it plays), or a new `-steamdeck` try.
   **Owner (2026-11-23): way 1, a known limit of the game** (Dota 2 plays; its text fields with a controller close it,
   Valve's fault).
   **Closed** (2026-11-23): known limit, noted in [[game-test-matrix]].

13. **Steam games with their publisher's launcher** (owner, 2026-11-18): EA (STAR WARS Jedi: Fallen Order) and Rockstar
   (Red Dead Redemption 2) work (their tests in item 14); CD Projekt Red (Cyberpunk 2077): **dropped by the owner
   (2026-11-20)**, a fault of NVIDIA's driver on that card, not of OwneetOS ([[closed-items]] 13a,
   [[nvidia-turing-shader-compiler-crash-in-vkd3d-games]]); Ubisoft: South Park: The Fractured But Whole (in place of Assassin's Creed Unity, owner 2026-11-20), when the owner
   has it.
   Demo `4.2c-steam-shaders` dropped (owner, 2026-11-23): Steam's own shader page stays.
   **Owner (2026-11-20):** South Park: The Stick of Truth instead of Assassin's Creed Unity? Checked: its Steam version
   does not use Ubisoft Connect (Ubisoft's support and PCGamingWiki: only non-Steam copies need it), so it would not
   test Ubisoft's launcher; South Park: The Fractured But Whole on Steam does use it. Answer given to the owner.
   **Owner (2026-11-20):** The Fractured But Whole replaces Assassin's Creed Unity for the Ubisoft Connect test (a
   Ubisoft account is needed).
   **Owner (2026-11-23): close 13 and 14 as soon as possible; Cyberpunk 2077 through its beta.** Searched: the branch
   reported to avoid NVIDIA's crash is named `2_31_old` (one user's report in vkd3d-proton issue 4450; Steam's list on
   the FrankenPC tells whether it still exists). Steps given to the owner: Steam → the game's properties → game
   versions and betas → `2_31_old`, then the game started from the console (REDlauncher, Play, quit). Saves made with a
   newer version may not open in the older one. (The Ubisoft test of this item passed: [[closed-items]] 21.)
   **Owner's test (2026-11-23): Cyberpunk 2077 (beta `2_31_old`) works.** Log `owneet-20261123-161037`: install script
   pointer off within 1 s (17:35:07-08), game 17:36:20-17:40:32, ended by itself (REDlauncher did not stay); disk check:
   nothing new. Left before closing 13 (proposed): Red Dead Redemption 2 and STAR WARS Jedi: Fallen Order again, for
   their launchers after the game and their install-script windows after owneetd 0.26.4-0.26.7.
   **Owner (2026-11-23):** both already installed: their installers' windows cannot be shown again; only the launchers
   after the game are tested. (The install-script pointer rule ran at every Steam start since 0.26.4 without harm:
   pointer off within 1 s each time; an installer's window that stays on screen keeps it on, as the unit test covers.)
   [[step-4.2c-steam-without-its-interface]]
   **Owner's test (2026-11-23): Red Dead Redemption 2 and STAR WARS Jedi: Fallen Order passed** (quit from the game's
   menu, the console came home by itself; OWNEETLOG was not in, so no log: my instructions did not say to start with it).
   **Closed** (2026-11-23): every publisher's launcher tested works (EA, Rockstar, CD Projekt Red with the beta, Ubisoft).

14. **Games: prevent, do not chase them one by one** (owner, 2026-11-18, serious): almost every game tested gives a
   problem; fixing them one at a time is not how a product for the public is made. The owner cannot buy games to test
   them (few on Steam, fewer on GOG, other kinds unknown); a user does not care whose fault it is, they want to play.
   Cyberpunk 2077 ran at high settings on the same PC and graphics card under Windows (the card was bought for it).
   Wanted: best practices that prevent whole classes of problems, using what open source projects already do
   (internet, other projects: recompilation, emulation, optimisation). The games' phase cannot be taken as done.
   **Owner (2026-11-18):** Cyberpunk 2077 runs without problems on the development PC (Linux Mint). Read there (read
   only): GeForce RTX 4060 (Ada), NVIDIA driver 595.99.02 (open kernel module), Intel i5-13500, Steam as a Flatpak;
   the game is not on the disks mounted now (a library on `/media/derf/Volume1`, not mounted) and its last trace in
   Steam's logs there is 2026-07-22. Two differences that matter for the crash: the card's family (Turing on the
   FrankenPC) and the driver (615.71.09 there). Asked the owner when it last ran there and in which game version.
   **Owner (2026-11-18):** it last ran there around June (before the game's version 2.5); the FrankenPC's GTX 1660
   SUPER is the card that ran it under Windows. "But the problem of all the other games remains." **Proposal** to the
   owner: [[game-compatibility-method]] (the four classes of problems seen, who already solved each, the method).
   Found on the way: the console's Windows games start with `GAMEID=umu-default` and no store
   (`owneet-windows-run`), so umu-protonfixes' per-game fixes never apply to them.
   **Owner (2026-11-18): direction approved; research first.** Point 2 to be tried (Steam's windows shown); the shader
   percentage (approved demo) waits: Steam's own page may make it unneeded.
   **Research done (2026-11-18):** [[steam-the-steamos-way]], [[umu-fixes-and-runtime]], [[nvidia-driver-channel]],
   [[game-test-matrix]]; an order of work proposed to the owner.
   **Owner (2026-11-18): order approved for points 1-3** (Steam not hidden; umu with id and store; native games in the
   Steam Linux Runtime); 4 and 5 along the way; the runtime comes with the Windows-games download.
   **First step built (2026-11-18, owneetd 0.25.36):** Steam is no longer hidden while it launches a game (its shader
   page, install scripts, publishers' launchers and questions on screen, as on SteamOS); from the game's start Steam
   stays behind it until the game's own window (no bare home screen in between). The old way with the testers'
   switch `owneet.debug.steam_launch=hidden`, to compare. Go tests. On OWNEETLOG: waits for the owner's test.
   **Owner's test (2026-11-18, owneetd 0.25.36), STAR WARS Jedi: Fallen Order:** Steam's interface on screen; after a
   few seconds EA's window asked to go on ("Let's go"), then back to Steam's home; about 30 s later Steam's notice on
   the game's input handling, then the shader preparation (until 20:40). Then several screens shown for a few seconds
   each; the game menu's sound heard but **the screen black**, and Steam's notification sounds. 20:43: Steam's popup
   "Jedi: Fallen Order has crashed"; holding Guide brought the console's home; 20:44 "Close game" closed it; Steam
   opened again with no glitch (store). Logs on OWNEETLOG: to read.
   **From the log (`owneet-20261118-202516`):** step 1 did what it should: Steam's controller page, then "Processing
   Vulkan shaders" with its Skip button were on screen (gamescope's screenshots 20:28-20:40); EA's window was seen and
   answered. The game (Unreal 4.21, DirectX 11 through DXVK 3.1.1, "Binding model: Descriptor heap", NVIDIA 615.71.09)
   started at 20:40:32, its window on screen at 20:40:39; at **20:41:03 Steam's window came in front for 5 s** (the
   game between two of its windows; Steam is now behind the game), back to the game at 20:41:08; right after, DXVK
   "Got VK_SUBOPTIMAL_KHR, recreating swapchain" and nothing more: the game's render thread hung ("LowLevelFatalError
   … GameThread timed out waiting for RenderThread after 120.00 secs", 20:43:16), black also in gamescope's own
   screenshots (the game drew nothing). Not known yet: whether Steam coming in front caused it (a game shown, hidden,
   shown again) or the driver / DXVK would hang anyway. **Test proposed:** the same game with the testers' switch
   `owneet.debug.steam_launch=hidden` (the old way: Steam never behind a game before its window). Disk check: nothing
   new (packages' cache 55, the same 5 old core dumps).
   **Owner (2026-11-18):** the switch written on OWNEETLOG (`owneet-debug.txt`: `owneet.debug.steam_launch=hidden`, to be
   removed after the test). **Nothing is left to the driver point (4), not approved: no "wait for a fix".** Found: no
   GPU fault in the kernel's log (no NVIDIA Xid), so the game's frames stopped in the handover between the game and the
   screen (DXVK's swapchain on gamescope's Xwayland), which is OwneetOS's own display chain (NVIDIA: forced
   composition, explicit sync, our Xwayland): ours to fix. Order of the tests: (A) the old way; if it still hangs, (B)
   the existing testers' switches of that chain, one at a time (`owneet.debug.nv_explicit_sync=off`, then
   `owneet.debug.gamescope_explicit_sync=off`); ProtonDB: the game is "gold" (613 reports), so it runs elsewhere.
   **Owner's test A (2026-11-18 21:37, the old way):** Jedi started with Steam closed: the console's home, a loading
   screen, Steam's home, then the game's splash screens; **21:39 the game ran**. 21:41 "Quit to desktop" in the game
   brought **Steam's home, not the console's**. Owner: a very narrow pass; everything else can be tolerated, but
   **quitting a game must bring the console's home**. Logs on OWNEETLOG: to read.
   **From the log (`owneet-20261118-213653`):** the install-script window brought Steam (owneetd 0.25.35, 21:37:48);
   the game in front at 21:37:56; Steam in front for 13 s between two of the game's windows (21:38:12-25) **and the game
   did not hang**: so Steam coming in front was not what hung it on the first try (that hang stays to be watched, maybe
   the very first start after the shader preparation). At 21:41:34 the game's window went, Steam (behind it) came in
   front, and the game ended only at 21:41:44 (EA closing after it): owneetd brought the home screen only with the game
   itself in front. **Fixed** in owneetd 0.25.37: a Steam game's end also brings the home screen with Steam in front,
   unless Steam was chosen during the game (test `TestSteamGameEndBringsHomeOverSteam`). The default stays the new way
   (Steam shown during a launch); the testers' switch removed from the stick. On OWNEETLOG: to test.
   **Owner's test (2026-11-18 22:01-22:08): passed** (quitting Jedi brought the console's home, 22:05:33 and 22:08:06).
   Launched from Steam itself it also comes back to the console's home: not a big problem, **left as it is** (owner: do
   not risk breaking something else). Disk check: nothing new. Next: more games for step 1 (first starts).
   **Owner's tests (2026-11-18, evening):** Dishonored 2 and BioShock Infinite: Steam's interface during the start, the
   main menu reached, the controller works, quitting brings the console's home: **passed**. ELDEN RING: Steam's interface,
   main menu, controller fine; **at the first quit, stuck on Steam's closing screen** (its prompts: force quit, or back);
   force quit ignored; holding Guide brought the console's home. Second try (after force-closing it): started as before,
   a saved game resumed fine, "Quit to desktop" brought the console's home. **The home's "recently played": Jedi still
   shown as the last game played**, though other games were played after it. Logs on OWNEETLOG: to read.
   **Still to test (owner, being installed):** Batman: Arkham City GOTY (queued after Red Dead Redemption 2), DARK SOULS
   III, BioShock, Red Dead Redemption 2 (Rockstar launcher), South Park: The Fractured But Whole (Ubisoft Connect, not bought yet; in
   place of Assassin's Creed Unity, owner 2026-11-20).
   **From the log (`owneet-20261118-221153`):** ELDEN RING's first run: the game's processes stayed after its window
   went; Steam showed its closing screen; the console's "Close game" (22:25:39) ended them in 3 s. Why Steam's own force
   quit did nothing is not in the logs: Proton's log is written again at each start, so the second run replaced the
   first (the test log should keep one per start). Proton's log of a long ELDEN RING session was 155 MB, in `/tmp`, in
   memory (testers only; to cap). **"Recently played":** the interface reads a Steam game's last-played time only from
   Steam's own files when it reads the games, and Steam writes them when it closes: a game played in this session is
   not seen as played until Steam closed. Fix proposed: the console marks a Steam game as played when it ends (owneetd
   knows it). Disk check: nothing new.
   **Owner (2026-11-18): first the recently-played fix, then ELDEN RING again, then umu.** Built: owneet-frontend 0.38.40
   (a Steam game started from the console is marked as played when it ends, in memory; Steam's own files say the same
   once Steam closes); owneetd 0.25.38 (the testers' Proton log for Steam games lighter: no trace of every exception);
   owneet-base 0.0.81 (the test log keeps one Proton log per start: `proton-steam-APPID-N.log`). On OWNEETLOG: to test
   (ELDEN RING, then the home's recently played).
   **Owner's tests (2026-11-19 08:52, log `owneet-20261119-085237`): all passed** (ELDEN RING quit to the console's home,
   08:59:39; the recently played follow at once; Batman: Arkham Knight too, 09:20-09:22). Proton's logs now 5 MB for
   ELDEN RING (was 155 MB), one per start. Seen: at power-off Steam took over 20 s to close and was ended by the
   console ("result=timeout", 09:22:25): Steam killed then checks its files at the next start; to watch. Disk check:
   nothing new. **Next: umu (step 2).** RetroArch: its own step, [[step-4.9-retro-games-with-retroarch|4.9]] (owner, 2026-11-21).
   **Step 2 built (2026-11-19):** protonfixes (in GE-Proton) carries the umu database (`protonfixes/umu-database.csv`,
   seen on the FrankenPC's disk listing in GE-Proton11-9) and needs no internet, but umu passes `GAMEID` on as the id, so
   the console looks the game up itself: owneet-frontend 0.38.41 reads a GOG game's product id (`goggame-<id>.info`,
   extra `disk.gog.id`) and starts it with `OWNEET_GOG_ID`; owneetd 0.25.39's `owneet-windows-run` finds its umu id in
   that file and gives umu `GAMEID=<umu id>` and `STORE=gog`; unknown games stay `umu-default`. Testers' switch
   `owneet.debug.umu_ids=off`. Checked: the lookup on the public database (The Witcher 2 GOG 1207658930 is
   `umu-20920`; its fix exists but is empty). On OWNEETLOG: to test with The Witcher 2 for Windows (its log line
   "GOG 1207658930 is umu-20920"). Also done: the project's build output cleaned (21 GB to 7.9 GB: old ISOs, old test
   logs, old build logs, old previews and demo scratch; the newest ISO, the release test, the VM images and the
   update repositories kept).
   **Owner's tests (2026-11-19):** **BioShock** (the original, not Remastered) starts, but neither the controller nor the
   pointer's click works. **Batman: Arkham City GOTY** starts and works with the controller: passed. **DARK SOULS III**
   starts and works with the controller: passed. **Red Dead Redemption 2:** cannot be opened, the Rockstar launcher
   does not respond to the controller. The Witcher 2 (step 2's test) left for last. Logs on OWNEETLOG: to read.
   **From the log (`owneet-20261119-161814`):** BioShock (7670) ran and was on screen (16:23:31); Steam gave it its
   default gamepad layout (`controller_xboxone_gamepad_joystick`); the original BioShock has no controller support of
   its own, so a gamepad layout does nothing: Steam's keyboard-and-mouse layouts (what a Steam Deck uses for such games)
   were not applied. The console's pointer was turned on (16:24:30) but is not made for games. **Proposal:** try
   SteamOS's options next (step 1, part two: `-steamdeck` first), so that Steam applies the layouts it uses on SteamOS
   for games without controller support. Red Dead Redemption 2 (1174180): Steam ran its install script (16:57:34,
   the Rockstar Games Launcher's installer) and its window ("Language select") **was shown** (step 1 works), but it
   does not take the controller, and the console's pointer is offered only for a running game or web app, not for
   Steam's own windows: nothing could drive it. **Proposal:** the pointer for Steam's windows too (either offered on
   Steam's card, or turned on by itself for a window of an install script): the owner's choice. Disk check: nothing
   new.
   **Built for the BioShock test (step 1, part two, already approved):** owneetd 0.25.40, testers' switch
   `owneet.debug.steam_os=os|pal|deck|all` (`-steamos3`, `-steampal`, `-steamdeck`, or the three as ChimeraOS);
   `all` written on OWNEETLOG for the first try, then one at a time.
   **Owner (2026-11-19): option B** (the pointer by itself for an install script's window). Built: owneetd 0.25.41
   ([[controller-input-map]] updated; test extended). On OWNEETLOG with the SteamOS options switch: to test with Red
   Dead Redemption 2 (the installer's "Language select") and BioShock.
   **Owner's test (2026-11-19, owneetd 0.25.41, `steam_os=all`), Red Dead Redemption 2:** started with Steam closed: it
   took him into "SteamOS" (Steam's own SteamOS interface); he chose the game again and the console's screen came back
   with "Steam is downloading what the game needs" (owner, angry: "wasn't it removed?"). Started from Steam itself: the
   pointer works on the installer. He stopped the process, to try again once this is fixed. Logs: to read.
   **From the log (`owneet-20261119-170849`):** the cause was the testers' switch `steam_os=all`: with `-steamos3` Steam
   behaves as the operating system: it closed and started itself again twice (17:10:31, 17:10:36), took the
   controller through HIDAPI (disconnected at 17:10:37), ran SteamOS's own helpers; while it had no window the
   console's "Starting …" screen stayed (17:11-17:12, with the approved download line of demo 4.5 at 0%), until
   Steam's window came back (17:12:17). The pointer turned on by itself for the installer's windows (17:11:22,
   17:12:37, 17:12:46): option B works. **The switch was removed from OWNEETLOG** (2026-11-19). `-steamos3` is not for
   OwneetOS as it is (Steam takes over the session); `-steamdeck` alone, for BioShock's layouts, only with the owner's
   go.
   **Owner (2026-11-19): prepare the `-steamdeck` test** (while he tests Red Dead Redemption 2). Nothing to build
   (`steam_os=deck` exists); the line goes on OWNEETLOG when it is back. Known risk told: `SteamDeck=1` for every game
   ([[steam-the-steamos-way]]).
   **Owner's report (2026-11-19, Red Dead Redemption 2's installer):** he opened Windows' file window to look at the
   launcher's install folder and closed it at once: the pointer vanished and cannot be turned on again. Logs: to read.
   **From the log (`owneet-20261119-171727`):** the pointer moved to the file window (17:19:17) and went off when it
   closed (17:19:21: it held for one window); the installer coming back opened no new window, and the pointer by hand
   is offered only for a running game. **Fixed** in owneetd 0.25.42: for an install script the pointer holds for every
   window of it and goes off once none of the script's programs is left, whoever started it (tests). On OWNEETLOG: to
   test (Red Dead Redemption 2 again; then BioShock with `steam_os=deck`, written only after RDR2, so that RDR2 does not
   run with `SteamDeck=1`).
   **Owner (2026-11-19): test everything in one go** (the launcher installs once; the pointer does not depend on
   `-steamdeck`): `steam_os=deck` goes on OWNEETLOG now, for RDR2 and BioShock together; RDR2 may pick Steam Deck
   settings at its first start (to change after, once the line is removed).
   **Owner's test (2026-11-19, in progress):** the Rockstar launcher installed, but it had to go on the console's main
   disk (no choice). Red Dead Redemption 2 then stayed on the console's "Starting …" screen for over a minute: told to
   press B (hide) to see what is behind, wait up to about 5 minutes (launcher update, sign-in, first graphics
   preparation), and note the time if nothing comes. Logs: to read.
   **Owner (same test):** behind the "Starting …" screen there was only the console's home; started again from Steam it
   went on, then the Rockstar launcher asked for a verification code and he could not open a keyboard. Told: Guide →
   "Resume with the pointer" on the game, A on the field (or Y) opens the console's keyboard.
   **Owner:** the keyboard works but the code field takes only the last digits. Cause (to confirm in the log): the
   code is split into one box per digit that moves to the next box by itself, and the console's keyboard sends the
   whole text at once, faster than the boxes move on. Workaround told: one digit at a time (Y, one digit, confirm).
   **Fix to build:** the console's keyboard types into a window one character at a time, at a person's pace.
   **Owner (correction):** the console's keyboard had every digit; after "Done" the launcher's field received only the
   last 3. **Cause:** the interface sends the text as soon as the window is on screen again (`focus.changed`), before
   the window has the keyboard, and the keys came 2 ms apart: the first ones were lost. **Fixed** in owneetd 0.25.43:
   with the pointer on, the text waits until the X server's keyboard focus is on the window on screen (checked every
   10 ms, at most 2 s), then is typed at a person's pace (key down 15 ms, 50 ms between keys). **Owner: no fix may
   break other games.** Checked: only the pointer's Send uses `/v1/input/text`; games never get typed text, web apps
   use `/v1/webapps/text`. Test `TestWaitKeyboard`. On OWNEETLOG: to test.
   **Also from the log (`owneet-20261119-172907`):** the pointer for the install script turned on and off by itself
   (17:30:01-17:32:25): fixed behaviour confirmed. With `-steamdeck` alone Steam also started itself twice (17:29:37,
   17:29:43); BioShock was not started in this session. The Rockstar launcher went into the game's own Windows folder
   (Proton's prefix, `compatdata/1174180` on the console's disk), where Proton puts it: not a choice of the console.
   The `steam_os` line removed from OWNEETLOG (17:5x). Disk check: nothing new.
   **Owner's report (2026-11-19, Rockstar launcher):** the code went in; then a checkbox: he ticks it, moves the pointer
   over "Next" and the tick disappears, every time. Suspect (to confirm in the log): Proton's Xalia (controller
   navigation for launchers, run by Proton in Steam games) acting on the same A as the console's pointer.
   **Confirmed (`owneet-20261119-174521`, process list):** `xalia.exe` (Proton Experimental's) runs next to the Rockstar
   `Launcher.exe`: two things act on the same controller over that window (the console's pointer ticks, Xalia's A
   acts too). Workaround told: pointer off, Xalia alone (D-pad, A). **Proposal:** while the console's pointer is on
   for an app, owneetd pauses that app's Xalia (SIGSTOP) and resumes it when the pointer goes off; Xalia untouched
   otherwise (it got Jedi's EA window through). Waits for the owner. Disk check: nothing new.
   **Owner (2026-11-19): with Xalia alone the checkbox cannot be reached; go ahead.** Built: owneetd 0.25.44 pauses
   (SIGSTOP) the `xalia.exe` programs in Steam's unit while the console's pointer is on (one started meanwhile too)
   and lets them go on (SIGCONT) when it goes off; Xalia untouched with the pointer off. Test
   `TestXaliaPausedWhileThePointerIsOn`. Other games: only while the pointer is on (never on a game itself). To put on
   OWNEETLOG (2026-11-19): to test.
   **Owner's test (2026-11-19): passed.** The tick stays; Red Dead Redemption 2 starts, works with the controller, and
   quitting it brings the console's home. **BioShock next (owner):** told to try a Steam layout by hand first (Steam →
   BioShock → controller settings → "Keyboard (WASD) and Mouse" template, or a community layout): if Steam's layouts
   make it playable, the console could set such a layout by itself, only for games without controller support.
   **Owner's report (2026-11-19, BioShock):** the buttons of the settings do not light up when the mouse pointer goes
   over them (hover). Logs on OWNEETLOG: to read.
   **From the log (`owneet-20261119-180115`):** it ends at 18:35:20 on Steam's BioShock page (the stick was taken out
   before the game ran): no data on the game. Earlier (16:23) the console's pointer could not click in BioShock either:
   the game does not take the mouse it is given under Proton, whichever moves it. No known fix online for this exact
   sign (ProtonDB 7670, Proton issue 388: input settings, Proton versions). Asked the owner: the layout used, whether
   clicks work, where the game's own pointer is; the test again with the stick in the FrankenPC throughout.
   **Owner's correction:** BioShock was not started: on BioShock's page in Steam the controller-settings button did not
   light up when reached with the gamepad (no pointer), so he could not use it. **From the screenshots:** at 18:34:38
   Steam's game menu was open (Menu: favourites, Manage, Properties, Cancel); at 18:35:20 the page showed no focused
   element at all (Play not lit, no "A Select" in Steam's prompt bar), while owneetd was keeping gamescope composing
   (the picture was not stale). Most likely Steam's own interface losing its focus when that menu closed; to watch
   whether it happens without the menu. Workaround told: Menu → Manage → controller layout, or B and back into the page.
   **Owner's test (2026-11-19, BioShock with Steam's "Keyboard (WASD) and Mouse" and other layouts):** it started only
   at the 4th try; the right stick moves the cursor, but every button pressed opens the game's "Quit to Windows?"
   popup, and confirming it does not let him play either. Logs on OWNEETLOG: to read.
   **From the log (`owneet-20261119-184228`):** Steam applied the template (`controller_xboxone_wasd.vdf`, 19:01:42);
   Proton started Xalia with the game too (it loads SDL3: it reads the controller): likely the source of the Esc on
   every button. The install script (DirectX and the others) kept a window up from 18:44:53 to 18:55:14 (pointer on,
   Xalia paused): the slow starts. **Test switch built:** owneetd 0.25.45 `owneet.debug.steam_xalia=off`
   (PROTON_USE_XALIA=0 for Steam's games; nothing changes without the line); on OWNEETLOG for the BioShock test only
   (no game with a launcher meanwhile), to be removed after. If confirmed, the fix proposed to the owner: Xalia kept out
   of a game's own window, left on launchers.
   **Owner's test (2026-11-19 19:15, Xalia off): nothing changed** (the popup still on every button): Xalia is not the
   cause. The switch line removed from OWNEETLOG. Next hypothesis (not verified): BioShock (Unreal Engine 2.5) also
   reads the controller as a joystick and its own `User.ini` binds the joystick's buttons to its menu (ProtonDB users
   fixed BioShock's controls in that file). Asked the owner: verify it (the test log copies the Steam games' `.ini`
   files changed in the session), or put BioShock aside and go on with The Witcher 2 (umu) and step 3.
   **Owner: verify it.** Built: owneet-base 0.0.82, the test log copies the `.ini` files (under 256 KB) of the users'
   folders in Steam's Windows prefixes (`<log>.games/ini/APPID/…`), only read. On OWNEETLOG: BioShock once more.
   **Owner's report (2026-11-19 evening):** Steam sometimes does not behave (updates?); recently played did not follow
   My Little Puppy started from Steam's own page (first only after the console restarted); BioShock started this time
   and the click came from the right trigger; the owner checked online: the Xbox 360 controller is supported. **Owner,
   serious: research online and read the logs before stating anything about a game, Steam or a tool** (my earlier
   "BioShock has no controller support" was wrong). **From the research and the log (`.ini` copies):** BioShock
   supports the Xbox 360 controller, turned on in its own Options → Controls; its `Bioshock.ini` had
   `UseController=False` and `UseJoystick=False`. Told: Steam's layout back to "Gamepad", then the controller turned
   on in the game's options. Steam: the `steamdeck_stable` client beta, joined by itself during the `-steamdeck` try,
   went back to the public client at 19:27:13; the restarts and updates before were that try's (the `steam_os` switch
   is not used again). At 19:27:02 Steam was closed from the console and at 19:27:06, while it was still closing,
   opened again: owneetd gave the address to the closing Steam, which started a second Steam of its own without
   `-gamepadui`. **Built (2026-11-19):** owneetd 0.25.46: Steam asked for while it closes waits for its end (an event,
   at most 25 s) and starts again with the console's options (test `TestSteamAskedForWhileClosingStartsAgainAfter`;
   only that case changes, nothing for games); owneet-frontend 0.38.42: every Steam game's end (`app.exited`
   `steam:<appid>`, wherever it was started) marks it as played, in memory (the console's own launches unchanged). On
   OWNEETLOG: to test (BioShock with its controller on; a game started from Steam's page, then the home).
   **Owner (2026-11-19):** BioShock's controller turned on in its options with a real mouse: **the game now works
   perfectly with the controller**. The console's pointer could not click there. **From the code:** the pointer's click
   is the button down and up in the same instant (`uinput.Press`, zero ms held), where a real mouse or Steam's trigger
   holds it while the finger presses. Hypothesis (not verified; the 16:23 log is on the stick): the game reads the
   button's state once per frame and never sees a click that short. **Proposal:** the mouse button follows A (down while
   A is held, up when released; X the same for the right button), no fixed time; released if the pointer goes off.
   Changes [[controller-input-map]] (A = click becomes A = the left button, held while A is held). **Owner: go
   (2026-11-19).** Built: owneetd 0.25.47 (vinput `Button`, the pointer presses on A / X down and lets go on their
   release, or when it goes off; the keyboard for a text field after the release); tests `TestButtonHeldAsLongAsA`.
   Other users: only the controller pointer (launchers, installers, apps; never games); `/v1/input/click` unchanged.
   On OWNEETLOG: to test (BioShock's menu with the console's pointer; a launcher's buttons and a text field).
   **Owner's test (2026-11-19): it works.** BioShock and the pointer's click closed: [[closed-items]] 14a. Left in 14:
   The Witcher 2 (Windows) with its umu id, step 3 (native games in the Steam Linux Runtime).
   **Owner's test (2026-11-19 21:37, The Witcher 2 Windows, reinstalled at 21:19): it works.** From the log
   (`owneet-20261119-205430`): "GOG 1207658930 is umu-20920 in umu's database"; protonfixes: "Non-steam game The Witcher
   2: Assassins of Kings Enhanced Edition (umu-20920)", "GOG store specified, using GOG database", its global fix
   applied (`OPENSSL_ia32cap=~0x20000000`). **Step 2 of the method confirmed.** (The game's own fix file is empty.) The
   launcher driven with the pointer (21:37:30-41). Next: step 3.
   **Owner (2026-11-20): every test passed** (recently played for a game started from Steam's page, Steam reopened while
   closing): owneetd 0.25.46 and owneet-frontend 0.38.42 work. Left in 14: step 3.
   [[step-4.2c-steam-without-its-interface]]
   **Step 3 researched** ([[umu-fixes-and-runtime]], 2026-11-20): native games outside Steam in Valve's "Steam Linux
   Runtime 1.0 (scout)" through umu (`umu-scout`), as Heroic does; downloaded with the Windows-games download; as today
   when it is missing; testers' switch `owneet.debug.native_runtime=off`. **Owner (2026-11-20): approved, build it.**
   **Built (2026-11-20):** owneetd 0.25.48 (once Windows games are ready, umu downloads umu-scout and the soldier
   runtime, about 0.9 GB unpacked; `owneet-native-run`), owneet-frontend 0.38.44 (native disk games start through it).
   The Witcher 2's launcher keeps the console's fixes (its preload passed in through `/run/host`). Checked in the
   builder VM: download, the libraries a game sees (32-bit SDL2, OpenAL), the preload, the fallback. To test on the
   FrankenPC: the download (Windows games already ready there), then The Witcher 2 (Linux), its launcher and the game.
   **Owner's test (2026-11-20): every test passed, The Witcher 2 (Linux) works perfectly.** To confirm in the log (stick
   still in the FrankenPC) that it ran in the runtime ("owneet-native-run: in the Steam Runtime (scout)"), not the old
   way. **Confirmed (`owneet-20261120-105501`):** the runtime downloaded by itself in a minute (10:55:09-10:56:12);
   The Witcher 2 (Linux) started in it at 11:10:41, its launcher with the console's fixes, until 11:13:34. Only a
   harmless line: bash (64-bit) cannot load the launcher's 32-bit preload before passing it on ("wrong ELF class").
   Disk check: nothing new but the runtime. **Step 3 done.** Left in 14: points 4 and 5 of the method (to discuss).
   **Owner (2026-11-20):** point 4 rejected (too much upkeep); point 5: GOG's games may be named and used; point 6 in
   Wave 1 ([[step-4.8-games-that-cannot-run]], demo first). Next for 5: the list of free games per cell, proposed to
   the owner ([[game-test-matrix]]).
   **Owner (2026-11-20):** downloading every game proposed (Dota 2, Paladins, Apex Legends, THE FINALS on Steam; Tyrian
   2000, GOG's offline installer, not Galaxy's; Beneath a Steel Sky, GOG's Linux version). No free game found yet for
   BattlEye allowed on Linux nor for a Windows OpenGL game: those cells stay empty. **Waits for the owner's decision:**
   a game that is neither on Steam nor on GOG (local guard) is named, next to Battlefield 6, in three vault notes and
   in the approved demos' texts of the guide and the website (`7.3-user-guide`, `7.8b`, `7.8d`, `7.8m`): remove it?
   **Owner (2026-11-20): removed, Battlefield 6 kept** (the vault's three notes, the four demos, the website's five
   languages).
   [[step-4.2c-steam-without-its-interface]], [[step-4.5-windows-games-proton]]
   **Closed** (2026-11-24, owner): points 1-3 done, 4 rejected, 5 tested (Dota 2, Tyrian 2000, Beneath a Steel Sky and
   THE FINALS run; Apex Legends refuses Linux; Paladins dropped; BattlEye and Windows OpenGL have no free game), 6 goes on as
   [[step-4.8-games-that-cannot-run]] in the roadmap. Noted "to watch" above and not reported again: Steam slow to close at
   power-off, the focus lost when Steam's game menu closes; reopened if they come back.
25. **A Steam download's progress not updated in the console, again** (owner, 2026-11-23, serious): THE FINALS'
   download went on in Steam, the console's progress did not move. Log to read (OWNEETLOG in).
   **From the log (`owneet-20261123-204230`):** THE FINALS was added from Steam (`steam://run/2073850`, 20:44:08). At
   20:48:41 the console showed it in the library as "Preparing…" (moving bar, no numbers); at 20:50:32 Steam's
   downloads page showed "Shader pre-caching update" with "Downloading 906.2 MB / 1.1 GB" and "Installing 71%": Steam was
   downloading the game's **shader pre-cache** (1.1 GB) before the game itself. The console shows any "Shader update"
   phase as "Preparing…" with no numbers, as built for item 8 (demo `4.2c-steam-preparing`, approved 2026-11-17:
   the shader cache among the phases without a percentage). Not a regression: the console never showed the shader
   download's progress; Dota 2's shader update (28%) was the same. Steam's content log gives the shader download's size
   when it starts ("AppID N update started : download 0/452843952, … stage 0/466678415") and writes it into
   `steamapps/shadercache/N/downloads/`, so the console could show it as a download (bytes on disk against the size).
   Proposed to the owner. Also seen: the test log's copy of Steam's `content_log.txt` was cut at 900 KB by the power-off
   (`cp -u` terminated), so this session's download lines are lost: the test log to be fixed.
   **Owner (2026-11-23): go.** Built: owneetd 0.26.8, a new game's shader pre-cache download is a "downloading" card
   (the look of item 8's approved download; no other change): its size from "update started … stage D/T", its bytes
   from `steamapps/shadercache/APPID/downloads` on the library disks, measured every 3 s; without that size, or for an
   installed game, as before ("Preparing…" / not listed); after it, "Preparing…" until the game's own download. Test
   `TestSteamShaderPreCacheDownload`. owneet-base 0.0.87: the test log copies whole files only (written as `.part`,
   then renamed). On OWNEETLOG. The owner stopped THE FINALS' download on purpose: at the next start it resumes,
   to see the progress.
   **Owner's test (2026-11-23/24): the download's progress moves ("solved"); THE FINALS installed and started, its setup
   read the gamepad, one timeout put down to the connection.** **From the logs (`owneet-20261123-211647`,
   `owneet-20261124-091849`):** the cause found on 2026-11-23 is confirmed (Steam's shader download ran 20:44:31-20:50:42,
   in three passes: 1.6 GB, 4 KB, 1.3 GB), **but 0.26.8's new code never ran**: at 21:17:30 Steam resumed the game's own
   download, shown well before too; its only later shader update came with the game installed (11:55). And 0.26.8 is
   wrong, from Steam's own numbers: (1) a pass after another kept the first one's bytes (the pass on screen at 20:50 would
   have shown 100% from its first second); (2) a resumed download counted twice what was already written (Dota 2 at 80%:
   100%); (3) the files' length runs ahead of what is written (Dota 2: 53% against Steam's 28%). The item stays open.
   **Corrected: owneetd 0.26.9**, each update Steam starts counted on its own, a resumed one once, the room the files
   take on the disk instead of their length; tests for the three; the real log read again with the same rules gives the
   three passes of THE FINALS, each with its size. Not seen on the FrankenPC yet: it needs a Steam game **not installed**
   that has a shader pre-cache. On OWNEETLOG. Disk check: nothing new but Steam's own folders.
   **A test of a minute (2026-11-24, from Steam's log):** Steam starts the shader pre-cache 3-5 s after a game's install
   begins ("update canceled : Shader Priority"), so the install is started and cancelled once the card has been seen:
   Paladins (444090, not installed, no shader files left on the disks) has 262 MB of it (2026-11-20).
   **Owner's test (2026-11-24): passed.** **From the log (`owneet-20261124-215212`):** Batman: Arkham Origins' shader
   pre-cache (300 MB, 21:57-22:03) on a slow connection gives the comparison: at 22:02:27 Steam's page says "Installing
   36%" (116.0 of 286.9 MB downloaded); the console, between 22:02:16 and 22:02:38, 36% (120.6 of 332.4 MB). Paladins'
   (276 MB, 21:54:31) was cancelled after 23 s and Steam uninstalled it without errors. Disk check (listing of 21:54, before
   the cancel and Batman's install): nothing new but Steam's own files and the updated packages.
   [[step-4.2c-steam-without-its-interface]]
   **Closed** (2026-11-24, owner).
26. **Batman: Arkham Origins, first start: no warning** (owner, 2026-11-24, step 4.8, owneet-frontend 0.40.0; every other
   test of the step passed): the console showed the licence's code (the window of 4.2c), not the warning that the game may
   not work. Steam's data on the development PC call it unsupported (209000: SteamOS 1, no reason, has a licence); in
   `launch()` the warning comes before the licence. Three possible causes:
   (1) installed from the console with "Install anyway" after the update: it counts as asked, as in the approved demo;
   (2) the FrankenPC's own Steam data do not call it unsupported (older than the development PC's): Details would then
   have no such rows; (3) a web app or the player was open: the warning is skipped then, the licence is not (a real
   difference in the code, to correct in any case: the licence is shown before "close … first"). Not seen in the
   preview: its invented games have no licence.
   **Explained (owner's answer and log, 2026-11-24):** cause (1). The install was started from the console after the update
   (Steam: 21:55:31), its warning was seen, the rows are in Details; Steam's data there give 11 such games. "Install anyway"
   counts as asked, as in the approved demo. The difference in (3) is **not corrected** (the owner: enough): with a web app
   or the player open, a game with a licence not accepted shows the licence, then "close … first", and its warning at
   the next start. [[step-4.8-games-that-cannot-run]]
   **Closed** (2026-11-24, with step 4.8).
