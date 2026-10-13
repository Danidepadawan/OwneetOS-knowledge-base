---
type: step
description: "QML client for the `owneetd` API and event stream (XMLHttpRequest or a small C++ plugin in the fork, decided in 3.1)."
phase: "[[phase-3-frontend]]"
step: "3.8"
status: done
legacy: "ROADMAP.md 3.8"
tags: [step, phase-3]
---
# 3.8 Frontend ↔ daemon bridge

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** QML client for the `owneetd` API and event stream (XMLHttpRequest or a small
  C++ plugin in the fork, decided in 3.1).
- **Outcome:** `owneet::Daemon` in the frontend (C++, `QLocalSocket`, `owneetd` in QML): requests
  with JSON and callbacks, the event stream with automatic reconnection. **Games start through
  owneetd** (each in its own systemd service, with its working folder: new optional `workdir` in
  `POST /v1/apps/launch`, owneetd 0.9.0) and end with `app.exited` (play time counted); without
  owneetd's socket the frontend still starts them itself (tests). The interface reads the
  controllers only while the home screen is on screen (`focus.changed`). **Home:** the running
  game takes the hero ("Now playing", time played; **Resume** in gamescope, **Close game** with a
  confirmation where Cancel is selected first), its cover says "Running"; a second game is refused
  with a translated message, and owneetd's error codes are translated (`error.*`). **Top bar:**
  controller battery and network (Wi-Fi with signal, or cable). Launch errors no longer use
  Pegasus's dialog. New test tool `owneet-testpad` (virtual controller, not in the image) and
  `vm/test.sh boot --tools DIR`. **Test VM:** cage — launch from the home screen, running game
  shown, Close game with confirmation, back to "Continue playing", cable icon; gamescope
  (headless) with the virtual controller — A starts the game and it comes to the front, Guide
  brings back the home screen with the game running, A on Resume shows it again, Close game ends
  it. Power actions through owneetd come with Settings (3.9).
- **Owner test (2026-10-09, NiPoGi, "diagnostics" entry = cage):** Home, Library (grid, filters,
  sort, Disks window), Appearance and language, Pro Controller (Nintendo prompts, A confirms) all
  work; holding Home 2 s closes a game in cage. Found: (1) the Pro Controller's battery was not
  shown: its driver gives only a level (full/high/normal/low/critical), not a percentage — the
  top bar now draws a battery icon filled by the level (the percentage next to it when known);
  (2) the network icon is hidden when not connected ("disconnected", as expected); (3) Guide and
  Resume cannot be tested in the diagnostics entry (cage) and the live system keeps nothing, so
  a new boot entry **"OwneetOS (test games)"** (`owneet.debug.test_games=on`, owneet-session
  0.0.12) starts the normal session with two test games (mpv test patterns). Checked in the test
  VM (gamescope, virtual controller). (4) A second controller cannot be paired while one is
  connected (automatic pairing only when none is): pairing from Settings → Controllers (3.9).
- **Owner test (2026-10-09, NiPoGi, "test games" entry = gamescope):** all passed — battery icon
  of the Pro Controller, a test game starts on screen, Guide shows the home screen with the game
  running, Resume brings it back, a second game is refused, Close game with confirmation.
