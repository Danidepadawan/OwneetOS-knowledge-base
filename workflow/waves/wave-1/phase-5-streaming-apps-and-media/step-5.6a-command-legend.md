---
type: step
description: "A legend of what each controller button does in the app on screen, opened by the user: a window over the app in gamescope, a full-screen page in cage."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.6a"
status: done
tags: [step, phase-5]
---
# 5.6a Command legend *(owner, 2026-10-31)*

Up: [[phase-5-streaming-apps-and-media]] · Status: **done** (owner, 2026-11-20; started 2026-11-18)

Added by the owner on 2026-10-31, after [[step-5.6-local-videos-and-music]] and before
[[step-5.7-apps-page]] (numbered like 4.2a–4.2c, so that no step is renumbered).

- **Deliverables:** the user can open a **legend of the controller's buttons for the app on
  screen**, so that every shortcut is within reach: the web apps' bindings of
  [[controller-input-map]] (a web app in general, "Inside YouTube", "Inside Netflix", "Inside
  Spotify"), and those of the apps that come later.
  - **In gamescope** (the standard session): a **window over the app**, which keeps running behind
    it (as the console's keyboard is drawn over a web page in gamescope).
  - **In cage** (the reduced session, which shows one window at a time): a **full-screen page** of
    the console's interface.
- **Related:** the quick menu's read-only "Controls and features" guide
  ([[step-3.13-start-up-animation-and-power-options]], [[quick-menu-and-startup]]) covers the
  console's own buttons; this legend covers the app's.
- **To decide when the step is planned** (with the owner): how the legend is opened (which button
  or path: a new binding goes into [[controller-input-map]] first, and the guard
  [[product-invariants]] keeps Guide owneetd's and LB / RB for sections); how it is closed; where
  its content comes from (one source for the console and the extension, so that the legend never
  disagrees with the bindings); its texts through the message files (en, it); games and Steam.
- **Demo first** ([[demo-before-code]]).
- **Agreed (owner, 2026-11-18)** ([[controller-input-map]], "The command legend"):
  - **View opens the legend** while a web app or the player is on screen. The app's own
    integration catches it (the console's extension: View, button 8, is unused by every site; the
    player's script), so the console still intercepts only Guide. View was reserved for
    screenshots ([[quick-menu-and-startup]]): it stays so on the console's own screens, and
    screenshots will take another gesture when they come.
  - **gamescope:** the legend **floats over the app**, not full screen, and the app keeps working
    under it (every button but View goes on to the app); **only View closes it** (B stays the
    app's back).
  - **cage:** a **full-screen page** of the console; **B or View** closes it, back to the app.
  - **No legend for games** (the console cannot know a game's buttons; a game reads every button).
  - **What follows:** the floating legend cannot be scrolled (the right stick is the app's), so it
    shows **the part for the screen the user is on** (Netflix's browsing pages, its title window
    or its player; a video or a song), and changes with it while open. **One data file** holds
    the legends (rows of buttons and a message), drawn by the console and checked by tests against
    the extension's and the player's bindings. Reused: the web keyboard's gamescope overlay (here
    without taking the controller), the extension's pause while the console's keyboard is open
    (cage only), the bridge path of `webapp.keyboard`, the player's control socket.
- **Sub-steps** (one per prompt, each tested by the owner):
  0. **Vault** (with sub-step 1): this note, [[controller-input-map]], [[quick-menu-and-startup]],
     the [[decision-log]].
  1. **Demo** `design/demos/5.6a-command-legend.html` ([[demo-before-code]]): the floating legend
     over a web app in general, YouTube, Netflix (browsing, title window, player), Spotify and the
     player (a video, a song) in gamescope, View opening and closing it while the app keeps
     working; the full-screen page in cage, B or View back to the app; texts (en, it), glyph sets.
     **Written and approved by the owner (2026-11-18):** `design/demos/5.6a-command-legend.html`
     (code `693376c`; its flows checked with scripted key presses: Netflix's legend following the
     browsing pages, the title window and the player; B in the app with the legend open; Guide;
     the cage page). What it adds beyond the decisions:
     - **the floating legend:** a panel at the top right (the palette's background, 90 %, a border),
       its title "Controls", the app's name and the screen (e.g. "The player"); the rows, then View
       "Close the legend" and Guide "Home"; when a legend does not fit (large text, a long legend),
       the panel widens to two columns;
     - **Guide closes it** on the way to the home screen (an overlay is drawn over whatever is on
       screen, so it would float over the console too);
     - **the cage page:** "Controls · {app}" and the screen, the rows in two cards, the prompts
       B / View "Back to {app}" and Guide "Hold: close {app}"; other buttons do nothing there;
     - **View's glyph**, new in the console: two overlapping squares (Xbox-style), a "CREATE" pill
       (PlayStation-style), a minus (Nintendo-style); R3 as a pill ("RS", "R3");
     - **texts without button names** (they read wrong with another controller): "the same button
       or Back: return", "after 0:05, previous goes back to the start".
  2. **Code:** the legends' data file and its texts (en, it); owneetd's legend state (`/v1/legend`,
     event `legend.changed`: toggled by the bridge and by the player's script; in cage the console
     shown and the app brought back, the player told to ignore its buttons meanwhile); the
     extension (View, the screen on show, the pause in cage); the player (`GAMEPAD_BACK`); the
     interface (the overlay in gamescope, the page in cage); tests (Go, the extension's, the
     frontend's, the data against the bindings); package versions.
     **Implemented (2026-11-19), waiting for the owner's test:** owneetd 0.19.0, owneet-frontend
     0.27.0, owneet-base 0.0.57 (the extension) ([[owneetd-api-legend]]).
     - **owneetd** (`daemon/internal/legend/`, `GET` / `POST /v1/legend`, event `legend.changed`):
       View toggles the legend of the app on screen for the screen on show; a web app's screen
       follows while it is open. gamescope: owneetd closes it when something else takes the screen
       (Guide) or the app exits. cage: owneetd shows the console for the page and brings the app back
       when it closes. owneet-bridge passes `legend` both ways; the player's script sends
       `owneet-legend` (`GAMEPAD_BACK` bound in `input.conf`).
     - **The extension:** View (button 8) sends the toggle with the screen's legend (each site's
       `legend()`: Netflix's player, title window or browsing rows, Spotify on its player pages,
       YouTube, otherwise `web`), sends the screen again when it changes while the legend floats
       over the page, waits under the console's page in cage and then ignores the buttons still
       held.
     - **The interface:** `Legend.qml`. gamescope: a panel at the top right in an external overlay
       window that never takes the controller, two columns when it does not fit. cage: a page in
       front, B or View (`Nav.isView`, the controller's SELECT) closes it. `foundation/legends.js`
       is the one source of the legends; View's glyph and R3's pill in `Glyph.qml`; texts (en, it).
     - **Tests:** Go (`legend`: over the app, the page, refusals, closing with the app; the API; the
       bridge's events; the player passing View on; `TestLegendMatchesBindings`: the player's legends
       against `input.conf`, skipped in the owneetd package build); the extension's
       `test/legend.test.js` (the legends a navigation names exist, Netflix's follow its screens,
       each app's legends name the buttons its navigation takes and only those); the frontend's
       suite and theme check (package build). Lint passes but for owneetd's old flaky `update`
       test, which passed when run again.
     - **Preview:** `tools/preview-steps/legend.txt` (gamescope: the panel for Netflix's player,
       Spotify's long legend, a song; closed) and `legend-cage.txt` (the page; X does nothing; B
       closes it), with the pretend owneetd's legend.
     - **Code:** `2c73d9f` (owneetd), `e8dd6bb` (extension), `f722794` (theme, texts), `5ac57e2`
       (tools), `49c2fdc` (packages).
     **Sub-step 2 passed the owner's test (2026-11-20)** in the test VM (cage, a Nacon GC-100):
     the legend's page for the player, Netflix's screens, YouTube and Spotify; B or View back to the
     app. Notes from the test: owneet-base 0.0.57 went in with `pacman -Udd` (the test VM has no
     `umu-launcher` or `dosbox-staging`, owneet-base's dependencies since step 4.5, and no package
     databases; its 0.0.56 ran without them too); the VM's controller passthrough sometimes drops a
     press (a press may need repeating), not the console's doing (owner: ignored for now).
  3. **Close:** known limits, the hardware checks (the floating legend over Brave and mpv in
     gamescope on FrankenPC: the test VM runs cage only), outcome; the owner approves.
     **Written (2026-11-20), approved by the owner (2026-11-20):**
     - **Checked for the close:** the floating legend at the largest text size (XL) in Italian, the
       longest legend (Spotify): two columns, the panel ends well above the bottom of a 720p screen
       (frontend preview, gamescope design).
     - **A problem found while writing the close, fixed (owner: "fix it", 2026-11-20):**
       gamescope draws **one external overlay at a time** (its source, `src/steamcompmgr.cpp`
       3.16.14: the most opaque one; [[gamescope-overlay-window-not-drawn-or-left-on-screen]]).
       The floating legend and the console's keyboard over a web page are both external overlays:
       with the legend open, A on a text field (Netflix's search) opens the keyboard, which takes
       the controller but may not be drawn (the legend stays in its place). **Fixed in owneetd
       0.19.1:** owneetd closes the floating legend when the console's keyboard opens
       (`webapp.keyboard`; not the cage page, under which the extension waits); Go test
       `TestClosesForTheKeyboard` (code `d3bad58`, `6c057b8`). Not seen in the test VM (cage has no
       overlays; the keyboard is a page there): checked at the next hardware test.
     - **Licences and terms** ([[legal-compliance]]): nothing new. No component, service or
       content added; View's glyphs are drawn for the console (shapes, no logo); the texts are the
       console's (en, it).
     - **Known limits of 5.6a** (agreed: the first three; the others not told before):
       - Only web apps and the player have a legend: not games, nor Steam (View is Steam's there).
         On the console's own screens View stays reserved; the quick menu's "Controls and features"
         covers the console's buttons.
       - gamescope: the panel covers the app's top-right corner until View closes it; it cannot
         be moved or scrolled (two columns when it is too tall).
       - The legend is the screen's as far as the app's navigation knows it: Netflix's browsing
         pages, title window and player; Spotify's player pages (elsewhere, sign-in for example,
         the general legend); one legend for YouTube. If Netflix changes its pages, the legend
         falls back to the general one, as its navigation would stop working too. A screen change
         reaches the open legend within a quarter of a second.
       - cage: the app keeps playing behind the page (a video or song goes on with its sound),
         unless it was paused before View.
       - PlayStation-style glyphs: View's pill reads "CREATE" (the DualSense's name); a
         DualShock 4 calls that button SHARE.
     - **To check at the next hardware test** (FrankenPC: gamescope, NVIDIA, a TV; with the open
       checks of [[step-5.1-brave-in-the-os]] to [[step-5.6-local-videos-and-music]]):
       - View in YouTube, Netflix (browsing, a title window, the player), Spotify and the player
         shows the panel at the top right; the app keeps working under it (moving, A, B, seeking;
         a video and its sound go on); the panel follows Netflix's screen while open; View closes
         it and it disappears completely (no last picture left);
       - Guide closes it on the way to the home screen; holding Guide closes the app and the panel;
       - A on Netflix's search field with the legend open: the legend closes, the keyboard is drawn;
       - View on a DualSense and a Switch controller (Brave's button 8 and mpv's `GAMEPAD_BACK`),
         with their glyph styles;
       - the panel over the player's own display and over the apps' top-right items; its size on
         the TV, and at XL;
       - in Steam and a game, View does nothing of the console's.
     - **Outcome:** **View, in a web app or the player, opens a legend of that app's buttons for
       the screen on show** (Netflix's browsing, title window and player; Spotify; YouTube; a video
       or a song; the general legend elsewhere). In gamescope it floats at the top right over the
       app, which keeps working under it (a window of the console that gamescope draws as an
       external overlay, never focused): only View closes it, Guide on the way home, and it closes
       with the app and when the console's keyboard opens over the page. In cage it is a page of the console, B or View back to the app. The app's own
       integration catches View (the console's extension; the player's script), so the console
       still intercepts only Guide. One data file holds the legends, drawn by the console and
       checked by tests against the extension's navigations and the player's bindings; texts in
       English and Italian; View's glyph in each style. Packages: owneetd 0.19.1, owneet-frontend
       0.27.0, owneet-base 0.0.57. Verified in the test VM (cage, a Nacon
       GC-100) and in the frontend preview (both designs, the largest text size); the floating
       panel waits for FrankenPC.
     - **Outside the step, for the owner:** at XL the settings' section list cuts "Controllers
       and Bluetooth" ("Controller e Bluetooth"), seen in this close's preview; owneetd's flaky
       `update` test (`TestCheckThenApply`, step 4.2b: it failed owneetd 0.19.1's first build, the
       second passed); the guard hook blocking actions that only name the package build script
       (from step 5.6; twice on 2026-11-20: a read-only search in it, and a command that only
       rewrote a line of a note naming the packaging tool, then made with the Edit tool); the builder VM's build
       chroot emptied by the system's cleaning of `/var/tmp`
       ([[build-chroot-emptied-by-tmpfiles]]: made again; a lasting fix proposed).
- **Step closed by the owner on 2026-11-20**, with the fix above (owneetd 0.19.1) and the hardware
  checks above as a follow-up. Next in the wave: [[step-5.7-apps-page]].
