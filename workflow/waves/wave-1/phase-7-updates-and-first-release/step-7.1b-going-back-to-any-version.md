---
type: step
description: "Going back to any published version of OwneetOS from Settings: the list of versions, the download in reverse, the warning; split from 7.1."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.1b"
status: done
tags: [step, phase-7]
---
# 7.1b Going back to any version *(split from 7.1 on 2026-10-25)*

Up: [[phase-7-updates-and-first-release]] · Status: **done** · Follows [[step-7.1-updates]]

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
- **Built (2026-11-01, `feature/phase7`):**
  - `owneet-updates` 0.0.1-2: `size VERSION` (the download size of going back, in a database
    folder of its own, to `/run/owneet/system-goto.json`) and `goto VERSION` (only an older version
    of the verified list: the same spare copy and 3 tries as an update; downloads with `-Syyuuw`, then
    removes the packages none of the older release's repositories has, then `-Suu`); template units
    `owneet-updates-size@` and `owneet-updates-goto@`, allowed by the polkit rule. A check no longer
    replaces "ready" (an installed update waiting for the restart), and no longer ends as a failed
    unit when it worked (a slip of 7.1).
  - owneetd 0.24.0: `listed`, `releases` and `goto` in `/v1/system-update`,
    `POST /v1/system-update/size` and `/go-to` ([[owneetd-api-system-update]]).
  - owneet-frontend 0.33.0: the row "Other versions", `VersionsSheet.qml` (the list and the
    warning of the approved demo), the "Checking…" window first when the list is not there, the
    update's own windows for the download, the installation and "ready"; the texts in the five
    languages (German, French and Spanish drafted, to be checked with
    [[step-7.9-console-more-languages]]; the French update texts say "tu" while most of the file
    says "vous").
  - `tools/make-test-release`: keeps every test release in the list, publishes every package of
    `out/repo` as a real release does, and `--extra NAME` adds a package only that release has.
- **Tested (2026-11-01):** Go tests and `tools/lint` (all checks passed); the screens in
  `tools/frontend-preview` (`system-update-versions*.txt`), compared with the demo (the offline
  notice is too short for the screenshots: seen in the log). In the test VM, on the system
  installed with `owneet-install`, three signed test releases (0.0.1, 0.0.2, 0.0.3 with the
  package `owneet-test-extra`): updated to 0.0.3 (spare copy 0.0.1); the list showed 0.0.3, 0.0.2,
  0.0.1; going to 0.0.3 refused (`not_listed`); the size of going back to 0.0.2 worked out; going
  back to 0.0.2 downgraded `owneet-updates`, removed `owneet-test-extra`, made 0.0.3 the spare copy
  and gave 0.0.2 its 3 tries. With 0.0.2 broken on purpose (the interface not executable), 3 starts
  failed and the 4th ran 0.0.3, which became the system again, with "The update did not work" on the
  console. Going back to 0.0.2 again, not broken: it started and counted as working, and 0.0.3 was
  offered as an update. The first try had failed: [[going-back-keeps-the-newer-package-database]].
  **Not checked here:** the screens on the console in the VM (the first start waits for a
  controller; seen in the preview instead), real hardware (with the next hardware test), a real
  release going back over a different Arch Linux Archive date (the test releases share one date).
  Code commit 369f926.
- **Approved by the owner (2026-11-01): done.**
