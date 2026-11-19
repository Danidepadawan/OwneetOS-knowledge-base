---
type: step
description: "A page with every app (streaming services, Videos, Music, stores, and the ones added later), reached from the home screen: when there…"
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.7"
status: in-progress
legacy: "ROADMAP.md 5.7"
tags: [step, phase-5]
---
# 5.7 Apps page

Up: [[phase-5-streaming-apps-and-media]] · Status: **in-progress** (started 2026-11-20)

- **Deliverables:** a page with every app (streaming services, Videos, Music, stores, and the
  ones added later), reached from the home screen: when there are more than six apps, the sixth
  tile of the home's Apps grid becomes "All apps" (like "All games" for games). Its own
  interactive demo first.
- **Related:** the overflow rule ([[home-and-library]], [[ui-patterns]]); installed and missing
  apps shown differently ([[optional-apps]]); the home's Apps grid with install and remove
  ([[step-5.0.0-optional-web-apps]]); the programs to come ([[step-5.0.1-optional-gaming-apps]]).
- **At the start (2026-11-20):** the home's Apps grid (3 × 2) holds exactly six apps: the
  catalogue's web apps (Netflix, YouTube, Spotify), then Videos, Music and the store (Steam's). By
  the overflow rule the page appears on no console until a seventh app arrives (more web apps in
  the catalogue, the programs of [[step-5.0.1-optional-gaming-apps]]).
- **Agreed (owner, 2026-11-20):**
  - **Reach: the rule as agreed.** The page is built now; "All apps" takes the sixth place of the
    home's grid only from the seventh app on (like "All games"). Tested with invented apps;
    consoles see no change until then. (Not chosen: "All apps" always in the sixth place;
    postponing the step.)
  - **Layout: a grid of tiles**, like the Library's grid, larger tiles in the home's style:
    installed apps bright, missing ones dimmed with the download mark, an app being installed or
    removed with the spinner and its line, the open app with the green dot. (Not chosen: a list
    with details; sections by kind.)
  - **Which five stay on the home: installed first, in a fixed order:** the catalogue's order (web
    apps, then Videos, Music, the store), installed apps before missing ones; the rest only on the
    page. The tiles do not move as they are used. (Not chosen: the most recently opened; chosen by
    the user.)
  - **Buttons: the same as the home's grid** ([[controller-input-map]], "The Apps page"): A opens,
    or installs a missing app (its confirmation, then progress on the tile); Menu → options
    (Remove; on Steam's tile, close Steam while it runs); B back to the home, the selection on
    "All apps"; the right stick scrolls; no filters (Y and LT / RT do nothing); LB / RB still
    switch sections. (Not chosen: All / Installed filters on LT / RT.)
  - **What follows (to confirm in the demo):** one order everywhere: the home shows the page's
    list, all of it with six apps or fewer, the first five plus "All apps" beyond (so with six or
    fewer a missing web app moves after the store, where today it keeps its place dimmed; the demo
    shows both). "All apps" looks like "All games". Videos and Music opened from the page: B comes
    back to the page, on their tile. The page's grid goes round like the Library's. No owneetd
    change: the catalogue and install / remove exist since 5.0.0. Reused: the home's app tile (one
    component for both places), the theme's app handlers, the page-of-Home pattern of the Videos /
    Music page.
- **Sub-steps** (one per prompt, each tested by the owner):
  0. **Vault** (with sub-step 1): this note, [[home-and-library]], [[controller-input-map]], the
     [[decision-log]].
  1. **Demo** `design/demos/5.7-apps-page.html` ([[demo-before-code]]): a switch between six apps
     (no "All apps") and nine; the home's five plus "All apps" and the order rule; the Apps page
     (title, the grid and its states, A opening or installing with its confirmation and progress,
     Menu → Remove, Videos and back, B back to the home on "All apps", the prompt bar); texts (en,
     it), glyph sets.
     **Written (2026-11-20), waiting for the owner's approval:** `design/demos/5.7-apps-page.html`
     (code `212dca0`; its flows checked with scripted button presses: "All apps" selected on the
     home, the page's grid going round, Videos and back to the page, B back to the home on "All
     apps", Menu → options, Italian at XL). What it shows beyond the decisions:
     - **the page:** a page of Home (the Home tab stays lit), its title "Apps" and the number of
       apps, the tiles in five columns, larger than the home's (the icon, the name, the marks);
     - **"All apps"** in the home's sixth place, outlined like "All games", A Open;
     - **with nine apps** (two invented installed web apps and one missing): the home shows the
       first five installed (Netflix, Spotify, Film Club, Podcasts, Videos): with four installed web
       apps, **Music and the store leave the home** and are on the page only; the missing ones
       (YouTube, Radio) come last on the page;
     - **with six apps:** a switch between installed first (YouTube, missing, after the store) and
       today's order (YouTube in its place, dimmed), for the owner to choose;
     - an app installed from the page moves to its place among the installed ones, the selection
       following it; an open web app shows the green dot on its tile and the home's hero (Resume,
       Close).
  2. **Code:** the theme (one ordered list for the home and the page, `AppTile.qml` out of
     `HomePage.qml`, the "All apps" tile, `AppsPage.qml` as a page of Home, B from Videos / Music
     back to where they were opened, texts); the pretend owneetd with a larger catalogue and
     preview steps; the frontend's tests and theme check; owneet-frontend 0.28.0.
  3. **Close:** known limits, the hardware checks (batched with FrankenPC's), outcome; the owner
     approves.
