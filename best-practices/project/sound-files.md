---
type: best-practice
description: "Format, loudness, licence and naming rules for interface sound files; one sound per press."
scope: project
tags: [best-practice, sounds]
---
# Interface sound files

Comes from: [[interface-sounds]]. Full list: [[interface-sounds-spec]].

- **Format:** WAV, PCM 16-bit, 48 kHz (PipeWire's native rate), **mono** (stereo only if the
  sound really uses it). The package converts delivered files when it is built (the delivered
  files stay as made).
- **No silence at the start**; a short fade-out, no long tail or reverb.
- **Same loudness for the whole set:** peaks around −6 dBFS, frequent sounds softer.
- **One family** of sounds; frequent sounds must not tire after hours of use.
- **Licence:** own work, or CC0 / CC BY / CC BY-SA (never NC or ND); author, source and licence
  recorded for `CREDITS.md` and `frontend/sounds/SOURCES.md`.
- **One sound per button press**, the most specific one; never while a game is on screen.
- Demos play the same files from `design/demos/sounds.js` (`tools/sounds/make-demo-sounds`).
