---
type: known-solution
description: "The player does not close when Guide is held (or Close is chosen): mpv ignores SIGTERM when its terminal input is off and it reads the controller, because SDL takes the signal."
status: solved
seen: 2026-11-11
updated: 2026-11-11
tags: [known-solution, player, mpv]
---
# mpv ignores SIGTERM when it reads the controller

## Symptom

Holding Guide in cage over the player (or Close on the home screen's hero) does not close it.
owneetd logs `Guide held: closing the app on screen` and `closing app` with `id=player`, and about
10 s later `app exited id=player result=timeout`: systemd killed it at the end of its stop timeout.
A video then loses its position (nothing new in `~/.local/state/owneet/watch_later`).

## Cause

owneetd closes an app by stopping its systemd unit, which sends SIGTERM. mpv quits on SIGTERM
through a handler that belongs to its **terminal input**: with `input-terminal=no` mpv installs
none. With `input-gamepad=yes` mpv starts SDL for the controller, and SDL installs its own SIGTERM
handler where none is set (it turns the signal into an SDL quit event, which mpv never reads). So
the signal is swallowed and mpv keeps playing until systemd's SIGKILL.

## Solution

Keep mpv's terminal input on (`daemon/player/mpv.conf` does not set `input-terminal=no`; under
systemd mpv reads no terminal anyway), so its own handler is in place before SDL starts: SIGTERM →
`CLOSE_WIN` → `quit` (bound explicitly in `input.conf`, not through owneet.lua, which ignores the
buttons while the console is over the player), and the video's position is saved. owneetd 0.17.1.
`daemon/internal/player/bindings_test.go` fails if `input-terminal` is turned off again, and
`tools/preview-steps/player-close.txt` checks the close (`tools/player-preview`).

## How we found it

[[step-5.6-local-videos-and-music]], sub-step 5, the owner's test (2026-11-11): the journal above.
The same delay had shown in the builder VM's container two days before (mpv still running a
minute after `kill`). In the container: with `input-terminal=no`, still running 15 s after SIGTERM
and nothing saved; without it, quit after 1 s with the position saved.

## Watch out

Any mpv (or other SDL program) started by owneetd with a controller and without its own SIGTERM
handler: test that owneetd's close actually ends it, not systemd's timeout.
