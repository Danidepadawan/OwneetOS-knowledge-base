---
type: known-solution
description: "Reading the songs' tags took 78 ms a song in the test VM though FFmpeg's library needs 1 ms: QSaveFile waits for the disk at every file of a cache."
status: solved
seen: 2026-11-09
updated: 2026-11-09
tags: [known-solution, frontend, performance]
---
# Cache files slow to write in a VM

## Symptom

The Videos and Music pages' first reading of the songs ([[step-5.6-local-videos-and-music]]) took
78 ms a song in the test VM (`Media: read the tags of 5 songs in 390 ms`), as slow as running
`ffprobe` for each song, while the same code took about 1 ms a song in the builder VM's preview.

## Cause

`owneet::Media` saved each song's own picture and its list of details with `QSaveFile`, whose
`commit()` waits until the file is on the disk (an fsync). On a VM's disk image that takes tens of
milliseconds a file; in the preview the home folder is in memory, so it did not show there. The
list was saved the same way on the interface's thread, which can also make the screen stutter.

## Solution

owneet-frontend 0.24.1 (`44c2f6a`): files of a cache are written whole to `NAME.part`, then renamed
over `NAME` (`write_cache` in `src/backend/owneet/Media.cpp`), without waiting for the disk. The test
VM then read the songs in 1.6 ms a song (1.0 ms in the files).

## How we found it

FFmpeg's library alone was quick in the builder VM, so the time had to be outside it. The log line
was extended to give the time spent reading the files apart from the total (`… ms a song in the
files`); with the cache written without waiting, both dropped to about 1 ms.

## Watch out

`QSaveFile` is right for files that must survive a power cut (settings, the user's choices), wrong
for a cache written often or from a loop. Measure in the test VM, not only in the preview, whose
home folder is in memory.
