---
type: step
description: "OwneetOS packages copied by the owner into an `owneet-updates` folder on the OWNEETLOG stick (a command copies them from `out/repo`); a…"
phase: "[[phase-4-games]]"
step: "4.2b"
status: done
legacy: "ROADMAP.md 4.2b"
tags: [step, phase-4]
---
# 4.2b Updates from a USB stick *(owner, 2026-10-13)*

Up: [[phase-4-games]] · Status: **done**

- **Deliverables:** OwneetOS packages copied by the owner into an `owneet-updates` folder on the
  OWNEETLOG stick (a command copies them from `out/repo`); a tester system applies them
  **automatically at boot** when they are newer (a message on the start-up screen) and from
  Settings → System → Updates (with progress). A small privileged helper installs packages only
  from OwneetOS's repositories (the same helper serves the optional apps, 5.0, and the updates,
  7.1). Unsigned OwneetOS packages are accepted only on systems with the tester mark and only
  from the stick; Arch packages keep coming from the pinned snapshot online. Nothing published.
- **Outcome (2026-10-13):** `owneet-update` (root; check, apply, boot) with
  `owneet-update@check|apply.service` (polkit `50-owneet-update.rules`: only these, only start, only
  the console user) and `owneet-update-boot.service` (before the console), owneet-base 0.0.26;
  owneetd 0.11.7 `/v1/update` and `update.changed`; Settings → System → Check for updates on
  tester systems (owneet-frontend 0.16.4; tester-only, no demo: the users' updates get theirs in
  7.1); `tools/make-update-stick`; `vm/test.sh boot --stick IMAGE`. Checked in the test VM with an
  OWNEETLOG stick image: the installer does not offer the stick; Settings found and installed
  owneet-base 0.0.24 → 0.0.25; at start-up 0.0.25 → 0.0.26 and, offline with no Arch package
  lists, 0.0.26-1 → 0.0.26-2, the console starting afterwards. Fixed on the way: the test log
  service mounts the stick at the same moment (the update uses its mount); pacman refused to
  install without Arch's package lists (now the stick alone first, Arch online only if needed).
- **FrankenPC (owner, 2026-10-13):** owneet-base 0.0.27 installed from the stick at start-up.
  Found in the test VM before the next stick: at start-up, an update that contains a user service
  (e.g. owneetd) waited for ever on pacman's hook that reloads the users' systemd (which waits for
  the update itself). owneet-base 0.0.29 turns that hook off at start-up only and removes a
  pacman lock left by an update cut short; checked in the test VM (owneetd updated at start-up,
  the console starting afterwards). Systems with an older owneet-base take such an update from
  Settings → System instead (stick plugged in after the console has started).
- **Steam on the FrankenPC (owner, 2026-10-13):** Steam stayed in English → it starts in the
  console's language (`-language`, owneetd 0.11.8); garbled, stale pictures in Steam with the
  NVIDIA driver → Steam draws its pages without the GPU there (`-cef-disable-gpu`, owneetd 0.11.9;
  games keep the GPU); Steam built the `en_US.UTF-8` locale again at every start → the system
  has it (and `it_IT.UTF-8`, owneet-base 0.0.28). Second test: Italian confirmed, no glitches
  this time, about 30 s to start: Steam had been killed at shutdown and checked all its files
  (7 s) → owneetd closes Steam cleanly, at shutdown too (owneetd 0.11.10). Third test: glyph
  strips and copies of Steam's own pictures, in some sessions only (2 of 3), with Steam drawing
  without the GPU and nothing in the logs; Steam still killed at shutdown (the console session
  stopped with it) → shutdown and restart close the apps first and wait for them (owneetd
  0.11.11); test switches in `owneet-debug.txt` on the OWNEETLOG stick (owneet-session 0.0.16),
  first try: gamescope without explicit sync. Fourth test: explicit sync off changes nothing
  (glyphs again, and Steam flickering over the console's home screen at the bottom); the glyphs
  disappear while a game runs (Hollow Knight: Silksong played fine) → suspected: a Steam window
  shown above everything but never drawn (on NVIDIA its memory keeps old pictures); the test log
  lists the windows every 10 s when `owneet-xprobe` is on the stick (owneet-base 0.0.31). Also
  found: choosing the running game in the library said "another game is running" → it goes back
  to the game, as on the home screen (owneet-frontend 0.16.6). Fifth test (5 starts): Steam
  now closes cleanly at shutdown ("Verifying file sizes only"); glyphs in 3 of 5 starts, for
  1–10 s after Steam appears and once when going back home; the window lists show only the
  console and Steam's own window (32-bit, with transparency): no hidden window → most likely
  Steam's window buffers shown before they are drawn (new memory is not cleared on NVIDIA).
  Next try: `owneet.debug.gamescope_composite=off`. Also: Steam games with play time showed
  "never played" (Steam gives no play count) → fixed (owneet-frontend 0.16.7). **Open, blocks
  delivery (owner, 2026-10-13):** a few test starts prove nothing; the glyphs are not bound to
  a time. With composition off (Steam's buffers sent straight to the screen) greenish rectangles
  showed almost all the time: another NVIDIA symptom of that mode (like the RTX 4060's black
  rectangles), not the glyphs. Suspected for the glyphs: Xwayland's GPU drawing (Glamor) with
  the NVIDIA driver. Test switch `owneet.debug.xwayland_glamor=gl|es|off` (Xwayland through
  `owneet-xwayland`, gamescope's `WLR_XWAYLAND`; owneet-session 0.0.17), with the normal
  composition. The owner photographs every occurrence. Glamor on OpenGL ES: greenish blocks on
  Steam's still empty window. Every picture seen so far is a leftover of something Xwayland drew
  before (Steam's start-up spinner, glyph strips, Steam's own pictures): Steam's window has no
  background (X11's default), so a new window shows whatever its new memory held until Steam
  has drawn it all, and the NVIDIA driver does not clear that memory → owneetd gives every app
  window a background as soon as it is shown and clears it, asking the app to draw it again
  (owneetd 0.11.12). Not enough: glitches in 1 of 2 starts while Steam's side menu opened and
  closed (one Steam window, never resized: parts of an already drawn window go wrong; a copy of
  Steam's top bar lower down, a shrunken copy of the screen). Next: Xwayland without Glamor.
  The owner noticed (normal settings) that the glitches change at every frame Steam sends and
  slow down as Steam stops redrawing: a sign of the compositor reading Steam's frames before
  Xwayland has finished them (synchronisation). Also found: Back from the first page Steam
  opened on left Steam loading for ever → Steam starts on its own home page and gets the page
  once it is shown (gamescope; owneetd 0.11.13). Glamor off froze the console's own start-up
  (no OpenGL for X11 programs) → with that switch the console draws itself in software
  (owneet-session 0.0.18). The owner points out that the FrankenPC showed no glitches while it
  ran the live system: "NVIDIA only" rested on live tests (the NiPoGi was never installed, and
  the NiPoGi too had glitches at Steam's start, hidden by the settling time) → same-trigger
  comparison live/installed with a new ISO carrying every fix so far.
- **Same ISO, same trigger (owner, 2026-10-14):** NiPoGi live (AMD Barcelo) clean; FrankenPC live
  (GTX 1660 Super) glyphs, shifted copies of Steam's pages, green noise blocks; no driver error in
  the logs (no Xid). The glitches are **NVIDIA-only**, live or installed alike. Glamor off: the
  console's own window is shown but gamescope never updates the screen (the frontend works in
  software on Xvfb), so that test cannot be done there. Test switches added
  `owneet.debug.xwayland_protocol=sync` and `owneet.debug.nv_explicit_sync=off`
  (owneet-session 0.0.19). **Owner's conclusion:** whatever the test, the glitches stay; it is a
  known problem of X11 windows with the NVIDIA driver, not reported upstream for now. The way out
  is to keep Steam's own interface off the screen: [[step-4.2c-steam-without-its-interface]].
- **Approved by the owner (2026-10-14)** after the FrankenPC tests (installed, started from its disk, several updates applied from the stick at start-up and from Settings).
