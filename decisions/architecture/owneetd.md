---
type: decision
description: "owneetd in Go, HTTP + JSON over a Unix socket, user service not root, vendored modules."
area: architecture
status: active
decided: 2026-10-07
updated: 2026-10-07
legacy: "PROJECT_RULES.md §4, §13 (2026-10-07)"
tags: [decision, architecture, owneetd]
---
# owneetd: language, transport, privileges

- **Go** (chosen over Rust, mainly for build simplicity and for the second developer and future
  contributors; the memory difference is ~2–3 % of the C1 target). Single static binary.
- **HTTP + JSON over a Unix socket** (`$XDG_RUNTIME_DIR/owneetd.sock`, mode `0600`) instead of a
  localhost TCP port: web pages in Brave cannot reach a Unix socket (no CSRF). No tokens needed.
- Runs as a **systemd user service of `owneet`, not root**. Root-only tasks (installer, updates,
  disk policy, other graphics cards) go to small separate privileged helpers with narrow
  polkit / D-Bus interfaces.
- **Third-party Go modules are vendored** in `daemon/vendor/`: builds need no network, licences are
  shipped with the package, the source archive is complete.
- No UI text comes from the daemon: errors carry a stable `code` the UI translates.

Full comparison and design: [[owneetd-design]]. Practices: [[go]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-07 | `owneetd`: Go; HTTP + JSON over a Unix socket instead of a localhost TCP port (web pages in Brave cannot reach it); runs as a user service of `owneet`, not root (step 2.1). |
| 2026-10-07 | Third-party Go modules are vendored in `daemon/vendor/` (builds need no network; licences shipped with the package). |
| 2026-10-07 | gamescope runs with `--steam`: owneetd tags each window with an app id and chooses what is on screen (as Steam does on SteamOS); each game or app runs in its own systemd user service, so closing it stops all of its processes. |
