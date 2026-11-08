---
type: technical-analysis
description: "API to list every disk and prepare one for games from Settings → Disks (erased, ext4, named by the player), and the installer's request for the other disks (step 6.7)."
component: owneetd
tags: [technical-analysis, owneetd, api, disks]
---
# owneetd API: disks prepared for games — implemented (6.7)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]] · Step:
[[step-6.7-preparing-other-disks]] · Decisions: [[disks]], [[installer-and-firmware]] · Guard: [[user-data]]

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/disks` | every disk of the PC: `path`, `serial`, `size` (bytes), `model`, `usb`, `console` (the console's own disk, or the USB stick it started from), `owneetlog`, `windows`, `bitlocker`, `linux`, `partitions` (`path`, `size`, `fstype`, `label`, `mountpoint`) |
| GET | `/v1/disks/prepare` | the status: `state` (`""`, `preparing`, `erasing`, `formatting`, `done`, `failed`), `disk`, `error` when failed |
| POST | `/v1/disks/prepare` | 202: body `{"disk", "size", "serial", "name", "folder", "erase_windows"}`, the disk as listed; the progress follows as `disks.prepare.changed` |

Refusals: 409 `disks.live` (from the USB stick only the installer prepares disks), `disks.busy`,
`disks.disk_changed` (not the disk that was listed), `disks.name_taken` (another disk's file system
has this name, letters in any case); 403 `disks.not_allowed` (the console's own disk, its stick,
OWNEETLOG); 400 `disks.windows_not_confirmed`, `disks.bad_name` (empty, more than 16 bytes, a "/",
a leading dot, spaces around), `request.invalid`. `folder` is `Games` or `Giochi` (the console's
language). Failures of the work itself, in `error`: `in_use` (a game or a copy uses the disk: nothing
changed), `partition_failed`, `format_failed`, `installed_only`, `name_taken`, `bad_name`.

**How:** the request goes to `/run/owneet-prepare/request` (the console user's folder, read by root key
by key, never run) and polkit lets the console user start `owneet-prepare-disk.service`
(`50-owneet-install.rules`), which checks everything again: the whole disk becomes one GPT partition
with ext4 (no space kept for root), labelled with the name, the console user owning it, with the Games
folder; meanwhile `owneet-mount` leaves it alone (`/run/owneet-mount/preparing`), then mounts it.

**The installer** (`POST /v1/installer/start`) takes `games: [{"disk", "size", "serial", "name",
"erase_windows"}]` (up to 8 other internal disks, any size) and `folder`; refusals
`installer.bad_name`, `installer.name_taken`. They are checked with the system's disk before anything
is touched and prepared last, by the same script (`owneet-install` state `games`, error `games_failed`).
