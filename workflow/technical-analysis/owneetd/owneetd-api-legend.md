---
type: technical-analysis
description: "API and design of the command legend in owneetd (step 5.6a): View in a web app or the player, the legend's state, over the app in gamescope, a page in cage, its one data file."
component: owneetd
tags: [technical-analysis, owneetd, api, input]
---
# owneetd: the command legend (step 5.6a)

Up: [[owneetd-design]] · Behaviour: [[controller-input-map]] ("The command legend"),
[[step-5.6a-command-legend]] · Code: `daemon/internal/legend/`, `daemon/internal/api/legend.go`,
`daemon/cmd/owneet-bridge`, `daemon/internal/player/player.go`, `extension/content/input.js`,
`frontend/owneet-frontend/src/themes/owneet/Legend.qml`, `…/foundation/legends.js`

| Method | Path | What |
|---|---|---|
| GET | `/v1/legend` | `{open, app, context, page}`: `app` the running app's id (`web:netflix`, `player`), `context` the legend to show (`web`, `youtube`, `netflix.browse`, `netflix.title`, `netflix.player`, `spotify`, `player.video`, `player.song`), `page` true when the interface shows it as a page in front (cage) |
| POST | `/v1/legend` | `{"action": "toggle", "context": "…"}` (View in the open web app: opens it, or closes that app's legend), `{"action": "screen", "context": "…"}` (the web app's screen changed: its open legend follows), `{"action": "close"}` (the interface: B or View on the page) → 204. Errors `legend.invalid` (400), `legend.no_app` (409: no web app open), `legend.unavailable` (503) |

Event: `legend.changed` (the state above; closed: `open` false with the app).

## How it works

- **View is caught by the app's own integration**, never by the console (which still intercepts
  only Guide):
  - **a web app:** the console's extension reads View (button 8, unused by every site). It sends
    `{"type": "legend", "action": "toggle", "context": …}` through the background worker and
    owneet-bridge (→ `POST /v1/legend`). Each site's navigation names its legend (`legend()`:
    Netflix by its player, title window or browsing rows; Spotify on its player pages; YouTube;
    otherwise `web`). While the legend is open over the page, the extension checks the screen every
    250 ms and sends `screen` when it changes. The bridge passes a web app's `legend.changed` back
    as `{"type": "legend", "open", "page"}`; under a page (cage) the extension stops reading the
    controller, and on its return ignores the buttons still held (as after the console's keyboard,
    View included).
  - **the player:** `GAMEPAD_BACK` → `script-binding owneet/legend` → `script-message owneet-legend
    player.video|player.song` on mpv's control socket → owneetd's player manager calls `Toggle`.
- **gamescope** (`Layered`): the interface draws the legend in a window of its own made a gamescope
  external overlay (as the web keyboard, `overlay.makeOverlay` / `showOverlay` / `hideOverlay`),
  never focused and never given the controller: the app keeps working under it. owneetd closes it
  when `focus.changed` names something else (Guide: an overlay would float over the console too)
  and when its app exits.
- **cage:** opening shows the console (`ShowHome`); the interface shows the page, where B or View
  (`Nav.isView`, the controller's SELECT key) sends `close`; owneetd brings the app back
  (`FocusApp`). The player is told to ignore its buttons meanwhile (owneetd's `focus.changed` →
  `owneet-focus no`, [[owneetd-api-player]]).
- **One data file:** `foundation/legends.js` in the theme holds every legend as rows of [buttons,
  message key] (strict JSON inside, `module.exports` for Node). The interface draws from it; the
  extension's `test/legend.test.js` checks it against the sites' navigations (the legends they
  name exist; each app's legends name the buttons its navigation takes, and only those), and
  `daemon/internal/player/bindings_test.go` against the player's `input.conf` (skipped in the
  owneetd package build, which has only `daemon/`).
