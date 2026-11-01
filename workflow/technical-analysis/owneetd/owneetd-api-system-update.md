---
type: technical-analysis
description: "API for the updates of an installed OwneetOS (check, install, go back to the previous version or to any older one, the notice after going back by itself), used by Settings → System."
component: owneetd
tags: [technical-analysis, owneetd, api]
---
# owneetd API: updates of an installed OwneetOS — implemented (7.1, 7.1b)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]] · Steps:
[[step-7.1-updates]], [[step-7.1b-going-back-to-any-version]] · Decision: [[distribution-and-updates]]

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/system-update` | the status below |
| POST | `/v1/system-update/check` | 202: looks for a newer release now (the console also checks by itself, 3 minutes after start-up and then daily) |
| POST | `/v1/system-update/install` | 202: downloads and installs the release found; the progress follows as events |
| POST | `/v1/system-update/go-back` | 202: the previous version becomes the system at the next start-up; `back` turns `done` (the interface restarts the console) or `failed` |
| POST | `/v1/system-update/size` | 202: body `{"version"}`, an older version of the list: works out the download size of going back to it (`goto` follows) |
| POST | `/v1/system-update/go-to` | 202: body `{"version"}`: goes back to that older version, an update in reverse followed like `install` (`state`, `version` = the older one) |
| POST | `/v1/system-update/notice-seen` | 204: the player has read that the console went back by itself (also clears a failed `back`) |

Status: `installed` (installed by the OwneetOS installer: only these systems have the rollback the
updates rely on; testers' PCs use `/v1/update`, the USB stick), `state` (`""` not checked since
the start, `none`, `available`, `downloading`, `installing`, `ready`, `failed`), `error` when
failed (`offline`, `not_signed`, `not_installed`, `on_previous`, `download_failed`,
`install_failed`), `current`, the newer `version` with its `size` (bytes), `notes` (per language)
and `packages` (`name`, `from`, `to`: the optional "Details"), `percent`, `checked` (the last check,
kept across start-ups), `checking`, `previous` (`version`, `since`; `null` without a spare copy),
`on_previous` (started from the spare copy), `rolled_back` (when the console went back by itself,
until the notice is seen), `back` (`working`, `done`, `failed`), `listed` (the signed list of
releases was downloaded since the start-up), `releases` (the current version and the older ones in
it, newest first: `version`, `date`), `goto` (`version`, `size`, `sizing`, `error`: `offline` or
`not_listed`; `null` until a size was asked).

Errors: `system_update.unavailable` (503, no system bus), `system_update.not_installed`,
`system_update.busy`, `system_update.nothing`, `system_update.on_previous`,
`system_update.no_previous`, `system_update.not_listed` (409: not an older version of the list),
`system_update.failed` (502, the unit could not be started).
Event: `system-update.changed` with the status, whenever it changes.

- The work is done as root by the units of `owneet-updates` (`owneet-updates-check.service`,
  `owneet-updates-apply.service`, `owneet-rollback-now.service`, and with the older version as
  instance `owneet-updates-size@VERSION.service`, `owneet-updates-goto@VERSION.service`); polkit
  allows only their start, only to the console user in the active local session
  (`50-owneet-updates.rules`, the instance only made of numbers and dots).
- owneetd follows four files every 2 seconds: `/run/owneet/system-update.json` (written by
  `owneet-updates`), `/run/owneet/releases.json` (the verified list, for the notes and the
  versions), `/run/owneet/system-goto.json` (the size of going back) and
  `/run/owneet/rollback.json`. The boot partition is root's only (`umask=0077`), so
  `owneet-rollback` publishes its state there after every change and at every start-up, with the
  spare copy's version (kept next to its kernel, `/previous/version`).
- Its own state, `~/.local/state/owneetd/system-update.json`: the time of the last check (`/run`
  is emptied at every start-up) and the going back by itself already shown.
- Package `daemon/internal/sysupdate`.
