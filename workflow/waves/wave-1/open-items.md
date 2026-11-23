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
| 14 | Games: prevent whole classes of problems ([[game-compatibility-method]]) | BioShock and the pointer's click closed (14a); umu ids, recently played from Steam's pages and Steam reopened while closing confirmed. Steps 1-3 done; point 4 rejected; point 5: the owner is downloading the free games proposed (2026-11-20); point 6 = step 4.8 (demo first) |
| 13 | Steam games with their publisher's launcher | Cyberpunk dropped (NVIDIA's driver, owner 2026-11-20); Ubisoft: South Park: The Fractured But Whole, when the owner has it |
| 19 | The interface stopped answering for about 40 s after Beneath a Steel Sky's failed start | Not reproduced; to watch (leave the stick in until the console is off) |
| 20 | Paladins: the first text field did not get the keyboard's text | Black screen: the game's exclusive full screen (borderless works, owner 2026-11-23); Steam's keyboard reaches no game (hypothesis: Steam without gamescope's Wayland): test in another game asked |
| 22 | Steam has network problems, the console does not | The Wi-Fi (USB Realtek) drops often: a test with cable / Intel card, or power saving off: the owner's choice |
| 9 | GitHub pages with every website update | READMEs on `main` (code: `3e359e9`, local, the owner pushes); description and website set by the owner (2026-11-20); topics not shown by GitHub yet: the owner checks |

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|

### To build or prepare (assistant)

| # | What | Where it stands |
|---|---|---|

### Others

| # | What | Where it stands |
|---|---|---|
| 3 | Netflix / YouTube not silent behind the home screen | Danidepadawan, with the web apps |

### Roadmap steps left before the first release

| Step | What | Status |
|---|---|---|
| [[step-4.8-games-that-cannot-run\|4.8]] | Games that cannot run, said honestly (demo first) | todo |
| [[step-4.9-retro-games-with-retroarch\|4.9]] | Retro games with RetroArch (owner, 2026-11-21: after the games' tests, before the legal review) | todo |
| [[step-5.0.1-optional-gaming-apps\|5.0.1]] | Gaming programs as optional apps (Steam, later Epic, GOG, RetroArch): left to the owner by Danidepadawan (2026-11-21) | todo |
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
19. **The FrankenPC froze, inputs ignored** (owner, 2026-11-22, right after Apex's window and Beneath a Steel Sky's
   failed start): switched off by hand. The session's log on the stick stops at 19:35:18 (Steam's update check, nothing
   wrong before it); the whole journal of that boot comes with the next start with OWNEETLOG (`.previous`).
   **From that journal (`owneet-20261122-195300.previous`, boot -2):** the system was running: after Beneath a Steel Sky
   ended (19:34:57) nothing was logged until the stick was pulled out at 19:35:37 (FAT write errors: that session's
   screenshots and games folder were lost), and the power button shut it down cleanly at 19:37:00. So the interface,
   not the PC, stopped answering for about 40 s; no error says why. Tried in the preview (a disk game that ends at once
   without a window): the interface kept answering. Not seen again in the next session. **To watch:** if it happens
   again, leave the stick in until the console is off (the screenshots show what was on screen).

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

## Decided, not built yet

9. **GitHub pages with every website update**: README, the repositories' description and topics; the
   text is prepared here, the owner publishes it. [[website]]
   **Prepared (2026-11-18):** the code's README follows the website (its description, slogan, features and
   requirements; status "almost here"; the website's address; no vault link, which does not work on GitHub; the folders
   as they are; the trademark note), committed on `feature/phase7`. The website's README: its Structure section names
   today's components (play-tour, guide-drawing, rich-text; no console-screen), not committed yet (which branch: the
   owner's). Both repositories' description and topics: in [[website]]. Waits for the owner.


13. **Steam games with their publisher's launcher** (owner, 2026-11-18): EA (STAR WARS Jedi: Fallen Order) and Rockstar
   (Red Dead Redemption 2) work (their tests in item 14); CD Projekt Red (Cyberpunk 2077): **dropped by the owner
   (2026-11-20)**, a fault of NVIDIA's driver on that card, not of OwneetOS ([[closed-items]] 13a,
   [[nvidia-turing-shader-compiler-crash-in-vkd3d-games]]); Ubisoft: South Park: The Fractured But Whole (in place of Assassin's Creed Unity, owner 2026-11-20), when the owner
   has it.
   Demo `4.2c-steam-shaders` approved, not built (Steam's own shader page is shown now).
   **Owner (2026-11-20):** South Park: The Stick of Truth instead of Assassin's Creed Unity? Checked: its Steam version
   does not use Ubisoft Connect (Ubisoft's support and PCGamingWiki: only non-Steam copies need it), so it would not
   test Ubisoft's launcher; South Park: The Fractured But Whole on Steam does use it. Answer given to the owner.
   **Owner (2026-11-20):** The Fractured But Whole replaces Assassin's Creed Unity for the Ubisoft Connect test (a
   Ubisoft account is needed).
   [[step-4.2c-steam-without-its-interface]]

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
   nothing new. **Next: umu (step 2).** RetroArch: moved to Wave 2 (owner).
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
