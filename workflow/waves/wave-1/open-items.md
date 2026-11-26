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
| 32 | Step 4.9: the user's own emulators are too little intuitive, not plug and play | Way B: demo 4.9d approved and built (owneet-frontend 0.44.0, owneetd 0.28.1, four cards out of git), on OWNEETLOG: to test |
| 33 | Step 4.9: no sound in three emulators; one not full screen, its textures flicker | Full screen asked (0.44.2); the sound: the test log now records the streams (owneet-base 0.0.89), next test |
| 34 | Step 4.9: fourth test, twelve emulators: sound, controller, bars, starts | Log read: causes found for most; the sound to look into |

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
   a fourth emulator added by the owner. The fourth one did not read the controller either (owner, 2026-11-26): its source binds only the
   stick and the directions by itself; and an emulator makes its own settings at its first start, so "only where it has none"
   would never act on a console where it ran once. **Built:** owneet-frontend 0.44.1, the controller's own button numbers in the
   cards, the emulator's untouched first settings replaced (never the user's). Not tested yet: the wrong processor
   (next test), moving a console with its original removed (the owner makes a backup first).

33. **Third test of the user's own emulators** (owner, 2026-11-26, owneet-frontend 0.44.1): one starts with its profile made and reads the
   controller, but its window is not full screen (a toolbar at the top), its textures flicker (loaded at times, at times not) and
   there is no sound; two more start with **no sound**; the one for another kind of processor is said as it should. One system
   file not copied yet (the owner gets it). Log read (2026-11-26): the screenshots show the emulator's own menu bar at the top
   (it was not asked for full screen: its card now asks, owneet-frontend 0.44.2). The sound: one emulator says its sound
   driver started; none of the three was ever silenced behind the home screen, as a stream of theirs would have been (on
   2026-11-25 one was): which streams they play, and where to, is not in the log. **The test log now records the outputs and
   the playing streams with their programs** (owneet-base 0.0.89), to see it at the next test. The flickering: nothing in the log,
   to research. The disk listing (taken before the emulators ran): nothing unusual.
   The owner (2026-11-26): the controller works in the two that did not read it before; the system file is now copied;
   more emulators added by the owner for the next test.

34. **Fourth test of the user's own emulators** (owner, 2026-11-26, evening; twelve emulators, numbered E1-E12 in the private research note,
   four of them recognised by a card). A Steam game: sound works. The recognised ones: three full screen with the controller but
   **no sound** (E1, E2, E3); one starts, full screen, with sound, but **does not read the controller** (E4, its system file now
   installed). The others, without a card: one works fully by itself (E8); two start with sound but show a bar or two and read
   **only the pointer, as touch** (E6, E9); two **do not start** (E7, E10); one says **a file is missing** (E5); two **need setting
   up** (E11, E12). Log read (2026-11-26): the three silent ones never played a stream the console could see (the ones with
   sound did); the cause is in how they are built, to be looked into. The one without controller: its emulator had made an
   **empty** controller file at its first start, which the console took for the user's own. Two that do not start say a system
   file is missing; one stops on a setting that asks for a Bluetooth adapter of its own. Two show their menu bars and bind no
   controller (no card yet).

## Decided, not built yet

Nothing at the moment.
