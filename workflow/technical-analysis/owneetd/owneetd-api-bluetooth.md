---
type: technical-analysis
description: "API for BlueZ devices and automatic gamepad pairing, the pairing agent."
component: owneetd
legacy: "docs/daemon-design.md §4 Bluetooth"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Bluetooth — implemented (2.5)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/bluetooth` | `adapter`, `powered`, `discovering`, `auto_pair`, `devices` (address, name, paired, trusted, connected, gamepad, battery) |
| POST | `/v1/bluetooth/auto-pair` | `{"enabled": true, "seconds": 120}` (default 120, max 600) — scan, pair, trust and connect any gamepad, no input |
| POST | `/v1/bluetooth/devices/{address}/connect` · `/disconnect` | Connect or disconnect a known device |
| DELETE | `/v1/bluetooth/devices/{address}` | Forget (unpair) a device |

Errors: `bluetooth.unavailable` (503, no system bus), `bluetooth.no_adapter` (409),
`bluetooth.unknown_device` (404), `bluetooth.invalid_address` (400), `bluetooth.failed` (502, BlueZ
refused; the message says why).

**First pairing with zero input** ([[controllers-and-pairing]]): whenever **no controller is
connected** (USB, dongle or Bluetooth), auto-pair turns on by itself — the adapter is powered, a scan
runs, and every device that **identifies as a gamepad** is paired, trusted and connected. It turns
off as soon as a controller is connected. The UI can also turn it on for a while (pairing a second
controller). Configuration: `bluetooth_autopair_without_controller` (default `true`).

A device is a gamepad when its Bluetooth Classic class of device is "peripheral / joystick or
gamepad", its Bluetooth LE appearance is joystick or gamepad, or BlueZ's icon is `input-gaming`.

owneetd registers a BlueZ **pairing agent** with the `NoInputNoOutput` capability (nobody can type
or compare a code). It accepts a pairing request **only from a gamepad while auto-pair is on** and
rejects everything else, so keyboards, phones or headsets are never paired without the user. The
agent is registered again when bluetoothd starts or restarts. Trusted devices reconnect by themselves.
Bluetooth controllers are listed in `/v1/controllers` with BlueZ's device name (Bluetooth LE
controllers otherwise appear as `bluez-hog-device`).

D-Bus library: `github.com/godbus/dbus/v5` (BSD-2-Clause), **vendored** in `daemon/vendor/` with
its dependency `golang.org/x/sys` (BSD-3-Clause): the package build needs no network and the source
archive is complete.
