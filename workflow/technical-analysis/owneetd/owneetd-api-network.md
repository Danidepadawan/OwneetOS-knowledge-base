---
type: technical-analysis
component: owneetd
legacy: "docs/daemon-design.md §4 Network"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Network — implemented (2.6)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/network` | `available` (NetworkManager running), `state`, `connectivity` (full/limited/portal/none/unknown), `wifi` (present, enabled, hardware_enabled, state, ssid, strength), `ethernet` (present, connected) |
| GET | `/v1/network/wifi` | Visible networks: `ssid`, `strength`, `security` (open/wpa/wpa3/wep/enterprise), `known` (saved), `connected`; connected first, then saved, then by signal |
| POST | `/v1/network/wifi/scan` | Start a scan (202); `wifi.scan_done` follows |
| POST | `/v1/network/wifi/connect` | `{"ssid": "…", "password": "…"}`; waits for the result (up to 60 s) |
| POST | `/v1/network/wifi/disconnect` | Disconnect Wi-Fi |
| DELETE | `/v1/network/wifi/{ssid}` | Forget a saved network (SSID URL-encoded) |
| PUT | `/v1/network/wifi/enabled` | `{"enabled": false}` — Wi-Fi radio off/on |

Errors: `network.unavailable` (503), `network.no_wifi` / `network.wifi_disabled` (409),
`network.not_found` (404, not visible), `network.unknown_network` (404, not saved),
`network.unsupported_security` (422, WEP or enterprise), `network.password_required` (422),
`network.invalid_password` (400, WPA: 8–63 characters or 64 hex digits),
`network.wrong_password` (422), `network.timeout` (504), `network.connect_failed` (502).

- **Connecting:** without a password, a saved network is reused; with one, a new saved network is
  created and replaces the old one **only if it works** (a wrong password never leaves a broken
  saved network behind). WPA/WPA2 (and WPA2/WPA3 transition) networks use `wpa-psk`, WPA3-only
  networks `sae`. Hidden networks are not listed (later, if needed).
- **Wrong password:** NetworkManager has no secret agent to ask, so a refused password ends the
  attempt at once with reason `no-secrets`, read from the device's `StateChanged` signal.
- **Saved networks** are system-wide (`/etc/NetworkManager/system-connections`, readable by root
  only), so they also work before login and for system services. NetworkManager allows this only
  to administrators, so the package `owneetd` ships one polkit rule,
  `50-owneet-networkmanager.rules`: the action `settings.modify.system` is allowed to the user
  `owneet` only, from the active local session only. `owneet` is **not** an administrator.
- Passwords are never logged and never returned by the API.
- Tested in the test VM with simulated Wi-Fi (`mac80211_hwsim`, see `vm/README.md`).
