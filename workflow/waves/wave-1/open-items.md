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
| 8 | "Preparing" while Steam prepares a download (no percentage: Steam does not give one) | Built (owneetd 0.25.33, owneet-frontend 0.38.39), on OWNEETLOG: to test with a Steam download |

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|

### To build or prepare (assistant)

| # | What | Where it stands |
|---|---|---|
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
9. **GitHub pages with every website update**: README, the repositories' description and topics; the
   text is prepared here, the owner publishes it. [[website]]

## Tests the owner put off

10. Cyberpunk 2077: Steam's question at launch shown at once. [[step-4.2c-steam-without-its-interface]]
12. "Playing for" over an hour on the home screen ("1 h 5 min", "2 h"). [[step-4.2c-steam-without-its-interface]]


