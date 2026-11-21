---
type: technical-analysis
description: "API for the time zone and the time by hand (systemd-timedated) and the Xbox wireless adapter's firmware, used by the first start and Settings."
component: owneetd
tags: [technical-analysis, owneetd, api]
---
# owneetd API: time zone and Xbox adapter firmware — implemented (6.1)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]] · Step:
[[step-6.1-first-boot-flow]]

## Time zone

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/time` | `zone` (e.g. `Europe/Rome`; `UTC` until one is chosen), `synchronized` (the clock was set from the internet), `date` and `time` now in that zone (`2026-10-29`, `14:30`) |
| PUT | `/v1/time/zone` | `{"zone": "Area/City"}`; answers the new status |
| GET | `/v1/time/zones?zone=…` | each zone's distance from UTC now (`offset`, seconds east), at most 100; for the lists of cities |
| PUT | `/v1/time/now` | `{"date": "YYYY-MM-DD", "time": "HH:MM", "zone": "Area/City"}`: the date and time by hand, in `zone` (the first start's city: the console is still on UTC) or, without it, the console's zone; years 2024-2100; answers the new status |

Errors: `time.unavailable` (503, no system bus), `time.unknown_zone` (400, not in the system's
time zone database), `time.bad_time` (400), `time.failed` (502). Event: `time.changed` with the
status.

- Through systemd-timedated (`SetTimezone`, then `SetNTP` on, never interactive). polkit allows
  only three actions to the console user in the active local session
  (`packages/owneetd/50-owneet-time.rules`): set-timezone, set-ntp and set-time.
- The time by hand (added 2026-10-29, for a console without the internet whose PC clock is wrong):
  `SetNTP` off (timedated refuses `SetTime` otherwise), `SetTime`, `SetNTP` on again, so the clock
  sets itself once online.
- The clock comes from the internet through systemd-timesyncd (enabled by `owneet-base`); the
  zone is always the player's choice, never guessed from the place ([[first-boot-setup]]).

## Xbox wireless adapter firmware

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/xone` | `needed` (an adapter is plugged in without its firmware), `state` (`""`, `installing`, `installed`, `failed`), `error` when failed (`offline`, `no_adapter`, `failed`) |
| POST | `/v1/xone/install` | 202: starts the installation; only after the player accepted Microsoft's terms on the console |

Errors: `xone.unavailable` (503), `xone.busy` (409), `xone.failed` (502, the unit could not be
started). Event: `xone.changed` with the status, also when an adapter that needs its firmware is
plugged in or out.

- udev marks a plugged-in adapter without firmware (`/run/owneet/xone-firmware-needed`). The root
  unit `owneet-xone-firmware-install.service` runs `owneet-xone-firmware install
  --accept-microsoft-terms`, which downloads the firmware from Microsoft on this PC (it is never
  shipped, [[legal-compliance]]) and writes its progress to `/run/owneet/xone-firmware.json`.
  polkit allows only that unit, only its start, to the console user
  (`packages/owneet-xone/50-owneet-xone.rules`). See [[xbox-wireless-dongle]].
