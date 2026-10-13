---
type: technical-analysis
description: "API for PipeWire volume, mute and output selection."
component: owneetd
legacy: "docs/daemon-design.md §4 Audio"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Audio — implemented (2.7)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/audio` | `available`, default `output` (id), its `volume` (0–100) and `muted`; `outputs`: id, name, kind (speakers, headphones, hdmi, bluetooth, usb, other), default, volume, muted |
| PUT | `/v1/audio/volume` | `{"volume": 0–100}` — default output, all channels alike |
| PUT | `/v1/audio/mute` | `{"muted": true}` |
| PUT | `/v1/audio/output` | `{"id": "…"}` — default output; sounds already playing move to it |

Errors: `audio.unavailable` (503, no audio server), `audio.no_output` (409),
`audio.unknown_output` (404), `audio.failed` (502).

- **How:** PipeWire's PulseAudio protocol (`pipewire-pulse`, socket `$XDG_RUNTIME_DIR/pulse/native`)
  through `github.com/jfreymuth/pulse/proto` (MIT, pure Go, vendored). owneetd subscribes to
  output, server and card changes, so changes made by any program produce `audio.changed`; it
  reconnects when PipeWire restarts. Connecting starts PipeWire (socket activation) at login.
- **Volume** uses the same scale as desktop mixers (PulseAudio's, perceived loudness), so 50 here
  is 50 in any other tool. Above 100 is not offered.
- **Outputs** are the ones PipeWire/WirePlumber expose for the active card profiles; headphones
  plugged into a jack switch automatically (WirePlumber). Choosing among card profiles (for cards
  where HDMI and analog outputs exclude each other) is left for later, if real hardware needs it.
- WirePlumber remembers volume and default output across restarts.
- Tested in the test VM with two virtual sound cards (`vm/test.sh boot --audio`).
