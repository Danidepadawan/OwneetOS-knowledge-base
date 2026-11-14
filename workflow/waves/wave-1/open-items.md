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
| 3t, 3p | Step 6.11: the simplified file manager, the console cleaning its own leftovers | Tested, all passed; the prefix rule left (assistant) |
| 3ag | Guide with nothing running goes back to the home screen; the Home prompt only while nothing runs | Built (owneet-frontend 0.38.33), on OWNEETLOG: to test |
| 3b | Wine's own programs (`C:\windows\…`) never counted as the game's | Built (owneetd 0.25.31), on OWNEETLOG: seen with the next Windows games |

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|

### To build or prepare (assistant)

| # | What | Where it stands |
|---|---|---|
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
| [[step-6.11-simplified-file-manager\|6.11]] | A simplified file manager (items 3t, 3p) | in-progress |
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
   **Disk check (2026-11-13 17:23 listings):** nothing new (packages' cache 196 files: from owneet-base 0.0.79 the
   console keeps two versions of each).
   **Disk check (2026-11-13 19:59 listings, owneet-base 0.0.79):** the packages' cache went from 196 files to 55 (two
   versions of each package: the hook works); 14 prefixes 7.6 GB, Proton's logs 1.4 GB, 5 core dumps; on the SATA disk
   Steam's wanted downloads 39.4 GB, shader caches 6.1 GB, `compatdata` 2.1 GB.
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
   **Owner (2026-11-13): build it after item 4.** Built in owneet-frontend 0.38.32 (the file manager) and owneet-base
   0.0.79 (the packages' cache and crash dumps cleaned by the console), details in
   [[step-6.11-simplified-file-manager]]; on OWNEETLOG; waits for the owner's test. Left: the prefix removed with a
   Windows game on an internal disk (3t (a)).
   **Owner's test (2026-11-14): all passed** (the file manager, the places, the deletions). Left in step 6.11: the
   prefix removed with a Windows game on an internal disk.
3af. **A test of owneetd failed once** (2026-11-13, while building owneetd 0.25.31): `TestStopAndSourceGone`
   (`daemon/internal/installs`) timed out (5 s) waiting for an event during the package's build; the next build
   passed, and 80 more runs (with and without the race detector) did not fail. A test that fails by chance: its
   cause to be found (assistant).

3ag. **Guide does nothing while nothing runs** (owner, FrankenPC, 2026-11-14): the Home button does nothing unless Steam
   is open. **Owner's fix (2026-11-14, no demo):** while Steam, a media app or a game runs, the Home prompt leaves the
   prompt bar; otherwise Guide really goes back to the home screen. **Built** (owneet-frontend 0.38.33: `guideHome()`
   on owneetd's `home.requested` closes the windows over the pages and goes to the Home section; `Nav.homePrompt` follows
   the running apps; [[controller-input-map]]); checked with `tools/frontend-preview` (`guide-home.txt`). On OWNEETLOG;
   waits for the owner's test.

## Decided, not built yet

6. **Cover pictures from a disk** (6.9): demo to do. [[step-6.9-cover-images-from-a-disk]]
8. **"Preparing" with a percentage for Steam downloads**: nice to have in Wave 1 if easy; demo first.
   [[step-4.2c-steam-without-its-interface]]
9. **GitHub pages with every website update**: README, the repositories' description and topics; the
   text is prepared here, the owner publishes it. [[website]]

## Tests the owner put off

10. Cyberpunk 2077: Steam's question at launch shown at once. [[step-4.2c-steam-without-its-interface]]
12. "Playing for" over an hour on the home screen ("1 h 5 min", "2 h"). [[step-4.2c-steam-without-its-interface]]


