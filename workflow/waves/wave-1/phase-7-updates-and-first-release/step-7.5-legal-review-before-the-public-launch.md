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
  agent alters neither the app nor its content. The string, approved by the owner on 2026-10-18 (YouTube's line
  of `packages/owneet-base/apps.json`, brand-neutral, [[step-5.3-youtube]]): `Mozilla/5.0 (Linux; SMART-TV) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36`.
- ~~**To include (2026-10-26):** the same question for **Spotify**, opened with a TV user agent too~~
  **Dropped (2026-10-28):** Spotify went back to its desktop web player without a user agent of
  its own ([[step-5.5-spotify]]); nothing to review for Spotify's agent.
- **To include (2026-10-18):** Brave's Shields block ads by default, and the managed policies
  (`packages/owneet-base/brave-policies.json`) do not turn them off, so YouTube's and Spotify's ads
  are blocked in the web apps. Kept as it is (owner, 2026-10-18); the review decides whether the
  policies must turn ad blocking off for the web apps ([[legal-compliance]]). Seen on 2026-10-19:
  an ad played on YouTube's TV interface with Shields on.
- **To include (2026-10-19):** the console asks for consent to Google's Widevine terms once and at
  every new Widevine version ([[step-5.4-netflix]]); whether that is enough, since a change of
  Google's terms without a new Widevine version cannot be seen by the console without asking a
  server ([[legal-compliance]]). Also: the wording of the console's consent ([[step-5.4-netflix]]);
  Widevine's own `LICENSE` ("You may not use … the Software without a separate license agreement
  with Google"): whether Brave's agreement with Google covers its users on OwneetOS; Brave's help
  page says that turning Widevine on means agreeing to Google's Terms of Use and that Brave is not
  liable for it.
