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
