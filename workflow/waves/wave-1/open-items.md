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
| 2 | "Resume with the pointer" and "Close game" in the library | Built (owneet-frontend 0.38.30), on OWNEETLOG: to look at |
| 3b | Wine's own programs (`C:\windows\…`) never counted as the game's | Built (owneetd 0.25.31), on OWNEETLOG: seen with the next Windows games |
| 7 | Waking the console with the controller (step 6.10) | Still woken at once by itself; owneet-base 0.0.77 tries three stages, one per sleep: to try |

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|
| 3t, 3p | Junk on the disks: step 6.11, a simplified file manager in Settings → Advanced | Demo 6.11 approved: building it waits for the owner's go |

### To build or prepare (assistant)

| # | What | Where it stands |
|---|---|---|
| 4 | "Shutting down" screen at once (7.6b) | Demo approved: code to write |
| 6 | Cover pictures from a disk (step 6.9) | Demo to make |
| 8 | "Preparing" with a percentage for Steam downloads | Nice to have: demo first |
| 3c | Removing the original on a USB disk Windows left read only | To check in the test VM |
| 3af | A test of owneetd that failed once (`TestStopAndSourceGone`) | Its cause to find |
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
| [[step-6.11-simplified-file-manager\|6.11]] | A simplified file manager (items 3t, 3p) | todo |
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
3. **Netflix / YouTube not silent behind the home screen**: left to Danidepadawan with the web apps
   (owner, 2026-11-09). [[step-4.5-windows-games-proton]]
3b. **Wine's own programs followed as the game's** (found in the owner's test log, 2026-11-09 21:50): the
   home screen at the game's end waited for `C:\windows\system32\explorer.exe` too, because it owns a window;
   there it ended before the game, but it could outlive it until Wine closes. Fix proposed: never count a
   program under `C:\windows` as the game's, even with a window. [[step-4.5-windows-games-proton]]
   **Owner (2026-11-13): apply it. Built** (owneetd 0.25.31, `closing.go` `wineProgram`: a window of a program in
   `C:\windows` no longer makes it the game's; test in `TestHomeWhenTheGamesProgramsEnd`). On OWNEETLOG; it shows only
   when such a program outlives the game, so it is checked with the next Windows games.
3c. **Removing the originals of single games, the read-only case** (6.6c, confirmed by the owner on
   2026-11-10: the original removed after a copy, with no error; the choice of
   games, item 1 of 2026-11-09, confirmed too): left, a USB disk that Windows left read only, to check
   in the test VM (the owner has no Windows disk). [[step-6.6-moving-games-and-media-between-disks]]
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
   **Disk check (2026-11-13 15:49 listings, the console's disk whole, the SATA disk's not made: the console slept
   first):** nothing new: 14 prefixes 7.6 GB, Proton's logs 1.5 GB, packages' cache 190 files, 5 core dumps.
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
3af. **A test of owneetd failed once** (2026-11-13, while building owneetd 0.25.31): `TestStopAndSourceGone`
   (`daemon/internal/installs`) timed out (5 s) waiting for an event during the package's build; the next build
   passed, and 80 more runs (with and without the race detector) did not fail. A test that fails by chance: its
   cause to be found (assistant).

## Decided, not built yet

4. **"Shutting down" screen at once** (7.6b): demo `design/demos/7.6b-shutting-down.html` approved;
   the code is missing. [[boot-experience]]
6. **Cover pictures from a disk** (6.9): demo to do. [[step-6.9-cover-images-from-a-disk]]
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
8. **"Preparing" with a percentage for Steam downloads**: nice to have in Wave 1 if easy; demo first.
   [[step-4.2c-steam-without-its-interface]]
9. **GitHub pages with every website update**: README, the repositories' description and topics; the
   text is prepared here, the owner publishes it. [[website]]

## Tests the owner put off

10. Cyberpunk 2077: Steam's question at launch shown at once. [[step-4.2c-steam-without-its-interface]]
12. "Playing for" over an hour on the home screen ("1 h 5 min", "2 h"). [[step-4.2c-steam-without-its-interface]]


