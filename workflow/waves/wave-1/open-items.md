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
| 3b | Wine's own programs (`C:\windows\…`) never counted as the game's | Built (owneetd 0.25.31): tested with step 6.9's new try (owner) |
| 6 | Cover pictures from a disk (step 6.9) | Built (owneet-frontend 0.38.38): to test again with pictures on a stick or disk that is not OWNEETLOG |

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|

### To build or prepare (assistant)

| # | What | Where it stands |
|---|---|---|
| 8 | "Preparing" with a percentage for Steam downloads | Nice to have: demo first |
| 3af | A test of owneetd that failed once (`TestStopAndSourceGone`) | Closed if it does not come back by the end of the tests (owner) |
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
| [[step-6.9-cover-images-from-a-disk\|6.9]] | Cover images from a disk (item 6) | in-progress |
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
3af. **A test of owneetd failed once** (2026-11-13, while building owneetd 0.25.31): `TestStopAndSourceGone`
   (`daemon/internal/installs`) timed out (5 s) waiting for an event during the package's build; the next build
   passed, and 80 more runs (with and without the race detector) did not fail. A test that fails by chance: its
   cause to be found (assistant).
   **Owner (2026-11-17):** if it does not come back by the end of the tests, it is closed (users would open a ticket).
## Decided, not built yet

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
8. **"Preparing" with a percentage for Steam downloads**: nice to have in Wave 1 if easy; demo first.
   [[step-4.2c-steam-without-its-interface]]
9. **GitHub pages with every website update**: README, the repositories' description and topics; the
   text is prepared here, the owner publishes it. [[website]]

## Tests the owner put off

10. Cyberpunk 2077: Steam's question at launch shown at once. [[step-4.2c-steam-without-its-interface]]
12. "Playing for" over an hour on the home screen ("1 h 5 min", "2 h"). [[step-4.2c-steam-without-its-interface]]


