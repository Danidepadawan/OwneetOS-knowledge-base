---
type: technical-analysis
description: "API and design of the Videos and Music pages' player in owneetd (step 5.6): mpv with OwneetOS's configuration, one at a time like a game, the session file of its display, its control socket, the console over it."
component: owneetd
tags: [technical-analysis, owneetd, api, media]
---
# owneetd: the player (step 5.6)

Up: [[owneetd-design]] · Behaviour: [[local-media]], [[controller-input-map]] ("Inside the
player"), [[step-5.6-local-videos-and-music]] · Code: `daemon/internal/player/`,
`daemon/internal/api/player.go`, `daemon/player/` (mpv's configuration, installed in
`/usr/share/owneet/player/` by the owneetd package)

| Method | Path | What |
|---|---|---|
| GET | `/v1/player` | What plays: `{open, kind, index, count, path, title, folder, artist, album, position, duration, paused, autoplay, audio_language, subtitles, error}` (`kind` `videos` / `music`; `audio_language` / `subtitles`: the preferred languages as the player last chose them, `subtitles` also `off`; `error`: a file that could not be played). After the player has quit, the last state with `open` false |
| POST | `/v1/player` | Start the player: `{kind, items: [{path, title, folder, artist, album, hue}], index, from_start, autoplay, audio_language, subtitles, texts, languages, codes, look: {bg, surface, raised, line, fg, muted, accent, onAccent, displayFont, textFont, textScale, glyphs}}` → 201 with the state; a list of any length (the body up to 64 MiB). A player already open closes first (another video or song moves the player to it). Errors `player.invalid` (400), `player.not_found` (404: the file to play is gone), `apps.game_running` (409: a game or web app is open), `apps.no_session` (409), `player.failed` (502), `player.unavailable` (503) |

Events: `player.changed` (the state above, at the start, at every change the player reports and
at its end); its end is also `app.exited` with id `player`.

## How it works

- **One at a time, like a game:** the player is the app `player` of kind `media`
  (`apps.KindMedia`, exclusive with `game` and `webapp`): Guide shows the console while it plays
  (gamescope), Resume brings it back, the home screen's hero has Resume and Close; in cage
  holding Guide closes it.
- **The command** (`player.Args`): `mpv --config-dir=/usr/share/owneet/player`
  `--input-ipc-server=$XDG_RUNTIME_DIR/owneet/player.sock`
  `--script-opts=owneet-session=$XDG_RUNTIME_DIR/owneet/player.json`
  `--watch-later-dir=~/.local/state/owneet/watch_later`, `--profile=owneet-music` for songs, the
  session's output (as owneet-placeholder: `gpu-next,gpu,x11` under gamescope, `gpu-next,gpu,wlshm`
  with Wayland under cage), `--playlist=$XDG_RUNTIME_DIR/owneet/player.m3u --playlist-start=N`.
  The request's files, as given (clean absolute paths without line breaks, the first one must
  exist; the others mpv skips if they are gone), go to mpv in that playlist file: a list of any
  length (sub-step 5 had them on the command line and a cap of 5,000).
- **The session file** (`player.json`, 0600): the request's kind, files, texts, languages and look,
  with the session's mode (Guide's prompt: "Home" or "Hold: close"). The interface sends the texts
  already translated (placeholders such as `{t}` left for the script), the palette's tokens as
  `#RRGGBB`, the fonts, the text size and the controller's glyph set. Re-read after owneetd
  restarts while the player plays.
- **"Watch from the start":** owneetd deletes the first file's saved position (mpv's
  `watch_later` file: the MD5 of the path, in upper case) before mpv starts.
- **The control socket:** owneetd connects within half a second of the start (also after it
  restarts), reads the script's `owneet-state` messages (mpv's `client-message` events: index,
  path, position, duration, paused, Autoplay, error) and sends them on as `player.changed`.
- **The console over the player** (gamescope): mpv reads the controller itself through SDL, which
  delivers controller events even when mpv's window is not shown (mpv has no SDL window of its
  own). owneetd follows `focus.changed` and sends `script-message owneet-focus yes|no`; the
  script ignores the buttons while it is "no" (and stops held repeats). On connecting it sends the
  current focus at once.
- **Moving to another file:** the running player is closed (`apps.Close`: mpv saves the video's
  position as it quits), owneetd waits until it has ended (10 s, then kills it), then starts the
  new one.

## The configuration (`daemon/player/`)

- `mpv.conf`: mpv's own bindings, on-screen controller, scripts and `ytdl` off; full screen, a
  window for songs too; exact seeks; saved positions with the path line and the position only
  (`watch-later-options=start`: an empty list saves no position at all, mpv 0.41); each file
  starts with its own tracks and playing (`reset-on-next-file=pause,aid,sid`); songs' profile
  never resumes or saves. mpv uses a saved position up when the file opens and writes it again on
  quit (SIGTERM included); moving on at a file's end writes nothing.
- `input.conf`: the controller's and keyboard's keys of "Inside the player", each to a
  `script-binding owneet/…`; never Guide (`GAMEPAD_MENU`), View, LB / RB or the sticks
  (`bindings_test.go` checks it); `CLOSE_WIN quit` (owneetd's close and the window's). mpv's
  terminal input stays on: its SIGTERM handler belongs to it, and without it SDL swallows the
  signal ([[mpv-ignores-sigterm-with-a-controller]]).
- `owneet.lua`: the buttons' meanings (LT's 5 s, Autoplay through `keep-open`, audio never "no
  sound", subtitles off then each track, the preferred languages applied in mpv's `on_preloaded`
  hook before mpv chooses a video's tracks and reported in `owneet-state`, RT writing the position of a video left half-way, B
  quitting), the held-button repeat of [[controller-input-map]] (mpv's own repeat is one for every
  key), and the display drawn with libass on the console's 1280 × 720 grid. Text sizes allow for
  libass sizing fonts by their whole height (the OS/2 table's win metrics: 1.59 em for Lexend, 1.56
  em for Bricolage Grotesque). The console's fonts are on disk for it (`/usr/share/fonts/owneet/`,
  owneet-frontend package).
