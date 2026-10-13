---
type: decision
area: product
status: active
decided: 2026-10-03
updated: 2026-10-03
legacy: "PROJECT_RULES.md §8 (online features, chat, logos)"
tags: [decision, product]
---
# Online features and chat

- **Online features** rely on existing services (Steam friends/achievements inside Steam,
  Discord, etc.). **No own server** ("Option A").
- **Chat**: pluggable modules, user picks the service. **Discord web first**, controllable by
  gamepad, optionally running **in the background** (voice keeps working during games;
  notifications and mute/push-to-talk via the overlay). Planned for [[wave-2]].
  - Use only official web clients. **No modded clients or self-bots** (ToS violations).
- No bundled third-party logos (Netflix, Spotify…): fetch icons at runtime or use generic ones.

## Creates

- Guards: [[product-invariants]] (no own server), [[legal]] (official clients only, no logos).

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-03 | Online features: Option A (no own server). |
