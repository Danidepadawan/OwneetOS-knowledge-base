---
type: technical-analysis
component: owneetd
legacy: "docs/daemon-design.md §4 Controllers"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Controllers

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/controllers` | **Implemented (2.3).** Connected controllers: id, name, brand, connection (usb/bluetooth/dongle), Guide available, battery |

The **Guide button** is `BTN_MODE` when the kernel driver reports it (Xbox, PlayStation, Nintendo
and most others); otherwise the `guide` entry of SDL_GameControllerDB tells which button it is.
Some Bluetooth controllers send it as `KEY_HOMEPAGE` on a second input device with the same
unique id: that device is followed too. Devices are never grabbed.
