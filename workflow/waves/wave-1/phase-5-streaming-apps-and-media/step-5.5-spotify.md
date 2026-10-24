---
type: step
description: "Spotify's web player with its own navigation on the controller; playing in the background is Wave 2."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.5"
status: in-progress
legacy: "ROADMAP.md 5.5"
tags: [step, phase-5]
---
# 5.5 Spotify

Up: [[phase-5-streaming-apps-and-media]] · Status: **in progress** (owner, 2026-10-23)

- **Deliverables:** Spotify's web player with its own navigation on the controller
  ([[extension-design]], "One navigation per supported app"): browsing, search, playing.
- **Playing in the background stays in [[wave-2]]** (owner, 2026-10-23; first decided on
  2026-10-14): in Wave 1 Spotify is closed by the user like any web app or game
  ([[step-5.1-brave-in-the-os]]); the deliverable "playback continues in the background" is
  dropped from this step.
- **What we know at the start (2026-10-23):**
  - Spotify's TV apps are native apps from each TV's store; no web TV interface is known (unlike
    YouTube's `/tv`), so the desktop web player (`open.spotify.com`, already in
    `packages/owneet-base/apps.json`) is expected, as with Netflix ([[step-5.4-netflix]]). The
    check confirms it.
  - Spotify's published keyboard shortcuts (support.spotify.com, "Keyboard shortcuts", one list
    for the desktop app and the web player): Space play / pause, Up / Down previous / next, Right
    add to queue, Ctrl+K search, Alt+J the context menu, Alt+Shift+H / 0 / J / Q Home, Library,
    Now playing, Queue. **No seeking key** is listed; Spotify's own list (Ctrl+/) may show more.
  - Spotify's terms were checked on 2026-10-18 ([[legal-compliance]]): nothing applies to the
    extension; Brave's ad blocking is already an item of
    [[step-7.5-legal-review-before-the-public-launch]].
  - The first opening goes through 5.4's Widevine consent and "Preparing…".
- **Agreed (owner, 2026-10-23):**
  - **LT / RT seek back / forward**, only with Spotify's own means (a key, or its progress bar
    moved as a keyboard moves it); setting the position from a script stays rejected, as for
    YouTube (2026-10-19).
  - **X adds the selected item to the queue** (the map's "secondary action on the selected item").
  - **LB / RB switch Spotify's top-level sections** (Home, Search, Your Library: the check
    confirms the list). The owner first asked for previous / next song on LB / RB; the guard
    [[product-invariants]] keeps LB / RB for top-level sections, so **previous / next stay in
    Spotify's player bar** (D-pad and A).
  - No demo: no new console screen, only bindings, as for YouTube and Netflix; the bindings go
    into [[controller-input-map]] before any code.
- **Sub-steps** (one per prompt, each tested by the owner):
  1. **Check in the test VM** (a probe next to the extension, `vm/run/probe-5.5/`, never
     shipped): what `open.spotify.com` shows in Brave, with a TV user agent too; the cookie banner;
     signing in with the console's keyboard; the first opening through Widevine; a song playing;
     the names Spotify gives its parts (`data-testid`, `aria-label`: sidebar, top bar, shelves of
     cards, track lists, player bar, right panel, menus); Spotify's keys sent by a script (Space,
     seeking, add to queue, the context menu, the sections, Spotify's own list).
  2. **Bindings, "Inside Spotify"** ([[controller-input-map]], [[extension-design]]), with the
     owner, from what the check finds: D-pad = Spotify's own navigation (shelves as rows of cards,
     track lists, sidebar, top bar, player bar); A presses or plays; B closes a menu, goes back,
     then "Close Spotify?"; X queue; LT / RT seek; LB / RB sections; Y search (or another
     page-level option, since Search is also an LB / RB section); Menu = Spotify's context menu;
     right stick scrolls. If Spotify has no means of seeking, back to the owner.
  3. **Code:** `extension/content/spotify.js` with a node test, the helpers it shares with
     `netflix.js` in one shared file, `input.js` passing X, Menu and LB / RB to the site's
     driver, the manifest, an owneet-base version.
  4. **Close:** terms of service, known limits, the next hardware checks, outcome.
- **Sub-step 1, the check** (owner, 2026-10-23 / 24, test VM, cage, 800×600 then 1422×1090; a
  probe next to the extension, `vm/run/probe-5.5/`, three versions, never shipped; Free account):
  - **A TV user agent gets Spotify's page for phones, which plays nothing:** no player bar, an
    "Open App" button, no keyboard shortcuts, and Play reloads the page. The owner liked its
    bigger, one-column look, but **the desktop web player stays** (the only one that plays).
    The desktop layout looked cramped mostly because the VM's screen was 800×600; how to make it
    calmer on a TV (Brave's scale for this web app, Spotify's sidebars folded, its full-screen
    "Now playing" view) is for sub-step 2.
  - **Spotify's own keys, sent by a script, that work:** Space play / pause; **Shift+← / Shift+→
    seek −5 / +5 s** (the progress bar moves by exactly 5000 ms; its slider steps by 5000 ms);
    **Alt+J opens the context menu** of the focused item (a `contextmenu` event too), with the
    focus inside it; Ctrl+K opens Quick Search (a dialog, Escape closes it); Ctrl+Shift+L goes to
    Search, Alt+Shift+H to Home. **Not working:** Alt+← / Alt+→ (history), Alt+Shift+0 (Your
    Library is the left sidebar in this layout), Enter on a focused button or card (scripted
    Enter activates nothing: a click does), the arrows on the progress bar.
  - **Spotify's own arrow-key navigation:** in a song list Down / Up move between songs and Right
    / Left between a song's links; in an open menu Down / Up move between its items; in a shelf
    Down / Up move from card to card (each card is a `row` of a grid) and Right / Left into a
    card's play button and link; **nothing moves between shelves or regions**. So the
    navigation is the extension's own (as Netflix's), over Spotify's named parts.
  - **Spotify's shortcut list** (Ctrl+/, its own window): Playback: Space, Like Alt+Shift+B,
    Shuffle Alt+S, Repeat Alt+R, previous / next Ctrl+← / Ctrl+→, seek Shift+← / Shift+→, volume
    Alt+↑ / Alt+↓, speed Shift+, / Shift+.; Navigation: Home Alt+Shift+H, back / forward Alt+← /
    Alt+→, Currently playing Alt+Shift+J, Search Ctrl+Shift+L, Liked songs Alt+Shift+S, Queue
    Alt+Shift+Q, Your Library Alt+Shift+0 (and 1–7 for its parts), Made for you Alt+Shift+M, New
    releases Alt+Shift+N, Charts Alt+Shift+C, Recents Alt+Shift+Y; Layout: left sidebar
    Alt+Shift+L, right sidebar Alt+Shift+R (and their widths); Quick Search Ctrl+K, context menu
    Alt+J.
  - **The parts' names** (desktop layout, 2026-10-24): left sidebar `nav[aria-label="Main"]`
    (Your Library, its rows `role=row` with `play-button`s); top bar `global-nav-bar` (`home-button`,
    `search-input`, `browse-button`, `upgrade-button`, `user-widget-link`); main view
    `main` / `home-page`; shelves `component-shelf` (a `role=grid` named by the shelf's title,
    `carousel-scroller`, `carousel-previous-button` / `carousel-next-button`, `see-all-link`);
    cards `[data-encore-id="card"]` (`role=listitem`, a `role=button` with `tabindex`, a
    `play-button`, the title link); songs `tracklist-row` in a `role=row` with `aria-rowindex`
    (`internal-track-link`); player bar `now-playing-bar` (`now-playing-widget-v2`,
    `control-button-skip-back`, `-playpause`, `-skip-forward`, `-repeat`, `control-button-queue`,
    `playback-position`, `playback-progressbar`, `playback-duration`, `volume-bar`,
    `fullscreen-mode-button`); context menu `#context-menu` (`data-testid="context-menu"`,
    `ul[role=menu]`, items `role=menuitem` **with no names of their own**: "Add to queue" is found
    only by its label); after "Add to queue" Spotify says "Added to queue" in a live region.
  - **A Spotify window keeps the selection outside it** (the "Start listening with a free
    account" window): the navigation has to go into Spotify's windows (as Netflix's title window).
  - **Brave's save-password window** (found by the owner, 2026-10-23: it needs a mouse) **is gone
    with three managed policies:** `PasswordManagerEnabled`, `PasswordLeakDetectionEnabled` and
    `AutofillAddressEnabled` set to false (verified by the owner in the test VM, 2026-10-24, after a
    new sign-in). They go into `packages/owneet-base/brave-policies.json` with the code of this step.
  - **Signing out does not reach Facebook / Google / Apple sign-in** (owner, 2026-10-24): Spotify's
    Log out ends only Spotify's session; the provider's sign-in stays in the web app's profile, so
    "Continue with Facebook" goes straight back to the same account. Today only removing the web
    app (which deletes its profile, [[step-5.1-brave-in-the-os]]) signs out of everything. A
    console "Sign out of {name}" (empty the web app's cookies and site data, keep the app and
    Widevine) was proposed; **the owner declined it (2026-10-24): no "Sign out of" option.**
    Removing the web app stays the only way to sign out of everything (a known limit of this step).
  - **Sub-step 1 done (2026-10-24).** Next: sub-step 2, the bindings.
- **Sub-step 2, the bindings** (owner, 2026-10-24): "Inside Spotify" in [[controller-input-map]] and
  "Spotify" in [[extension-design]]: its own navigation (shelves and cards, song lists, the left
  sidebar, the top bar); A clicks; B closes a menu or window, goes back, then "Close Spotify?";
  X adds to the queue; **Y moves the selection to the player bar and back** (owner's choice over
  Quick Search: previous / next are there); Menu = Spotify's context menu; LT / RT −5 / +5 s;
  **LB / RB = Home → Search → Your Library**, going round (owner's choice over Home ↔ Search).
  **On a TV** (owner's choice): **Spotify drawn bigger** (laid out as on a screen about 1280 px
  wide, 1.5× on a 1080p TV) and **its right panel folded away**; the left sidebar stays open and
  Spotify's full-screen view is only its own button in the player bar. "Install App", "Open in
  Desktop app" and "Open Miniplayer" are never reached. **Sub-step 2 done.** Next: sub-step 3,
  the code (extension, Brave's password policies, an owneet-base version).
- **Sub-step 3, implemented (2026-10-24), waiting for the owner's test:** owneet-base 0.0.51:
  `extension/content/spotify.js` (Spotify's own navigation, as agreed in sub-step 2; tests
  `test/spotify.test.js`), `extension/content/shared.js` (the rows' geometry and the keys, moved out
  of `netflix.js`; `test/shared.test.js`), `input.js` passing X, Menu and LB / RB to the site's
  driver, the worker setting Brave's zoom for Spotify, and Brave's managed policies without password
  or address saving. One detail beyond sub-step 2, for the owner to confirm: **right at the end of a
  shelf reaches its "Show all"** (otherwise unreachable from the cards).
