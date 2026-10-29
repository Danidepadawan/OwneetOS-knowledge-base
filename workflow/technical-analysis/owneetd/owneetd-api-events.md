---
type: technical-analysis
description: "The event stream (/v1/events) and every event type."
component: owneetd
legacy: "docs/daemon-design.md §4 Event stream"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Event stream

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

`GET /v1/events` keeps the connection open and sends one JSON object per event (Server-Sent
Events format). Event types (initial list):

`guide.pressed`, `controller.added`, `controller.removed`, `controller.battery` (implemented, 2.3),
`bluetooth.auto_pair`, `bluetooth.pairing`, `bluetooth.paired`, `bluetooth.pair_failed`,
`bluetooth.forgotten` (implemented, 2.5), `network.changed`, `network.connecting`,
`network.connect_failed`, `network.forgotten`, `wifi.scan_done` (implemented, 2.6), `audio.changed`
(implemented, 2.7), `power.suspending`, `power.resumed`, `power.shutting_down` (implemented, 2.8), `app.started`,
`app.exited`, `focus.changed`, `guide.released` (implemented, 2.9), `input.layout_changed`
(implemented, 2.4), `display.changed`, `display.pending`, `display.confirmed`, `display.reverted`
(implemented, 3.9), `update.changed` (implemented, 4.2b), `apps.catalog.changed` (implemented, 5.0.0),
`apps.open_failed` (`id`, `code`: `apps.widevine_failed` or `apps.failed`, `error`: a web app's first opening failed, 5.4),
`xone.firmware_needed` (later).
