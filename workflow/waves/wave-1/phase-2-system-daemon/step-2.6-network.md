---
type: step
phase: "[[phase-2-system-daemon]]"
step: "2.6"
status: done
legacy: "ROADMAP.md 2.6"
tags: [step, phase-2]
---
# 2.6 Network

Up: [[phase-2-system-daemon]] · Status: **done**

- **Deliverables:** NetworkManager over D-Bus: scan, connect (with password from the OSK), forget, status.
- **Outcome:** `internal/network`: status (state, connectivity, Wi-Fi, Ethernet), visible networks
  grouped by name with security (open, WPA, WPA3; WEP and enterprise reported as unsupported),
  scan, connect with password check before NetworkManager and a precise "wrong password" error,
  disconnect, forget, Wi-Fi on/off; events `network.*`, `wifi.scan_done`. A new password replaces a
  saved network only if it works. Networks are saved system-wide thanks to a narrow polkit rule
  (`settings.modify.system` for `owneet` in the active local session only; `owneet` is not an
  administrator). The diagnostics report shows the network status.
- **Test VM with simulated Wi-Fi** (`mac80211_hwsim` + NetworkManager hotspot, `vm/README.md`):
  scan finds the network; short password → `invalid_password`; wrong password → `wrong_password`
  in 1 s, nothing left saved; right password → connected in 3 s, saved in a root-only file;
  disconnect and reconnect without password; forget; Wi-Fi off → `wifi_disabled`; WPA3-only
  network: wrong and right password both handled. Passwords never appear in the journal. owneetd
  ~17.7 MB RSS (unchanged). Unit tests: security classification, password rules, network list.
  Real-hardware Wi-Fi is tested with the settings UI (step 3.9), or earlier on request. Approved
  by the owner (system-wide saved networks with the polkit rule).
