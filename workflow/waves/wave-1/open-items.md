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
| 27 | The games folder in German, French and Spanish is not recognised | Corrected 2026-11-25, on OWNEETLOG: to confirm |
| 28 | The keyboard's prompts overlap (German, XL) | Corrected 2026-11-25 (they scroll), on OWNEETLOG: to confirm |
| 29 | Step 4.9: moving a console between disks | Demo 4.9b of 2026-11-25 waits for approval (the card and the folder "Emulation" built) |

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
| [[step-4.9-the-users-own-emulators\|4.9]] | The user's own emulators (owner, 2026-11-25: the user brings everything; built 2026-11-25, owneet-frontend 0.41.1 and owneetd 0.27.1: waits for the test on the FrankenPC) | in-progress |
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

27. **The games folder's name in German, French and Spanish** (found by the assistant on 2026-11-25; owner: "solve it now"): the texts
   say "Spiele", "Jeux", "Juegos", the console knows only `Games` and `Giochi` (interface, owneetd's moves and installs, the
   disks' preparation). **Corrected:** owneet-frontend 0.41.1, owneetd 0.27.1, owneet-base 0.0.88, owneet-installer 0.0.6: the five names
   everywhere; a new one in the console's language. Seen in the preview (a game in "Spiele"); preparing a disk with one of the
   new names not tried.
28. **The on-screen keyboard's prompts overlap** (found on 2026-11-25 in German, text XL; owner: solve it now, "if the XL text is too
   big in the prompts, make them scroll"). **Corrected:** owneet-frontend 0.41.1 (`PromptBar`): only when, with the right-hand words
   already left out (demo 3.3c), they still meet; every screen. Seen in the preview (German, XL).
29. **Step 4.9, after the build** (owner, 2026-11-25): a text for the pointer's card when an emulator is opened by itself (approved);
   moving a console's folder between disks ("absolutely yes": demo first); the owner's idea of a top folder "Emulation" next
   to the games folder, instead of looking into every game's folder: the assistant's judgment asked (**agreed: better**). **Built:** the
   card's text, the folder "Emulation" (also a place of the file manager), owneet-frontend 0.41.1. The moving: demo
   `4.9b-move-a-console` waits for approval.

## Decided, not built yet

Nothing at the moment.
