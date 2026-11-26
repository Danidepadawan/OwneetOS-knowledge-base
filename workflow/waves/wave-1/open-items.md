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
| 29 | Step 4.9: moving a console between disks | Built 2026-11-25 (demo 4.9b approved), on OWNEETLOG: to test with 4.9 |

### Waits for the owner's decision

| # | What | Where it stands |
|---|---|---|

### To build or prepare (assistant)

| # | What | Where it stands |
|---|---|---|
| 30 | Step 4.9: an emulator starts its game but does not read the controller | Cause found: its own first settings are for a keyboard. Demo 4.9c approved, built: owneet-frontend 0.43.0, to test |
| 31 | Step 4.9: an emulator does not start its game, perhaps a wrong setting | Our rule gave it the wrong folder: built, owneet-frontend 0.43.0, to test; the closing stays as it is |
| 32 | Step 4.9: the user's own emulators are too little intuitive, not plug and play | Way B chosen (owner, 2026-11-26): the console recognises some emulators and prepares them. Demo 4.9d |

### Others

| # | What | Where it stands |
|---|---|---|

### Roadmap steps left before the first release

| Step | What | Status |
|---|---|---|
| [[step-4.9-the-users-own-emulators\|4.9]] | The user's own emulators (owner, 2026-11-25: the user brings everything; built 2026-11-25, owneet-frontend 0.42.0 and owneetd 0.28.0: waits for the test on the FrankenPC) | in-progress |
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
   `4.9b-move-a-console` approved (owner, 2026-11-25) and built: owneet-frontend 0.42.0, owneetd 0.28.0, on OWNEETLOG.

30. **An emulator of the user's starts its game but does not read the controller** (owner, 2026-11-25, first test of step 4.9 with
   three emulators; one works perfectly). "The matter of the inputs to remap is not a small one." Log read (2026-11-25): the emulator was started well and its game
   was on the screen; with no settings of the user's, its own source maps the first controller to the keyboard (the emulator of item
   31 maps none). The working one recognises the controller by itself. The assistant had taken the pointer's going off at a second
   window for a hindrance: **it was not, the pointer did its work (owner, 2026-11-25)**: its rule stays as it is. Agreed
   (owner, 2026-11-25): the notice before an emulator's first start says where the controller is set, and can open the emulator.
   Demo `4.9c-first-start-of-an-emulator` approved (owner, 2026-11-25), built: owneet-frontend 0.43.0.
31. **An emulator of the user's does not start the game**, "perhaps a wrong setting" (owner, 2026-11-25, same test). Log and the emulator's source read (2026-11-25): the game's folder holds a text file
   and one folder, the game is in the latter; our rule gave the outer folder, where the emulator looks for the game's program in
   fixed places only and does not find it. **Built (owner's OK, 2026-11-25): owneet-frontend 0.42.1:** a single folder with
   the game's name is looked into, one with another name is asked about once; tiny files beside folders that hold a big one
   do not stand for the game ([[users-own-emulators-design]]). To test. Whether other settings are missing too is not known until it is given the right folder. Remarks of the same log:
   (a) two emulators closed from the console did not end in 10 s and were killed, a save could be lost: one, in its own
   source, answers the request to close with a question on the screen (by default), which nobody could see; the other's
   library takes the request, and the emulator does not read what it makes of it; asked as a window is closed, it ends by itself (its
   source). The change is proposed to the owner;
   (b) an emulator built for another kind of processor is listed as any other, and cannot start: demo 4.9c approved, built: owneet-frontend 0.43.0;
   (c) an emulator asked for a higher limit of locked memory than the system gives.
   **The owner (2026-11-25): stop, nothing that damages what is built so far.** Asked: on what the console decides whether to ask the
   user; how many of these problems one program for many consoles would solve. Nothing more is built until the owner chooses. Of
   owneet-frontend 0.42.1 (not on OWNEETLOG) two points change what starts today, found by the assistant: a folder with one folder of
   another name is asked about (it was given as it is); tiny files beside big folders give the folder (the file was given),
   and some emulators want that very file. To correct or take back, the owner's choice.
   **Chosen (owner, 2026-11-25):** corrected, so that what starts today stays identical: only a single folder with the game's own name is
   looked into, and what to start is asked once when that has files and folders side by side; the rest as before 0.42.1
   (owneet-frontend 0.43.0). The closing stays as it is, until a test shows that a save is lost.

32. **The user's own emulators are too little intuitive** (owner, 2026-11-25, second test of step 4.9): "Owneet was made to be plug and play".
   One asks for its system files, one for its controller (not clear how, nor whether it works), one starts but asks to create a
   profile and it is not clear how. Solutions asked: researched and proposed (2026-11-25): A as today, B the console recognises some emulators and
   prepares them, C one program for many consoles. **B chosen (owner, 2026-11-26)**, names in the code only after the legal review,
   a fourth emulator added by the owner. Not tested yet: the wrong processor
   (next test), moving a console with its original removed (the owner makes a backup first).

## Decided, not built yet

Nothing at the moment.
