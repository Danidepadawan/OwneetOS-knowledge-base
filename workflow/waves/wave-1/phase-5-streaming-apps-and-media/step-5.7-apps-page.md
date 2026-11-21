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
    the user.) **Changed by the owner after the demo (2026-11-20): the built-in apps first**
    (Videos, Music, the store), then the web apps; **with six apps or fewer a missing app keeps its
    place**; **from the seventh installed app, the five most used** (see the demo's review below).
  - **Buttons: the same as the home's grid** ([[controller-input-map]], "The Apps page"): A opens,
    or installs a missing app (its confirmation, then progress on the tile); Menu → options
    (Remove; on Steam's tile, close Steam while it runs); B back to the home, the selection on
    "All apps"; the right stick scrolls; no filters (Y and LT / RT do nothing); LB / RB still
    switch sections. (Not chosen: All / Installed filters on LT / RT.)
  - **What follows (to confirm in the demo):** one order everywhere: the home shows the page's
    list, all of it with six apps or fewer, the first five plus "All apps" beyond (so with six or
    fewer a missing web app moves after the store, where today it keeps its place dimmed; the demo
    shows both; **not kept**: the owner chose to keep it in its place, see the demo's review). "All apps" looks like "All games". Videos and Music opened from the page: B comes
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
     **Written (2026-11-20), approved by the owner (2026-11-21):** `design/demos/5.7-apps-page.html`
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
     **The owner's review (2026-11-20):** (1) **the built-in apps first** (Videos, Music, the store),
     then the web apps in the catalogue's order, so that Music and the store never leave the home;
     (2) **with six apps or fewer a missing app keeps its place**, dimmed (as today; the demo's
     switch R acted only with six apps and showed nothing with the nine it starts with: removed).
     With more than six, the installed apps still come before the missing ones on the page, and
     the home shows its first five. The demo is updated (code `d59e582`): with nine apps the home
     shows Videos, Music, Steam Store, Netflix, Spotify and "All apps"; with six, Videos, Music,
     Steam Store, Netflix, YouTube (missing, in its place), Spotify.
     **Then (owner, 2026-11-20): the home's five follow use once many apps are installed.** With
     six installed apps or fewer, the home's places are fixed (the order above); **from the
     seventh installed app, the home shows the five most used apps, the most used first**, and "All
     apps". The Apps page keeps the fixed order. Asked and answered: with six installed and one
     missing (seven in all) the home shows the first five of the fixed order, the sixth installed
     only on the page (not chosen: the most used as soon as the installed apps do not all fit); the
     uses are **every opening from the console, all time** (not chosen: the last 30 days); removing
     an app clears its count; equal counts follow the fixed order; Resume (bringing back the open
     app) is not an opening. The demo is updated (code `0388d2e`): with nine apps (seven installed)
     the home shows the five most used (invented counts listed under the demo, never shown on the
     console); opening an app counts and moves it, the selection following; removing one goes
     back to the fixed order; `#installed=` sets the web apps installed. Checked with scripted
     presses: six installed (fixed), eight installed (most used), the store opened up to Music's
     count (after Music, the fixed order).
     **Demo approved by the owner (2026-11-21)**, with the changes above (code `0388d2e`).
  2. **Code:** the theme (one ordered list for the home and the page, `AppTile.qml` out of
     `HomePage.qml`, the "All apps" tile, `AppsPage.qml` as a page of Home, B from Videos / Music
     back to where they were opened, texts); the pretend owneetd with a larger catalogue and
     preview steps; the frontend's tests and theme check; owneet-frontend 0.28.0.
     **Implemented (2026-11-21), waiting for the owner's test:** owneet-frontend 0.28.0 (no
     owneetd change: the catalogue and install / remove exist since 5.0.0).
     - **The order:** `foundation/apps.js` (plain functions, imported by the theme and tested with
       Node): the fixed order (`videos`, `music`, `store`, then `web:<id>` in the catalogue's order),
       the Apps page's (installed before missing), the home's six places (every app with six or
       fewer; beyond, the first five of the page's order while six or fewer are installed, the five
       most used from the seventh, then "All apps"), and the counts of removed apps cleared.
     - **The uses:** the shell counts an opening of a web app (owneetd's answer to the opening, not
       when it is brought back), of the Videos or Music page, of Steam's store (also from the
       welcome card and the library's "Add games"); kept in the theme's memory (`appUses`);
       cleared for apps no longer installed once the catalogue is known.
     - **The interface:** `AppTile.qml` (the home's tile, moved out of `HomePage.qml`, and "All
       apps"; larger on the page), `AppsPage.qml` (a page of Home: title and number of apps, five
       columns, the grid going round, the home grid's buttons, B back to the home on "All apps"),
       `HomePage.qml` (its places from `apps.js`, kept while an app is installed or removed; when
       they move the selection follows its app), `theme.qml` (`appsOpen`, Videos and Music back to
       where their tile was, also after the player). Texts (en, it): `home.all_apps`,
       `apps.title`, `apps.count`.
     - **Tests:** `frontend/owneet-frontend/tests/theme/apps.test.js` (six cases: the fixed order,
       six apps in place, the page, six installed with one missing, the five most used and their
       ties, removed counts), run by `tools/lint`; the frontend's suite and theme check (package
       build); the translations check.
     - **Preview:** the pretend owneetd's `@manyapps` (three invented web apps, seven installed):
       `tools/preview-steps/apps-page.txt` (the home's five and "All apps", the page, the row going
       round, YouTube installed and moved with the selection, options, Music opened from the page
       and back, Music opened four times first on the home) and `apps-six.txt` (today's six: the
       built-in apps first, the missing ones dimmed in place); `web-apps.txt` again (install and
       remove on the home). The previews that walk the home's tiles follow the new order.
     - **Code:** `b20c0ce` (theme, texts, tests), `99f634f` (tools), `aa1bc9f` (package).
     **Sub-step 2 passed the owner's test (2026-11-21)** in the test VM (cage, a Nacon GC-100),
     owner: "Everything works smoothly": today's six apps in the new order; with three invented web
     apps added to the VM's catalogue for the test (`/usr/share/owneet/apps.json`, its copy kept
     and put back afterwards) the home's five and "All apps", the Apps page, an app installed from
     it, the five most used from the seventh installed app, Videos / Music back to the page.
  3. **Close:** known limits, the hardware checks (batched with FrankenPC's), outcome; the owner
     approves.
     **Written (2026-11-21), waiting for the owner's approval:**
     - **Checked for the close:** the home's "All apps" ("Tutte le app") and the Apps page in
       Italian at the largest text size (XL): the names whole, the grid in two rows for nine apps
       (frontend preview, `@manyapps`).
     - **Licences and terms** ([[legal-compliance]]): nothing new. No component, service or
       content added; the tiles are generic letters (no logo); the invented web apps (Film Club,
       Podcasts, Radio) exist only in the demo, the pretend owneetd and the test VM's catalogue
       for the owner's test (put back afterwards), never shipped. The uses are counted on the
       console and never sent anywhere ([[product-invariants]]: no telemetry).
     - **Known limits of 5.7** (agreed: the first four; the others not told before):
       - The page appears only from the seventh app: with today's catalogue (Netflix, YouTube,
         Spotify) no console shows it, until more web apps or the programs of
         [[step-5.0.1-optional-gaming-apps]] come.
       - From the seventh installed app the home's tiles move as the apps are used; with six
         installed and some missing, the sixth installed app is only on the page.
       - The uses are counted for all time; removing an app clears its count; there is no other way
         to reset the order.
       - The page has no filters, sorting or search.
       - **Installed apps include Videos, Music and the store** (always there): the five most used
         take over the home when **four web apps** are installed (seven in all).
       - **What counts as a use:** a web app opened (not brought back with Resume; its first
         opening counts when owneetd accepts it, also if the user then leaves while Widevine is
         downloaded), the Videos or Music page opened, Steam's store opened from anywhere in the
         console (its tile, the welcome card, the library's "Add games"). Games never count.
       - The uses are kept by the interface on the console (its memory, with the other settings):
         a new installation of OwneetOS starts from zero.
       - **Guide shows the console where it was**, as for the Videos page (5.6): an app opened from
         the Apps page comes back to the Apps page (its tile with the green dot, A Resume), not to
         the home screen; B then goes to the home.
       - At the start, until owneetd answers (a moment), the home shows today's six; on a console
         with more apps it then changes to five and "All apps".
       - More apps than fit (three rows, fifteen apps; two rows at XL, ten): the grid scrolls with
         the selection and the right stick, not seen yet (nine apps at most in the preview).
       - When Steam becomes optional ([[step-5.0.1-optional-gaming-apps]]), the store's tile will
         have to follow its installed state (today it is always installed).
     - **To check at the next hardware test** (FrankenPC: gamescope, NVIDIA, a TV; with the open
       checks of [[step-5.1-brave-in-the-os]] to [[step-5.6a-command-legend]]): the home's tiles in
       the new order and the Apps page on the TV (sizes, text); in gamescope, an app opened from
       the page, Guide back to the page with the green dot, Resume; the order following real use
       (with a test catalogue of more web apps, as in the owner's test).
     - **Outcome:** the home's apps in a **fixed order, the built-in apps first** (Videos, Music,
       the store) then the web apps, a missing app dimmed in its place. **With more than six
       apps the home shows five and "All apps"**: the first five of the fixed order while six or
       fewer are installed (installed before missing), **the five most used from the seventh
       installed app** (each opening from the console counts, for all time; equal counts in the
       fixed order). **"All apps" opens the Apps page**, a page of Home: every app in a grid of
       larger tiles, five to a row, the installed ones before the missing ones, the grid going
       round; the home grid's buttons (A opens or installs, Menu its options, B back to the home
       on "All apps"); Videos and Music back to where they were opened. No owneetd change.
       Package: owneet-frontend 0.28.0. Verified with the Node tests of the order, the frontend's
       tests and theme check, the frontend preview (nine and six apps, XL in Italian) and in the
       test VM (cage, a Nacon GC-100) with a test catalogue of nine apps; the hardware checks wait
       for FrankenPC.
     - **Outside the step, for the owner:** at XL the settings' section list cuts "Controllers and
       Bluetooth" (from the close of 5.6a); owneetd's flaky `update` test (`TestCheckThenApply`);
       the guard hook blocking actions that only name the package build script; the lasting fix
       proposed for the builder VM's chroot in `/var/tmp` ([[build-chroot-emptied-by-tmpfiles]]).
