---
type: step
description: "Trademark search for 'OwneetOS' (EUIPO, Italian register); licence notices in the UI ('About → Licences'); review of licences,…"
phase: "[[phase-7-updates-and-first-release]]"
step: "7.5"
status: todo
legacy: "ROADMAP.md 7.5"
tags: [step, phase-7]
---
# 7.5 Legal review before the public launch

Up: [[phase-7-updates-and-first-release]] · Status: **todo**

- **Deliverables:** trademark search for "OwneetOS" (EUIPO, Italian register); licence notices in
  the UI ("About → Licences"); review of licences, third-party terms and privacy by someone
  experienced in open-source licensing ([[legal-compliance]]).
- **To include (2026-10-18):** whether the console's Brave extension fits Netflix's Terms of Use
  §1.8(vi), "insert any code or product or manipulate the content of the Netflix service in any
  way": it adds one ring element (closed shadow root) to the page and clicks, scrolls and types
  only on the user's input ([[legal-compliance]], [[extension-design]]). If it does not, the ring
  can be drawn by the console in its gamescope overlay instead of in the page.
- **To include (2026-10-18):** whether opening YouTube's TV interface (`youtube.com/tv`) with a TV
  user agent fits YouTube's Terms of Service (no altering or modifying the Service, no
  circumventing; access "to the extent made available to you"). The owner's view: it does: the
  terms allow the modes the service makes available, the TV interface is one of them, and a user
  agent alters neither the app nor its content. The exact string is the one in YouTube's line of
  `packages/owneet-base/apps.json` (brand-neutral, [[step-5.3-youtube]]).
- **To include (2026-10-18):** Brave's Shields block ads by default, and the managed policies
  (`packages/owneet-base/brave-policies.json`) do not turn them off, so YouTube's and Spotify's ads
  are blocked in the web apps. Kept as it is (owner, 2026-10-18); the review decides whether the
  policies must turn ad blocking off for the web apps ([[legal-compliance]]).
