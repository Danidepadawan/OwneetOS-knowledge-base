---
type: step
description: "A legend of what each controller button does in the app on screen, opened by the user: a window over the app in gamescope, a full-screen page in cage."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.6a"
status: in-progress
tags: [step, phase-5]
---
# 5.6a Command legend *(owner, 2026-10-31)*

Up: [[phase-5-streaming-apps-and-media]] · Status: **in-progress** (started 2026-11-18)

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
  2. **Code:** the legends' data file and its texts (en, it); owneetd's legend state (`/v1/legend`,
     event `legend.changed`: toggled by the bridge and by the player's script; in cage the console
     shown and the app brought back, the player told to ignore its buttons meanwhile); the
     extension (View, the screen on show, the pause in cage); the player (`GAMEPAD_BACK`); the
     interface (the overlay in gamescope, the page in cage); tests (Go, the extension's, the
     frontend's, the data against the bindings); package versions.
  3. **Close:** known limits, the hardware checks (the floating legend over Brave and mpv in
     gamescope on FrankenPC: the test VM runs cage only), outcome; the owner approves.
