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
    dependency is expected: FFmpeg can read the songs' tags (its library, sub-step 4).
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
     **Agreed (owner, 2026-11-04):** [[controller-input-map]], "Inside the player": the same
     buttons for a video and a song; A pause / play; **D-pad left / right −10 / +10 s**, exact;
     **LT / RT the previous / next video or song** (the owner swapped them: the proposal had LT /
     RT seeking and the D-pad in small steps); X the next audio track (never "no sound"); Y
     subtitles (off, then each track); B leaves the player, back to the list (a video's position
     saved); every press shows the on-screen display, the buttons without a meaning only show it;
     the sticks do nothing; View and LB / RB not bound; Guide never bound by mpv; mpv's defaults
     off; the same on the keyboard. **Music starts from the beginning** (a song never resumes; the
     rest of its folder or album plays after it) and only a video's position is kept
     ([[local-media]]). **Plan change:** the songs' tags are read by the frontend with FFmpeg's
     library in place of `ffprobe` (sub-step 4 below). **Then (owner, 2026-11-04):** an
     **Autoplay** switch for videos, on by default and remembered (on: the next video of the folder
     starts when one ends; off: back to the list), switched by Y in the Videos page and Menu in the
     player; **LT goes back to the start first** (to the previous video or song only in the first
     5 s).
  3. **Demo** `design/demos/5.6-videos-and-music.html` ([[demo-before-code]]): Videos (folders as
     cards, a folder's videos, progress, Menu → "Watch from the start", covers from an image in
     the folder or generated, the empty page explaining the Videos folder); Music (the folder view,
     the artist and album view with its spinner on the first visit, the empty page); the player's
     screens (the video's on-screen display, music's now-playing screen); opened from their Apps
     tiles, B back home; in cage too.
     **Written and approved by the owner (2026-11-04):** `design/demos/5.6-videos-and-music.html`
     (on the approved home and library demos; its player's rules checked with scripted key
     presses: LT's 5 s, Autoplay at the end, Guide, B). What it adds beyond the decisions,
     approved with the demo ([[local-media]]):
     - **Videos:** a **"Continue watching"** row (started videos, the latest first) above the
       folders; 16:9 cards; a folder opens as a list beside its picture (its `cover.jpg` /
       `folder.jpg`, a season using its series' picture, or one drawn from its name), with the
       selected video's audio and subtitle languages and where it stopped; the disk's name on the
       cards when two disks have media; Y "Autoplay: On / Off" in the page's head.
     - **Music:** square cards; a folder of songs or an album as a list (the artist under each song
       only in a folder of several artists); Artists → an artist's albums → the songs; untagged
       songs under "Unknown artist", their file's name as the title and their folder as the
       album; the spinner counts the songs read ("12 of 24").
     - **While the player is open:** another video or song moves the player to it (a game open:
       "{name} is open: close it first."); Guide (gamescope) shows the console where it was, the
       item marked "Playing" (A on it resumes), the home screen's hero with Resume and Close, the
       Videos or Music tile with the green dot; in cage holding Guide closes the player, back to
       the list.
     - **Positions:** mpv's own behaviour, a video's saved position used up when it opens and saved
       again when it is left; a video watched to the end shows as not started; previous / next
       resume a started video. A `.srt` beside the video shows by itself (mpv's own); embedded
       subtitles start off.
     - **The player's display:** the folder and the title, the progress and the times, the Audio /
       Subtitles / Autoplay states with their buttons, the prompts (in cage, Guide "Hold: close");
       short messages at the top ("Resumed at 12:04", "+10 s", "Back to the start", "Audio:
       Italian (2 of 2)"); the subtitles move up while it shows; paused, it stays. Music's screen:
       the picture, title, artist, album, progress and the next song.
     - **A USB disk removed while it plays:** the player stops (the position kept) with "The USB
       disk was removed: {title} stopped."; otherwise the pages change quietly.
  4. **Code, reading the media and the two pages:** a media reader in the frontend next to
     `DiskGames` (folder names and translations, a disk coming or going re-read quietly, covers,
     progress from the saved positions, tags read in the background on entering the artist view and
     kept in a list on the console's disk); the Videos and Music pages; the tiles open them; message
     files (en, it); tests. **The tags are read with FFmpeg's library (libavformat) inside the
     frontend** (owner, 2026-11-04, in place of one `ffprobe` per song, 75 ms each in sub-step 1):
     the file's and the stream's tags; FFmpeg is already in the image and in `CREDITS.md`
     (GPL-3.0-only as packaged, which the frontend's GPLv3 allows); its time per song measured
     here.
     **Implemented (2026-11-09), waiting for the owner's test:** owneet-frontend 0.24.0 (`ffmpeg`
     now a dependency; `CREDITS.md`).
     - **The reader** `owneet::Media` (`src/backend/owneet/Media.cpp`, `media` in QML): the
       `Videos` / `Video` and `Music` / `Musica` folders at the top of every disk and in the home
       folder; a folder is listed at once, its files' details (length, audio and subtitle
       languages, tags, a song's own picture) read in a background thread, the folder on screen
       first, and kept in `~/.cache/owneet/media.json` (the songs' pictures in
       `~/.cache/owneet/media-pictures/`); subtitle files beside a video by their names; names in
       a person's order, written in the reader (Qt's collator ignores numbers in the C locale);
       a disk coming or going changes the pages quietly (Storage's signal).
     - **Saved positions:** read from `~/.local/state/owneet/watch_later`, mpv's files named
       after the MD5 of the video's path. The player (sub-step 5) writes there, with the video's
       path on the first line (`--write-filename-in-watch-later-config`), which "Continue
       watching" needs.
     - **The theme:** `MediaPage.qml` (both pages), `MediaCard.qml`, `MediaRow.qml`, `MediaText`
       (times, language names: `lang.*` messages, else the language's own name); the tiles open
       the pages, B goes back up to the tile; Autoplay kept in the theme's memory. A on a video or
       song says "later" until sub-step 5. `GameArt` fixed: a picture another art had loaded
       first was drawn as art (Qt gives no signal for it).
     - **Tests:** `test_Media` (the folders, the order of names, a season's picture, subtitle
       files, saved positions and Continue watching, tags read from WAV files with FFmpeg,
       artists and albums, the kept list). **Preview:** `tools/preview-steps/media.txt` and
       `media-empty.txt`, with `@media` (an invented USB stick made with FFmpeg in
       `tools/frontend-preview`).
     - **Time per song (the tags):** 0.5–1.4 ms in the builder VM (`ffprobe`: 75 ms in the test
       VM, sub-step 1). **The owner's test (2026-11-09):** both pages work as in the demo; the
       test VM read 5 songs in 390 ms, 78 ms a song, no quicker than `ffprobe`. Likely cause:
       QSaveFile waits for the disk at every file of the cache (a song's own picture, the list),
       slow on a VM's disk. owneet-frontend 0.24.1 writes the cache without waiting and logs the
       time spent in the files alone. **Measured again (owner, 2026-11-09): 1.6 ms a song, 1.0 ms
       of it in the files** (5 songs in 8 ms; [[cache-files-slow-to-write-in-a-vm]]). (The
       frontend's log file keeps information lines in memory: the time is read from the journal,
       `journalctl -t owneet-cage`.)
     **Sub-step 4 passed the owner's test (2026-11-09)** with owneet-frontend 0.24.1.
     - **While building:** the PC went to sleep twice during a package build
       ([[builder-vm-stops-after-the-host-sleeps]]).
  5. **Code, the player:** mpv's configuration shipped by OwneetOS (the bindings of sub-step 2,
     mpv's defaults off; its on-screen display as a small Lua script given the palette tokens and
     the translated texts by the console; exact seeks; saved positions on the console's disk, a
     video's position only, never for songs; to check: whether mpv still acts on the controller
     while the console is over it in gamescope, and if so the script ignores the buttons until the
     player is on screen again); started through
     owneetd as an app that runs one at a time, like a game; package versions; tests (the launch,
     mpv's bindings never naming Guide).
     **Implemented (2026-11-10), waiting for the owner's test:** owneetd 0.17.0 (`mpv` now a
     dependency of it), owneet-frontend 0.25.0 ([[owneetd-api-player]]).
     - **The player's files** (`daemon/player/`, installed in `/usr/share/owneet/player/`):
       `mpv.conf` (mpv's own bindings, on-screen controller, scripts and `ytdl` off; exact seeks;
       saved positions with the path line and the position only; each file with its own tracks;
       songs' profile never resumes or saves), `input.conf` ("Inside the player", controller and
       keyboard, never Guide, View, LB / RB or the sticks), `owneet.lua` (the buttons' meanings,
       the map's repeat timing, the display drawn with libass from the console's texts, palette,
       fonts and glyphs).
     - **owneetd** (`daemon/internal/player/`, `GET` / `POST /v1/player`, event `player.changed`):
       the player is the app `player` of kind `media`, one at a time with games and web apps;
       owneetd writes the session file, builds the command, forgets a saved position for "Watch
       from the start", closes a player already open before another starts, follows the script
       through mpv's control socket and tells it when the console is on screen over it.
     - **Found while building it:**
       - mpv 0.41 saves no position at all with an empty `watch-later-options`: the list is
         `start`.
       - mpv uses a saved position up when the file opens (the file is deleted) and writes it
         again on quit, SIGTERM included; moving on at a file's end writes nothing. RT on a video
         left half-way writes its position (`write-watch-later-config`).
       - **mpv acts on the controller while the console is over it:** it reads the controller
         through SDL without an SDL window, and SDL then delivers controller events even when
         another app is on screen. So the check planned here was settled in the design: owneetd
         sends `owneet-focus` from `focus.changed`, and the script ignores the buttons while the
         console is on screen (checked in the preview; the real check is in gamescope, below).
       - libass sizes text by the font's whole height (OS/2 win metrics: 1.59 em Lexend, 1.56 em
         Bricolage Grotesque); the console's fonts are now also installed on disk
         (`/usr/share/fonts/owneet/`, owneet-frontend) for mpv.
       - mpv's plain X11 output ignores the background colour: the song screen draws its own
         background around the picture.
     - **The interface:** A on a video or song starts the player with the rest of its folder or
       album (Autoplay, the texts, the palette, the language names sent each time); what plays is
       marked "Playing" on the pages (A brings the player back, no Menu on it; a video playing is
       first in Continue watching, its progress live); the home screen's hero shows it with its
       time, Resume and Close (Close at once, "{title} closed"), its tile a green dot; Autoplay
       switched in the player follows on the page; when the player closes the console is back on
       the list it was opened from, on what played last; a file that could not be played and a
       USB disk removed while it plays are said (`player.failed`, `toast.usb`). New texts (en,
       it): the player's prompts, states and messages, `media.playing`, `toast.closed`,
       `toast.usb`, `error.player`. Beyond the demo: a file that cannot be played moves on to the
       next with "{title} could not be played." (the last one: said by the console).
     - **Tests:** Go (`player`: the command, the session file, refusals, moving the player,
       following its socket and the focus; `bindings_test.go`: never Guide, View, LB / RB or the
       sticks, every binding known to the script, mpv's defaults off; the API), `test_Media`
       (language codes, files present).
     - **Preview:** `tools/player-preview` runs the real mpv with these files in a container of
       the builder VM (Xvfb, invented media made with FFmpeg), presses buttons through mpv's
       control socket, and prints the script's state and the saved positions:
       `player-video.txt`, `player-music.txt`, `player-autoplay.txt`. Checked there: resuming a
       saved position, the display gone after 4 s, pause, ±10 s, audio tracks ("Audio: Italian (2
       of 2)", never "no sound"), subtitles off then each, Autoplay on (the next episode, the end
       not saved) and off (the player closes at the end, nothing saved), LT's 5 s, RT saving the
       position, Escape saving it, the buttons ignored with the console over the player; songs
       with the folder's `cover.jpg`, their own picture, drawn art, the last song, nothing saved.
       The frontend preview (`media-player.txt`, `media-player-music.txt`; the pretend owneetd now
       "plays") shows the pages and the hero with the player open, and Close.
     - **Code:** `9150828` (owneetd), `85b0cbe` (the reader), `79a3c2a` (theme, texts), `9a49168`
       (tools), `cbf1393` (packages, credits).
     - **The owner's test (2026-11-11), first finding:** holding Guide did not close the player
       (owneetd's close, then `result=timeout` 10 s later): mpv ignored SIGTERM, because
       `input-terminal=no` removed its handler and SDL, started for the controller, took the
       signal ([[mpv-ignores-sigterm-with-a-controller]]); a video also lost its position. Fixed in
       **owneetd 0.17.1** (mpv's terminal input on, `CLOSE_WIN quit` bound, a test and
       `player-close.txt`); mpv's warnings for the buttons left unbound (Guide, View) no longer
       logged at every press.
       **Confirmed by the owner (2026-11-11):** with owneetd 0.17.1 holding Guide closes the
       player.
     - **The rest of the owner's test passed (2026-11-11):** the display and every button, resuming
       and "Watch from the start", Autoplay on and off, songs and their pictures, Continue
       watching after Guide held. **One change asked (owner, 2026-11-11):** Autoplay on the same
       button inside and outside the player: **Y switches Autoplay in the player too, Menu cycles
       the subtitles** (X stays audio; [[controller-input-map]], [[local-media]],
       [[decision-log]]); the approved demo is updated to match.
     - **While building:** owneetd's `update` package has a flaky test (`TestCheckThenApply`:
       its fake rewrites the state file while the manager polls it; 6 failures in 150 runs),
       older than this step; reported to the owner.
  6. **Close:** known limits, the FrankenPC checks (hardware decoding, a Switch controller's buttons
     in mpv, a real USB disk of media; in gamescope, which the test VM does not have: Guide → the
     console with the sound going on → Resume, and the player's buttons doing nothing while the
     console is over it), outcome; the owner approves the step.
