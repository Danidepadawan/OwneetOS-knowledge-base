---
type: decision
description: "Videos and Music: the media folders on every disk, Music's two views, Guide keeping it playing, videos resuming where they stopped."
area: ux
status: active
decided: 2026-11-02
updated: 2026-11-02
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
    enters that view**, with a spinner meanwhile.
- **Guide keeps it playing:** the player is an open app, like a game. Guide shows the home screen
  while the sound goes on, and Resume brings the player back. One app runs at a time.
- **Videos remember where they stopped:** a started video shows its progress, A resumes, and Menu
  has "Watch from the start". The positions are kept on the console's disk; the media disks are
  never written for this.
- **The player is mpv** ([[architecture-stack]]). It reads the controller itself; Guide stays
  owneetd's ([[guide-button]]). Its bindings are in [[controller-input-map]].

## Why

- **The folders:** searching whole disks is slow on big ones and lists clips, samples and games'
  own files; the `Videos` / `Music` folders match the `Games` folder the user already knows.
- **Two Music views:** folders are quick on any disk and match how music is often stored (Artist /
  Album); the tags give the artist and album view when the folders are not tidy. Reading the tags
  only on entering that view keeps the folder view instant.
- **Guide:** pausing on Guide was the alternative; music that goes on while the user looks at the
  home screen is what a console's player does.
- **Resuming:** always starting from the beginning was the alternative.

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
