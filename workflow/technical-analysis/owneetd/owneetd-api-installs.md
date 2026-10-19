---
type: technical-analysis
description: "API and design of game installs in owneetd (step 4.6): GOG's .sh extracted, Windows installers run silently under Proton, the queue, the marks in a game's folder, stopping and uninstalling."
component: owneetd
tags: [technical-analysis, owneetd, api, games]
---
# owneetd: installing games from their installers (step 4.6)

Up: [[owneetd-design]] · Behaviour: [[games-on-disk]], [[step-4.6-installers]] ·
Frontend side: [[frontend-disk-games]] · Code: `daemon/internal/installs/`

| Method | Path | What |
|---|---|---|
| GET | `/v1/installs` | `{installs: [{dest, title, kind, state, done, total}]}`: the one in progress first (`installing`), then the ones waiting (`queued`); `total` 0 for Windows installers (no percentage) |
| POST | `/v1/installs/inspect` | `{installer, kind}` → `{need, exact, free, licence}`: the space needed on the console's disk (`exact` for GOG's `.sh`, else twice the installer's files), the free space, the licence's text ("" when not found) |
| POST | `/v1/installs` | `{installer, kind, dest, prefix, title}` → 202, queued; 400 `installs.invalid`, 409 `installs.no_space` / `installs.exists` |
| POST | `/v1/installs/stop` | `{dest}` → 204: the install in progress stops (what it wrote is removed), or leaves the queue; 404 `installs.not_found` |
| POST | `/v1/installs/uninstall` | `{dest}` → 204: removes a game the console installed; 404 when its folder has no `.owneet-installed` |

Events: `installs.changed` (the status above; at most twice a second while bytes move),
`install.done` `{dest, title}`, `install.failed` `{dest, title, reason}` with reason `cancelled`,
`source_gone` (the installer's disk was unplugged), `windows` (Windows games not ready),
`no_space`, `failed`.

## Paths

- `dest` must be `$HOME/<games folder>/<name>` (`Games` / `Giochi`, any case, as the frontend's
  `DiskGames::folderNames`; not hidden, one level). The folder may exist only when the installer
  is in it (an installer copied to the console's disk): its entries are kept, also when the game
  is uninstalled.
- `installer`: a regular file under `/run/media/owneet` (USB disks) or in the home folder's games
  folder. `prefix` (Windows installers): under `~/.local/share/owneet/windows/prefixes/`; the
  frontend gives the prefix of `dest` (`DiskGames::windowsPrefix`), so the installed game starts
  in the prefix it was installed in.

## Kinds

- `sh` (GOG's Linux installer, MojoSetup): a shell script followed by a ZIP archive whose offsets
  do not count the script; Go's `archive/zip` finds it. Only `data/noarch/` is written (the game,
  what MojoSetup copies), with the archive's permissions; links only inside the game's folder;
  entries leaving the folder are skipped. No installer code runs (owner, 2026-10-19). The licence:
  a `*eula*` / `*licen[cs]e*` / `*terms*` `.txt` in `data/noarch/docs/`, else in the game, else in
  the archive (UTF-8, else Latin-1).
- `inno`, `nsis`, `msi`: run by `owneet-windows-run PREFIX …` in a transient user unit
  (`systemd-run --user --wait`, unit `owneet-install-<hash>.service`, the console session's
  `DISPLAY`: their hidden windows are never shown, owneetd shows only its apps). Options: Inno
  `/VERYSILENT /SUPPRESSMSGBOXES /NORESTART /SP- /NOICONS /DIR=Z:\…`; NSIS `/S /D=…` (last, never
  quoted); MSI `msiexec /i … /qn TARGETDIR=… INSTALLDIR=…`. NSIS and MSI install through a link
  without spaces (`~/.local/share/owneet/installs/<hash>` → dest), kept for the game's registry
  and removed with it. Exit 3 of `owneet-windows-run` = Windows games not ready. An installer
  that ends well but wrote nothing failed. Stopping stops the unit (every process it started).
  The licence: a licence `.txt` next to the installer or in its `docs` folder.

## Marks and restarts

- `.owneet-installing` (JSON: installer, kept entries) while the install works: the frontend does
  not list that folder (its installer shows the progress instead).
- `.owneet-installed` (JSON: installer, kind, kept entries, link, date) once done: the frontend
  lists the game with `disk.installed` (Uninstall) and hides its installer elsewhere.
- `~/.config/owneet/installs.json` lists the folders being installed; when owneetd starts, those
  still marked `.owneet-installing` (a restart cut them short) are removed.
- Uninstalling never touches the game's prefix (its saves stay).
