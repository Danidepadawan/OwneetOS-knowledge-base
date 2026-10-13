---
type: decision
area: architecture
status: active
decided: 2026-10-07
updated: 2026-10-07
legacy: "PROJECT_RULES.md §13 (2026-10-07)"
tags: [decision, architecture, network]
---
# Wi-Fi networks are saved system-wide

- Saved Wi-Fi networks are **system-wide** (`/etc/NetworkManager/system-connections`, root-only),
  so they work before login and for system services.
- A narrow **polkit rule** (`50-owneet-networkmanager.rules`) allows `settings.modify.system` to
  the user `owneet` **in the active local session only**. `owneet` is **not** an administrator.
- A new password replaces a saved network only if it works; passwords are never logged and never
  returned by the API.

Technical design: [[owneetd-api-network]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-07 | Wi-Fi networks are saved system-wide: a polkit rule allows `settings.modify.system` to `owneet` in the active local session only; `owneet` is not an administrator (step 2.6). |
