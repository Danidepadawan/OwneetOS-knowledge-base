---
type: decision
description: "The binding meaning of every button on every screen, keyboard fallback, OSK buttons, repeat timing."
area: ux
status: active
decided: 2026-10-03
updated: 2026-10-16
legacy: "PROJECT_RULES.md §9.1"
tags: [decision, ux, input]
---
# Controller input map (global, binding for every screen)

Every screen and component must follow this map. A button may never have two meanings on the same
screen. New bindings are added here (with the owner) before they are implemented.

| Button (Xbox / PlayStation) | Meaning |
|---|---|
| D-pad / left stick | Move selection (spatial navigation) |
| A / ✕ | Confirm / select |
| B / ○ | Back / close. Where there is nothing to go back to (Home, Library, the list of Settings sections): the **quick menu** (power options, controls and features) |
| X / □ | Secondary action on the selected item (e.g. Details, Install) |
| Y / △ | Page-level option (e.g. Sort, Search) |
| LB / RB (L1 / R1) | Switch top-level section (Home, Library, Settings, …) — **reserved, never used for anything else** (except inside the on-screen keyboard, where no section can be switched: its pages of keys) |
| LT / RT (L2 / R2) | Switch filter inside the current page (e.g. Library: All / Installed / Favorites — "Installed" was removed on 2026-10-11 and restored on 2026-10-14, [[game-library]]). There are no sub-tabs: tabs are only the sections on LB / RB |
| Menu / Options | Options menu for the selected item |
| View / Create | Reserved (screenshot in a later wave) |
| Guide / PS | **Owned by the system daemon**: home / quick menu from anywhere, including in games. Apps and themes must never bind it. Prompt label: "Home". **Exception, Steam** (2026-10-12): while Steam or a Steam game is on screen, a short press is Steam's (its menu; its overlay in games) and **holding it for 1 second** comes back to the console (Steam and the game keep running). See [[guide-button]]. |
| Right stick | Scrolls the page: fast scroll in long lists and grids, and the content of windows (e.g. Credits and licences) |

**On-screen keyboard** (demo 3.10, approved 2026-10-11; changed 2026-10-13): while it is open, A
types the selected key, X deletes, Y types a space, **LB / RB change the page of keys** (letters,
symbols, accented letters), **LT held = capital letters while it is held** (as on Steam's
keyboard), RT does nothing, Menu = Done, B closes the keyboard; the selection wraps around at
every edge. These meanings hold only inside the keyboard; Guide and the right stick keep theirs.

**Lists that go round:** the library's grid (left / right within a row, down / up between the
last and the first row, [[game-library]]) and the list of Settings' sections (up on the first
section goes to the last, down on the last to the first; owner, 2026-10-16).

While a game or app is running, the system intercepts **only** the Guide button; every other input
goes to the game.

**Keyboard fallback** (optional, same meanings): arrows = D-pad, Enter / Space = A, Esc /
Backspace = B, X = X, Y = Y, Q / E = LB / RB, Z / C = LT / RT, M = Menu, Page Up / Page Down =
right stick.

The input map is **fixed**: it is not saved in the frontend's settings, so a change reaches every
system. **Held buttons:** a direction repeats after 360 ms, then every 140 ms; LB / RB and LT / RT
repeat after 720 ms, then every 360 ms; analog triggers count as pressed above half their travel
(released below a quarter); every other button acts once per press.

> [!warning] Waiting for the owner's confirmation
> On 2026-10-13, when `main` was merged into `refactor/ai-harness`, the guard [[product-invariants]]
> ("never use LB / RB for anything but switching top-level sections") gained the exception for the
> on-screen keyboard's pages of keys, matching this note. The edit was kept on that branch; guards
> change only with the owner's agreement, so the owner confirms it (or changes it) when reviewing
> the merge, and this box is then removed.

Implemented once for every screen in step 3.5 (`Nav`, `NavArea`: [[qml]]). Pending binding: the
controller pointer of [[step-4.7-controller-pointer]] goes here before it is implemented.

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Global controller input map adopted: LB/RB = sections, LT/RT = filters ([[controller-input-map]]). |
| 2026-10-08 | Demo 3.3 feedback: wordmark/logo provisional (final logo before the launch, roadmap 7.6); about twenty palettes (Tide in vivid "minty" cyan; new Ember, Espresso, Harbor and more) in a picker with live preview; language chosen from a list; the Guide prompt reads "Home" ([[design-direction]]). |
| 2026-10-08 | Step 3.4 approved. Input map implemented once for every screen (step 3.5): keyboard fallback keys, fixed map, repeat timing ([[controller-input-map]]). |
| 2026-10-09 | Interface sounds reduced to ten ([[interface-sounds-spec]]): one "click" (`nav-confirm`) for A, B, filters, switches, volume and on-screen keyboard; one sound for notices and successes, one for errors and warnings; game launch and Guide over a game share one; `startup` required. LT/RT switch filters only: no sub-tabs inside pages ([[controller-input-map]]). |
| 2026-10-09 | Demo 3.9 review: pairing drawings mark the real buttons (no drawing for "other controllers"); connected Bluetooth controllers can be turned off or forgotten; Display gets a brightness setting (where the screen allows it); the keyboard layout is chosen separately from the language; the right stick scrolls the page and windows ([[controller-input-map]]). |
| 2026-10-09 | Held LB / RB / LT / RT repeat after 0.72 s, then every 0.36 s (directions: 0.36 s, then 0.14 s) ([[controller-input-map]]). Demo 3.9 approved; the brightness setting is shown only on screens that allow it. |
| 2026-10-11 | Demo 3.10 (on-screen keyboard) approved, with the selection wrapping around vertically too. Inside the keyboard: X delete, Y space, LT / RT pages of keys, Menu Done ([[controller-input-map]]). |
| 2026-10-11 | Step 3.12 (interface sounds) done; the first sound after boot needs the sound output running first (a looped silence). Demo 3.13 approved: animated start-up from the boot splash's wordmark; a **quick menu** (side panel from the right, as on SteamOS) with power options and a read-only "Controls and features" guide, opened by **B where there is nothing to go back to** (an accidental press only opens the menu). View stays reserved for screenshots in a later wave ([[controller-input-map]]). |
| 2026-10-12 | After the owner's first Steam test (Guide fought over by owneetd and Steam): **while Steam or a Steam game is on screen, a short Guide press is Steam's; holding Guide for 1 second comes back to the console** (option A; [[controller-input-map]]). "Exit Steam" in Steam's menu also comes back. Steam's own screens that matter (login, a game's launch progress) are shown automatically ([[game-library]]). |
| 2026-10-13 | On-screen keyboard (owner's request): LT held = capital letters while it is held, as on Steam's keyboard; the pages of keys move to LB / RB (no section can be switched while the keyboard is open); RT does nothing there ([[controller-input-map]]). |
| 2026-10-16 | The list of Settings' sections goes round: up on the first section to the last, down on the last to the first. |
