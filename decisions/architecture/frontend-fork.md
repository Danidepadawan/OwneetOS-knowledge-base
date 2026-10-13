---
type: decision
description: "owneet-frontend is a Pegasus fork inside the repository; trademark terms, what is not used, Qt 5 now."
area: architecture
status: active
decided: 2026-10-08
updated: 2026-10-08
legacy: "PROJECT_RULES.md §12 (Pegasus), §13 (2026-10-08); ROADMAP 3.1"
tags: [decision, architecture, frontend, legal]
---
# Frontend: the Pegasus fork `owneet-frontend`

- The console interface is a **fork of Pegasus Frontend**, named **`owneet-frontend`**, living
  **inside the OwneetOS repository** (`frontend/owneet-frontend`, no separate GitHub repository;
  owner's choice in step 3.1). Pegasus `5d58223` was imported unmodified; every OwneetOS change is
  a separate, later commit.
- Pegasus's licence adds trademark terms (GPL section 7): the modified frontend never uses
  "Pegasus" or Pegasus's logos as its title or logo, keeps Pegasus's copyright notices and credits
  it.
- **Not used:** Pegasus's CC BY-NC-SA default theme, logo, Roboto fonts and button images.
  **Disabled:** its online metadata downloads (Steam store, GOG API, Play Store): local data only.
- The interface stays loaded while a game runs (Pegasus unloaded it), and games start through
  owneetd.
- Qt 5.15 now; the Qt 6 port is a later step (Qt 6 is not possible yet).

Architecture: [[frontend-architecture]]. Guard: [[legal]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-08 | Legal check before phase 3: the frontend fork is named `owneet-frontend` (Pegasus's trademark terms); Pegasus's CC BY-NC-SA theme, logo, Roboto fonts and button images are not used; its online metadata downloads are disabled. `CREDITS.md` credits every project OwneetOS builds on and ships in the image ([[legal-compliance]]). Step 2.9 approved. |
