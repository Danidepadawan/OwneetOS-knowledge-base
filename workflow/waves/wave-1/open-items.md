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
| 25 | A Steam download's progress not updated in the console, again | Corrected in owneetd 0.26.9, on OWNEETLOG: the owner's test of a minute with Paladins' install |

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|

### To build or prepare (assistant)

| # | What | Where it stands |
|---|---|---|

### Others

| # | What | Where it stands |
|---|---|---|

### Roadmap steps left before the first release

| Step | What | Status |
|---|---|---|
| [[step-4.8-games-that-cannot-run\|4.8]] | Games that cannot run, said honestly (demo first) | todo |
| [[step-4.9-retro-games-with-retroarch\|4.9]] | Retro games with RetroArch (owner, 2026-11-21: after the games' tests, before the legal review) | todo |
| [[step-5.0.1-optional-gaming-apps\|5.0.1]] | Gaming programs as optional apps (Steam): left to the owner by Danidepadawan (2026-11-21) | todo |
| [[step-7.3-user-guide\|7.3]] | User guide | in-progress |
| [[step-7.4-hardware-testing-and-v0.1.0\|7.4]] | Hardware testing and v0.1.0 | todo |
| [[step-7.5-legal-review-before-the-public-launch\|7.5]] | Legal review before the public launch | in-progress |
| [[step-7.8k-website-more-languages\|7.8k]] | Website in German, French and Spanish | in-progress |
| [[step-7.8l-website-download-link\|7.8l]] | Website download link (at the release) | todo |
| [[step-7.9-console-more-languages\|7.9]] | Console in German, French and Spanish | in-progress |
| [[step-7.10-donations-choice\|7.10]] | The choice on donations | needs-decision |
| [[step-7.11-sourceforge-project\|7.11]] | SourceForge project | todo |

The steps' status is kept in their own notes; this table follows them. What moved to the next wave is in [[wave-2]],
never here.

## The owner's reports, in detail

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

## Decided, not built yet

Nothing at the moment.
