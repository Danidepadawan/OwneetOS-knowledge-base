---
type: decision
description: "The binding meaning of every button on every screen, keyboard fallback, OSK buttons, repeat timing."
area: ux
status: active
decided: 2026-10-03
updated: 2026-10-29
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
right stick, **Super (the Windows key) = Guide** (2026-10-15: owned by owneetd like Guide, also while
a game or app runs; for testing and PCs without a controller).

**Inside a web app** (step 5.2, 2026-10-15; the console's extension in Brave,
[[extension-design]]): D-pad / left stick move a ring between the page's targets (spatial
navigation); A presses the target (on a text field: the console's on-screen keyboard); B leaves full
screen, closes the page's open dialog, or goes back a page, and where there is nothing to go back to
asks to close the web app ("Close {name}?"); the right stick scrolls. X, Y, Menu, LB / RB and LT / RT
do nothing (sites may get their own meanings in steps 5.3–5.5). Guide stays owneetd's.

**Inside YouTube** (step 5.3, 2026-10-18; YouTube's TV interface `youtube.com/tv`,
[[extension-design]]): the extension sends the TV interface its own keys and draws no ring
(YouTube draws its selection). D-pad / left stick = arrows (YouTube's selection; held directions
repeat with this map's timing); A = Enter (select; in the player YouTube's own pause / play);
B = Escape (YouTube's back), and where YouTube's back has nothing left (its "Welcome back" account
page, where Escape does nothing) asks to close the web app ("Close YouTube?"); LT / RT, X, Y, Menu,
View and the right stick do nothing (no key of the TV interface seeks by 10 s: seeking is done
with YouTube's own progress bar, 2026-10-19); LB / RB are never used. Guide stays owneetd's. Other pages (e.g. Google's) keep the web-app bindings above.

**Inside Netflix** (step 5.4, 2026-10-22; Netflix's desktop site, its own navigation,
[[extension-design]]): on the **browsing pages** (Home, Series, Films, My list, search results)
D-pad / left stick move from row to row keeping about the same column, with Netflix's top menu
above the first row, and from tile to tile in a row, the row sliding on at the edge of what is
visible; A on a tile opens Netflix's title window and the selection goes into it; the right stick
scrolls the page. In the **title window** the D-pad moves between its buttons (Play / Resume, My
list, rating, the season, the episodes, "More like this"); B closes it and the selection goes back
to its tile. In the **player** any button brings up Netflix's controls and the D-pad moves between
them (back, play / pause, −10 / +10, volume, next episode, episodes, subtitles and audio, speed);
A presses the selected control, and pauses / plays while the controls are hidden; **LT / RT = −10
/ +10 s** (Netflix's own ← / →, repeating with this map's LT / RT timing); B closes an open menu,
otherwise leaves the player. B closes an open dropdown first (the Browse and profile menus, a
title's seasons; owner's test, 2026-10-22). Pages outside Netflix's main screens (start page, sign-in, the email
code, "Who's watching?") keep the web-app bindings above. **Y opens Netflix's search** on the
browsing pages (owner, 2026-10-22); X, Menu and View do nothing; LB / RB are never used; Guide
stays owneetd's.

**Inside Spotify** (step 5.5; Spotify's desktop web player, drawn bigger on a TV, its own
navigation, [[extension-design]]; owner, 2026-10-28 and 2026-10-29): **D-pad / left stick move by
position only**, everywhere in Spotify (the page, the player bar, a menu, a window): the selection
goes to the nearest target in the pressed direction, with no rule of rows or columns; a card, a song
and a Your Library row are one target each; Spotify's sliders (the progress bar, the volume) are
not stops; the page scrolls to the selection. **A plays** the selected card, Your Library row or
song at once (its own play button); on anything else A presses it (a text field: the console's
keyboard). **Menu opens the selected item's page** (the album, playlist, artist or song; owner,
2026-10-29). **B** closes an open menu or window first (Spotify's windows keep the selection inside
them), then the player bar, otherwise goes back a page, and where there is nothing to go back to asks
to close the web app ("Close Spotify?"). **X adds the selected song, album or playlist to the queue**
(Spotify's context menu, "Add to queue"; owner, 2026-10-23). **Y moves the selection to the player
bar** (shuffle, previous, play / pause, next, repeat, lyrics, queue, devices, full screen…) **and Y
or B brings it back** where it was (owner, 2026-10-24). **LT / RT = −5 / +5 s** (Spotify's own
Shift+← / Shift+→, repeating with this map's LT / RT timing; owner, 2026-10-23). **LB / RB do
nothing** (owner, 2026-10-29: everything is reachable by position). The right stick scrolls.
"Install App", "Open in Desktop app" and "Open Miniplayer" are never reached: they open windows the
console cannot show. View, L3 and R3 do nothing; Guide stays owneetd's. Pages outside Spotify's
player (sign-in, Facebook / Google / Apple sign-in) keep the web-app bindings above.

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

**Controller pointer** ([[step-4.7-controller-pointer]], owner 2026-10-19): for apps and
launchers made for a mouse (e.g. a Steam game's EA app or Ubisoft Connect, a game's start or
options window), **never left on a game** itself. The user turns it on by hand from the console
(Guide, then "Resume with the pointer" on the running game or app: launchers belong to their
game, so it is offered there too), and off the same way; it holds for **one window**: it turns off
by itself when another window takes the screen (e.g. the game after its launcher) and when the
app closes. While it is on:
**left stick** moves the pointer, **D-pad** moves it in small steps, **A** = click, **X** = right
click, **right stick** = wheel (scroll), **Y** = type: the console's on-screen keyboard, then the
text goes to the window (a fallback: **A on a text field opens the keyboard by itself**, owner
2026-10-19, when the pointer has the text "I" shape after the click); Guide keeps its meaning. It intercepts nothing: the app still receives
every input (no grab), the pointer only adds a virtual mouse's movements and clicks (owner,
2026-10-19: compatible with the guard [[product-invariants]]).

Implemented once for every screen in step 3.5 (`Nav`, `NavArea`: [[qml]]).

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
| 2026-10-15 | Keyboard fallback for Guide: the **Super (Windows) key**, handled by owneetd like Guide (also while a game or app runs). Chosen over G, which is used for typing and in games (owner's choice, assistant's advice). |
| 2026-10-15 | Inside a web app (step 5.2): D-pad moves a ring between the page's targets, A presses, B goes back and asks to close where there is nothing to go back to, the right stick scrolls; text fields open the console's keyboard; the other buttons do nothing ([[extension-design]]). |
| 2026-10-16 | The list of Settings' sections goes round: up on the first section to the last, down on the last to the first. |
| 2026-10-18 | Inside YouTube (step 5.3, its TV interface): the extension sends YouTube's keys and draws no ring: D-pad = arrows, A = Enter, B = Escape and "Close YouTube?" where YouTube's back has nothing left (its account page), LT / RT = ±10 s in the player if a key does exactly that; the other buttons do nothing ([[controller-input-map]]). |
| 2026-10-19 | Controller pointer (step 4.7): turned on by hand from the console, for apps and launchers, never on games; left stick moves, D-pad small steps, A click, X right click, right stick wheel, Y types with the console's keyboard; nothing intercepted (no grab: compatible with the guard). |
| 2026-10-19 | Pointer: A on a text field opens the console's keyboard by itself (the pointer's "I" shape after the click, read through XFixes); Y stays as the fallback. |
| 2026-10-19 | Inside YouTube: LT / RT stay unused (no key of the TV interface seeks by exactly 10 s; seeking the video directly from the extension rejected); seeking is done with YouTube's own progress bar ([[controller-input-map]]). |
| 2026-10-22 | Inside Netflix (step 5.4): Netflix's own navigation on its browsing pages (rows and tiles, rows sliding on, A into the title window), the title window (B back to the tile) and the player (any button shows the controls, D-pad between them, A presses or pauses, LT / RT ±10 s, B closes a menu or leaves); other pages keep the web-app bindings ([[controller-input-map]]). |
| 2026-10-24 | Inside Spotify (step 5.5, its desktop web player): its own navigation (shelves and cards, song lists, the left sidebar, the top bar); A clicks; B closes a menu or window, goes back, then "Close Spotify?"; X adds to the queue; Y to the player bar and back; Menu = Spotify's context menu; LT / RT −5 / +5 s; LB / RB Home → Search → Your Library, going round ([[controller-input-map]]). |
| 2026-10-26 | Inside Spotify redone for its player with an Android TV user agent: Y opens the full player (this view's player bar) and Y or B closes it; LT / RT press Spotify's progress bar ±5 s with the full player open, nothing elsewhere; LB / RB the bottom tabs; the footer, links leaving Spotify, "Get App" / "Open App" and the fixed bottom bars never reached by the D-pad. |
| 2026-10-28 | Inside Spotify back on its desktop web player (the Android TV view keeps Your Library in Spotify's app): the bindings of 2026-10-24, and the **D-pad moves by position only** (the nearest target in the direction, no rows or columns; owner), in Spotify's own code. |
| 2026-10-29 | Inside Spotify: **A plays** a card, Your Library row or song at once, **Menu opens its page**; LB / RB do nothing (everything is reachable by position); the D-pad moves by position in the player bar, menus and windows too, Spotify's sliders not stops. |
