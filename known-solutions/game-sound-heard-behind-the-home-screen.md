---
type: known-solution
description: "A game left behind the home screen with Guide is still heard: its sound stream (PipeWire's ALSA plugin, 32-bit games) has no process id, only its client has one, so owneetd could not tell whose it was."
status: solved
seen: 2026-11-11
updated: 2026-11-11
tags: [known-solution, audio, games]
---
# A game's sound is heard behind the home screen

## Symptom

FrankenPC, 2026-11-11, The Witcher 2 (GOG, Linux, 32-bit): Guide brings the home screen back and the game's sound goes on.
In owneetd's log there is "on screen focus=home" but no "sound silenced behind the home screen". Windows games and Steam
games went silent as decided on 2026-11-09.

## Cause

owneetd silences a game behind the home screen by muting each sound stream whose process belongs to the game
(`audio.ApplySilence`, `apps.SilentNow`), and it read the process from the stream's `application.process.id`. A
32-bit game plays through ALSA, and PipeWire's 32-bit ALSA plugin gives its stream no process id
(`pactl list sink-inputs`: "PipeWire ALSA [witcher2]", no `application.process.id`); the stream's **client** has it
(`pactl list clients`: `application.process.id`, `application.process.binary = "witcher2"`). With no process, the
stream was never the game's.

## Solution

owneetd 0.25.25 (`daemon/internal/audio/silence.go`): a stream without a process id takes its client's
(`clientPIDs`, the clients listed once per pass, only when a stream needs it); Go test `TestClientPIDs`.

## How we found it

1. The test log: no "sound silenced" line after Guide.
2. Test VM: `witcher2` started through owneetd, then `pactl list sink-inputs` within its first seconds: the stream has
   no process id; `pactl list clients`: its client has the game's pid.

## Watch out

- Any program that plays through ALSA or another layer may give its process id only on the client.
- The test VM runs the reduced (cage) session, where a short Guide does nothing: the silence after Guide is only
  seen on hardware.
