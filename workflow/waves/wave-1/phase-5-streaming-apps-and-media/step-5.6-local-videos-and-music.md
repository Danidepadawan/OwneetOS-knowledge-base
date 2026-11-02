---
type: step
description: "Mpv with gamepad bindings, Videos and Music browsing in the frontend from mounted disks."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.6"
status: in-progress
legacy: "ROADMAP.md 5.6"
tags: [step, phase-5]
---
# 5.6 Local videos and music

Up: [[phase-5-streaming-apps-and-media]] · Status: **in-progress** (started 2026-11-02)

- **Deliverables:** mpv with gamepad bindings, Videos and Music browsing in the frontend from mounted disks.
- **What is there at the start (2026-11-02):**
  - The home screen's Apps grid already has the **Videos** (▶) and **Music** (♪) tiles; A on them
    says "later" (`notYet()` in `frontend/owneet-frontend/src/themes/owneet/HomePage.qml`). Their
    names `app.videos` / `app.music` are in the message files.
  - **mpv and FFmpeg are already in the image** (`packages/owneet-session` depends on mpv) and in
    `CREDITS.md`; mpv is the chosen player, Kodi rejected ([[architecture-stack]]). No new
    dependency is expected: FFmpeg's `ffprobe` can read the songs' tags.
  - USB disks are mounted automatically, read only, since [[step-4.3-local-drm-free-games]]; full
    mounting is [[step-6.5-automatic-disk-mounting]]. The `Games` folder and its reading in the
    frontend (`DiskGamesProvider`, `owneet::DiskGames::folderNames`) are the pattern to follow.
  - owneetd runs a game or a web app one at a time (`daemon/internal/apps/apps.go`); the home
    screen shows the open one with Resume and Close.
- **Agreed (owner, 2026-11-02):** [[local-media]]:
  - **Media folders:** a `Videos` / `Music` folder (or its name in the console's language: `Video`
    / `Musica`) at the top of any disk or USB stick and on the console's own disk, as `Games`;
    everything inside, sub-folders included.
  - **Music has two views:** by folder (the folders as on the disk) and by artist and album (from
    the songs' tags), the second read **only when the user enters it**, with a spinner meanwhile
    (proposal: the console keeps the list, so later visits are quick).
  - **Guide keeps it playing:** the player is an open app like a game (Guide shows the home
    screen, Resume brings the player back, one app at a time).
  - **Videos remember where they stopped:** a started video shows its progress, A resumes, Menu
    has "Watch from the start"; mpv's own saved positions, kept on the console's disk (the media
    disks stay read only).
- **The guards here:** mpv reads the controller itself, so nothing but Guide is intercepted while
  it plays, and mpv never binds Guide (only OwneetOS's own mpv bindings, mpv's defaults off;
  [[product-invariants]]); the player's on-screen display takes its texts from the message files
  and its colours from the palette tokens; nothing needs the internet; nothing is written to a
  media disk; the test media is generated in the VM with FFmpeg (no copyrighted files).
- **Sub-steps** (one per prompt, each tested by the owner):
  0. **Vault** (with sub-step 1): this note, [[local-media]], the [[decision-log]].
  1. **Check in the test VM** (a probe, `vm/run/probe-5.6/`, never shipped): mpv's controller input
     with the virtual pad (the name mpv gets for each button, Guide left unbound, mpv's default
     gamepad bindings and turning them off); mpv full screen in gamescope and in cage, the sound,
     Guide → home → Resume; generated videos (H.264, HEVC, VP9, AV1 in mp4 and mkv, embedded and
     side `.srt` subtitles, two audio tracks) and songs (mp3, flac, ogg, m4a, with tags and an
     embedded cover); mpv's saved positions (`watch_later`) and reading a video's progress from
     them; `ffprobe` in the image, what it reads from the songs and its time per file. Decoding
     speed is not judged in the VM (software); the FrankenPC checks it.
     **Result (owner's test VM, cage, a Nacon GC-100 passed through, 2026-11-02):**
     - **Versions:** mpv 0.41.0 (SDL2 through `sdl2-compat` 2.32 on SDL3 3.4, LuaJIT), FFmpeg
       9.0.2 with `ffprobe`; mpv has `--input-gamepad`, `--save-position-on-quit`,
       `--watch-later-dir`, `--write-filename-in-watch-later-config`.
     - **The controller:** mpv reads it itself (`--input-gamepad=yes`); the console user can read
       the pad (`uaccess`). mpv's names: A `GAMEPAD_ACTION_DOWN`, B `ACTION_RIGHT`, X
       `ACTION_LEFT`, Y `ACTION_UP`, LB / RB `LEFT_SHOULDER` / `RIGHT_SHOULDER`, LT / RT
       `LEFT_TRIGGER` / `RIGHT_TRIGGER`, View `BACK`, Menu `START`, **Guide `GAMEPAD_MENU`** (SDL's
       Guide button: never bound), L3 / R3 `LEFT_STICK` / `RIGHT_STICK`, `DPAD_*`,
       `LEFT_STICK_*`, `RIGHT_STICK_*`. **mpv 0.41 binds no controller button by default** (its
       input test: "(nothing)" for every one). A held stick sends 3–4 presses a second.
     - **Seeking:** a relative seek goes to the nearest keyframe (−5 s jumped 3–9 s in files with a
       keyframe every 8 s): the player needs exact seeks (`--hr-seek=yes`).
     - **In cage:** full screen with `--vo=gpu-next,gpu,wlshm --gpu-context=wayland,waylandvk`
       (`gpu` in the VM), sound through PipeWire. No hardware decoding in the VM (VA-API, Vulkan
       and CUDA refused, as expected): the FrankenPC checks it. gamescope is not checked here (the
       VM has only headless gamescope): with the real player in sub-step 5.
     - **Formats:** H.264, HEVC, VP9 and AV1 in mp4 and mkv all decode. A side `.srt` with the
       video's name is loaded and shown by itself; embedded subtitles are found but not turned on;
       audio tracks come with their language and title.
     - **Saved positions:** owneetd's close (as the console closes an app) makes mpv quit cleanly
       and save; the next start resumes there (25.3 s). The file is named after the **MD5 of the
       video's full path** (upper case) and holds `start=`: the console reads a video's progress
       without mpv. mpv also saves the chosen tracks: the probe's X went through "audio off", so
       the resumed video was silent. To fix in the player: audio switches only between tracks,
       and what is saved is chosen (the position; never "audio off"). Songs got a saved position
       too. mpv also writes a tiny "redirect" file for each parent folder.
     - **Covers:** a song shows its embedded cover, or the folder's `cover.jpg`.
     - **The on-screen display:** a Lua script drew a text (accented letters included) and a bar
       in a colour given at start (`--script-opts`): the planned display works.
     - **Tags (`ffprobe`):** mp3, flac and m4a give title, artist, album artist, album, track and
       date in the file's tags; **Ogg Vorbis keeps them in the stream's tags** (read both); an
       untagged song has none (its folder and file names then). **75 ms per song** in the VM, one
       `ffprobe` per file (about 75 s for 1,000 songs), mostly starting the program.
  2. **Bindings, "Inside the player"** ([[controller-input-map]], with the owner, before any code),
     from what the check finds. Starting proposal: A pause / play; LT / RT −10 / +10 s (the map's
     repeat); D-pad left / right the same in small steps (music: previous / next song); Y
     subtitles, X audio track; Menu the player's options; B leaves the player (position saved);
     LB / RB never used; Guide owneetd's; the same on the keyboard fallback keys. In the Videos and
     Music pages: the map as it is, LT / RT switching Music's views (the map's "filter inside the
     page").
  3. **Demo** `design/demos/5.6-videos-and-music.html` ([[demo-before-code]]): Videos (folders as
     cards, a folder's videos, progress, Menu → "Watch from the start", covers from an image in
     the folder or generated, the empty page explaining the Videos folder); Music (the folder view,
     the artist and album view with its spinner on the first visit, the empty page); the player's
     screens (the video's on-screen display, music's now-playing screen); opened from their Apps
     tiles, B back home; in cage too.
  4. **Code, reading the media and the two pages:** a media reader in the frontend next to
     `DiskGames` (folder names and translations, a disk coming or going re-read quietly, covers,
     progress from the saved positions, tags read with `ffprobe` in the background on entering the
     artist view and kept in a list on the console's disk); the Videos and Music pages; the tiles
     open them; message files (en, it); tests.
  5. **Code, the player:** mpv's configuration shipped by OwneetOS (the bindings of sub-step 2,
     mpv's defaults off; its on-screen display as a small Lua script given the palette tokens and
     the translated texts by the console; saved positions on the console's disk); started through
     owneetd as an app that runs one at a time, like a game; package versions; tests (the launch,
     mpv's bindings never naming Guide).
  6. **Close:** known limits, the FrankenPC checks (hardware decoding, a Switch controller's buttons
     in mpv, a real USB disk of media), outcome; the owner approves the step.
