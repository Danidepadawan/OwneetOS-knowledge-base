---
type: step
description: "PipeWire: volume, mute, output selection (speakers, HDMI, headset)."
phase: "[[phase-2-system-daemon]]"
step: "2.7"
status: done
legacy: "ROADMAP.md 2.7"
tags: [step, phase-2]
---
# 2.7 Audio

Up: [[phase-2-system-daemon]] · Status: **done**

- **Deliverables:** PipeWire: volume, mute, output selection (speakers, HDMI, headset).
- **Outcome:** `internal/audio`: PipeWire through its PulseAudio protocol (`jfreymuth/pulse`, MIT,
  vendored, as planned in the daemon design). Outputs with name and kind (speakers, headphones,
  HDMI, Bluetooth, USB), default output, volume (mixer scale, 0–100) and mute; changing the output
  moves sounds already playing; changes made by any program produce `audio.changed`; reconnects
  when PipeWire restarts. The diagnostics report shows the audio status.
- **Test VM** (`vm/test.sh boot --audio`: built-in + USB virtual sound cards): both outputs listed
  (`usb`, `speakers`); volume 25 and mute applied (checked with `pactl`); output switched while a
  sound played, and the sound moved; volume changed by another program → event; PipeWire restarted
  → reconnected in 26 ms, settings kept. owneetd ~18 MB RSS; PipeWire starts at login (pipewire,
  pipewire-pulse, WirePlumber ~40 MB, needed anyway by the UI's sounds). HDMI and Bluetooth outputs
  are checked on real hardware with the settings UI (step 3.9).
