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
| 13 | Steam games with their publisher's launcher (EA app, Rockstar, CD Projekt Red, Ubisoft Connect) | Cyberpunk: NVIDIA's fix awaited (beta 2.31 meanwhile); demo `4.2c-steam-shaders` to approve; install-script window shown (owneetd 0.25.35, to test with Jedi) |
| 9 | GitHub pages with every website update | READMEs written, description and topics prepared ([[website]]): the owner looks, then pushes and sets them |

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|

### To build or prepare (assistant)

| # | What | Where it stands |
|---|---|---|
| 14 | Games: prevent whole classes of problems, not one game at a time (owner, serious) | Order approved ([[game-compatibility-method]]): first, Steam no longer hidden during a launch |
| 3af | A test of owneetd that failed once (`TestStopAndSourceGone`) | Closed if it does not come back by the end of the tests (owner) |

### Others

| # | What | Where it stands |
|---|---|---|
| 3 | Netflix / YouTube not silent behind the home screen | Danidepadawan, with the web apps |
| 10 | Cyberpunk 2077: Steam's question at launch shown at once | The owner's batch test, with 13 (nothing to build: owneetd 0.25.6) |
| 12 | "Playing for" over an hour on the home screen | The owner's batch test, with 10 and 13 (a game left open over an hour) |

### Roadmap steps left before the first release

| Step | What | Status |
|---|---|---|
| [[step-5.0.1-optional-gaming-apps\|5.0.1]] | Gaming programs as optional apps (Steam, later Epic, GOG, RetroArch) | todo |
| [[step-5.5-spotify\|5.5]] | Spotify | todo |
| [[step-5.6-local-videos-and-music\|5.6]] | Local videos and music | todo |
| [[step-5.7-apps-page\|5.7]] | Apps page | todo |
| [[step-7.3-user-guide\|7.3]] | User guide | in-progress |
| [[step-7.4-hardware-testing-and-v0.1.0\|7.4]] | Hardware testing and v0.1.0 | todo |
| [[step-7.5-legal-review-before-the-public-launch\|7.5]] | Legal review before the public launch | in-progress |
| [[step-7.8k-website-more-languages\|7.8k]] | Website in German, French and Spanish | in-progress |
| [[step-7.8l-website-download-link\|7.8l]] | Website download link (at the release) | todo |
| [[step-7.9-console-more-languages\|7.9]] | Console in German, French and Spanish | in-progress |
| [[step-7.10-donations-choice\|7.10]] | The choice on donations | needs-decision |
| [[step-7.11-sourceforge-project\|7.11]] | SourceForge project | todo |

Not before the release: [[step-1.7-xbox-wireless-dongle-xone|1.7]] and [[step-6.10-waking-the-console-with-the-controller|6.10]] (moved to Wave 2). The steps'
status is kept in their own notes; this table follows them.

## The owner's reports, in detail

3. **Netflix / YouTube not silent behind the home screen**: left to Danidepadawan with the web apps
   (owner, 2026-11-09). [[step-4.5-windows-games-proton]]
3af. **A test of owneetd failed once** (2026-11-13, while building owneetd 0.25.31): `TestStopAndSourceGone`
   (`daemon/internal/installs`) timed out (5 s) waiting for an event during the package's build; the next build
   passed, and 80 more runs (with and without the race detector) did not fail. A test that fails by chance: its
   cause to be found (assistant).
   **Owner (2026-11-17):** if it does not come back by the end of the tests, it is closed (users would open a ticket).
## Decided, not built yet

9. **GitHub pages with every website update**: README, the repositories' description and topics; the
   text is prepared here, the owner publishes it. [[website]]
   **Prepared (2026-11-18):** the code's README follows the website (its description, slogan, features and
   requirements; status "almost here"; the website's address; no vault link, which does not work on GitHub; the folders
   as they are; the trademark note), committed on `feature/phase7`. The website's README: its Structure section names
   today's components (play-tour, guide-drawing, rich-text; no console-screen), not committed yet (which branch: the
   owner's). Both repositories' description and topics: in [[website]]. Waits for the owner.

13. **Steam games with their publisher's launcher** (owner, 2026-11-18): the owner installs games for a batch of tests
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
   [[step-4.2c-steam-without-its-interface]], [[step-4.5-windows-games-proton]]

## Tests the owner put off

10. Cyberpunk 2077: Steam's question at launch shown at once. [[step-4.2c-steam-without-its-interface]]
    **Owner (2026-11-18):** tested in the batch with 13; nothing to build (owneetd 0.25.6 shows Steam as soon as its log
    says it waits for the user).
12. "Playing for" over an hour on the home screen ("1 h 5 min", "2 h"). [[step-4.2c-steam-without-its-interface]]
    **Owner (2026-11-18):** tested in the batch with 10 and 13: a game left open over an hour, then Guide.


