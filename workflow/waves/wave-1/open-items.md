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

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|
| 3b | Wine's own programs (`C:\windows\…`) counted as the game's | Fix proposed |
| 3e | A copy to a slow SMR disk looks stuck | Diagnosis done: what the console does about such disks |
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
## Decided, not built yet

4. **"Shutting down" screen at once** (7.6b): demo `design/demos/7.6b-shutting-down.html` approved;
   the code is missing. [[boot-experience]]
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

