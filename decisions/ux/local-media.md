---
type: decision
description: "Videos and Music: the media folders on every disk, Music's two views, Guide keeping it playing, videos resuming where they stopped."
area: ux
status: active
decided: 2026-11-02
updated: 2026-11-04
tags: [decision, ux, media]
---
# Local videos and music

- **Media folders:** a folder named `Videos` or `Music`, or its name in the console's language
  (`Video`, `Musica`), at the top of any disk or USB stick and on the console's own disk, as the
  `Games` folder ([[games-on-disk]]). Everything inside counts, sub-folders included. Nothing else
  on the disks is searched.
- **Music has two views:**
  - **by folder:** the folders as they are on the disk;
  - **by artist and album:** built from the songs' own tags. It is read **only when the user
    enters that view**, with a spinner meanwhile. The tags are read by the frontend itself with
    FFmpeg's library (libavformat), both the file's and the stream's tags (Ogg keeps them in the
    stream), and kept in a list on the console's disk (owner, 2026-11-04).
- **Guide keeps it playing:** the player is an open app, like a game. Guide shows the home screen
  while the sound goes on, and Resume brings the player back. One app runs at a time.
- **Videos remember where they stopped:** a started video shows its progress, A resumes, and Menu
  has "Watch from the start". The positions are kept on the console's disk; the media disks are
  never written for this. Only the position is kept (never a track choice such as "no sound").
- **Music starts from the beginning** (owner, 2026-11-04): a song never resumes, and the rest of
  its folder or album plays after it.
- **Autoplay for videos** (owner, 2026-11-04): a switch, **on** on a new console and remembered on
  the console's disk. On: when a video ends, the next video of the same folder starts (after the
  last one, back to the list). Off: the video stops at its end and the player goes back to the
  list. It is switched with **Y in the Videos page** ("Autoplay: On / Off") and **Menu in the
  player** ([[controller-input-map]]). Music is not affected.
- **Previous goes back to the start first** (owner, 2026-11-04): LT in the first 5 s of a video or
  song goes to the previous one; from 0:05 on, to the start of the one playing.
- **The player is mpv** ([[architecture-stack]]). It reads the controller itself; Guide stays
  owneetd's ([[guide-button]]). Its bindings ("Inside the player") are in [[controller-input-map]].

## Why

- **The folders:** searching whole disks is slow on big ones and lists clips, samples and games'
  own files; the `Videos` / `Music` folders match the `Games` folder the user already knows.
- **Two Music views:** folders are quick on any disk and match how music is often stored (Artist /
  Album); the tags give the artist and album view when the folders are not tidy. Reading the tags
  only on entering that view keeps the folder view instant.
- **Guide:** pausing on Guide was the alternative; music that goes on while the user looks at the
  home screen is what a console's player does.
- **Resuming:** always starting from the beginning was the alternative. Songs are short and are
  listened to again from the start, so only videos resume.
- **Tags with FFmpeg's library:** running `ffprobe` for each song took 75 ms a song in the test VM
  (about 75 s for 1,000 songs), mostly starting the program; the library is already in the image
  with FFmpeg, so nothing is added.

## Creates

- Guards: none new ([[product-invariants]]: Guide owneetd's, nothing intercepted while the player
  is open; [[user-data]]: the media disks are not written).
- Steps: [[step-5.6-local-videos-and-music]]; moving media between disks is
  [[step-6.6-moving-games-and-media-between-disks]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-11-02 | Local videos and music (step 5.6): `Videos` / `Music` folders (or their translated names) at the top of every disk and on the console's disk; Music by folder and by artist and album, the second read only on entering it with a spinner; Guide keeps it playing, like an open app; videos resume where they stopped, Menu "Watch from the start". |
| 2026-11-04 | Step 5.6 sub-step 2: the player's bindings ([[controller-input-map]], "Inside the player"); music starts from the beginning and the rest of its folder or album follows; only a video's position is kept; the songs' tags read with FFmpeg's library inside the frontend in place of `ffprobe` (plan change, sub-step 4). |
| 2026-11-04 | Autoplay for videos: a switch, on by default and remembered (on: the next video of the folder starts; off: back to the list at the end), Y in the Videos page and Menu in the player; LT goes back to the start first (the previous one only in the first 5 s). |
