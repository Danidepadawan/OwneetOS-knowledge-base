---
type: known-solution
description: "A game or emulator has no sound from its start, though its stream runs: closed earlier from the home screen while owneetd had it muted, WirePlumber remembered it muted and muted its next start."
status: solved
seen: 2026-11-26
updated: 2026-11-27
tags: [known-solution, audio, games, emulators]
---
# A program is silent after it was closed from the home screen

## Symptom

A game or an emulator starts and plays, full screen, with the controller, but **no sound at all**, from the first second.
Others are heard, and the same one had sound in an earlier test. The test log's sound section shows its stream
(`Stream/Output/Audio`) going to the right output, `state=running`; owneetd's journal never says "sound silenced
behind the home screen" for it, even when Guide brings the home screen in front. Seen with five of the user's own emulators
([[open-items]] 33, 34; [[step-4.9-the-users-own-emulators]]): three silent since the third test, two more in the fifth, whose
sound had worked before.

## Cause

WirePlumber remembers each program's stream volume and **mute** (by its application name, in
`~/.local/state/wireplumber/stream-properties`) and gives them back at its next start (`node.stream.restore-props`, on by
default; its script `node/state-stream.lua`). owneetd mutes a game's stream behind the home screen
([[game-sound-heard-behind-the-home-screen]], `daemon/internal/audio/silence.go`), and a game is mostly closed from there: the
stream ends muted, WirePlumber stores it muted, and the next start is muted before it plays. owneetd gives back only what it
muted itself, and mutes only a stream that is not muted yet: so it never touched it again, and the journal stays quiet.
Hard to see: the stream exists and runs, the program's sound libraries are complete, and nothing logs a mute.

## Solution

owneet-hardware 0.0.7: `52-owneet-streams-fresh.conf` in `/usr/share/wireplumber/wireplumber.conf.d/` sets
`node.stream.restore-props = false` (the key in WirePlumber 0.5.18; its online settings page names it `stream.restore-props`,
which this version does not read). A stream starts as its program asks; what was stored before is no longer read, so the
programs already remembered as muted are heard again. The output a stream was moved to is still remembered
(`node.stream.restore-target`). The console has no volume per program, so nothing is lost: the interface sets its sounds'
volume itself, owneetd only the output's. The test log (owneet-base 0.0.92) shows each stream's `mute` and volumes.

## How we found it

1. Fourth test: the silent ones never had a stream in the log (old log section) → the log was given every PipeWire client
   and stream (owneet-base 0.0.89, 0.0.90).
2. Fifth test: every silent emulator **had** a running stream to the HDMI output; the journal had "silenced" and "sound back"
   only for the ones heard, and none for the silent ones although Guide brought the home screen → their streams were already
   muted at start (`case silent && !s.Muted` in `silence.go`).
3. The two heard ones were closed from the home screen muted (silenced without "sound back"): the same path that had made the
   others silent before.
4. WirePlumber's state script (from its 0.5.18 package, in the builder VM): it restores `mute` from its store when a stream
   appears, gated by `node.stream.restore-props`.
5. Reproduced in the builder VM (PipeWire, WirePlumber, pipewire-pulse, removed afterwards): a stream muted with `pactl
   set-sink-input-mute`, ended and started again comes back **muted**; with the drop-in it comes back **unmuted**.

## Watch out

Anything that mutes or changes another program's stream (owneetd's silence, a mixer) is remembered by WirePlumber only while
`node.stream.restore-props` is on: never turn it back on. A program silent from its start with a running stream: read the
stream's `mute=` in the test log first.
