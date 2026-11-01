---
type: step
description: "Going back to any published version of OwneetOS from Settings: the list of versions, the download in reverse, the warning; split from 7.1."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.1b"
status: in-progress
tags: [step, phase-7]
---
# 7.1b Going back to any version *(split from 7.1 on 2026-10-25)*

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress** · Follows [[step-7.1-updates]]

- **Deliverables:** in Settings → System, the published versions of OwneetOS with their dates; the
  user picks one, reads the warning (personal data do not go back; an old version has old
  security problems and may not know newer hardware) and confirms; the console downloads that
  version's OwneetOS packages (kept published for every release) and Arch's packages of its
  Arch Linux Archive date, installs them as an update in reverse (spare copy, 3 tries, the same
  rollback of [[step-6.3-installer-backend]]) and restarts ([[distribution-and-updates]]).
- **Done when:** in the test VM, going from a newer version to an older one works, and a broken
  older version goes back by itself to the one the user came from.
- **Started (owner, 2026-11-01)** on `feature/phase7`, after [[step-7.1-updates]] was approved. The
  screens are those of the approved demo `design/demos/7.1-updates.html` ("Other versions", "Choose
  a version", the warning). Owner's choices for what the demo does not show:
  - the list of versions comes from the signed list of releases; offline, the same notice as the
    update row ("No internet: the console checks again when it is online"); online but not checked
    since the start-up, the "Checking…" window of 7.1 first, then the list;
  - the warning opens at once, as in the demo; its line "{size} to download" stays empty until
    the size is known (it needs the chosen version's package lists from the internet);
  - packages the newer version added and the older one does not know are removed: the system
    becomes exactly the chosen version.
