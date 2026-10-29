---
type: step
description: "Licence notices in the UI ('About → Licences'), review of licences, third-party terms and privacy; the name's search done, no trademark registered."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.5"
status: in-progress
legacy: "ROADMAP.md 7.5"
tags: [step, phase-7]
---
# 7.5 Legal review before the public launch

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress**

- **Deliverables:** licence notices in the UI ("About → Licences"); review of licences,
  third-party terms and privacy by someone experienced in open-source licensing
  ([[legal-compliance]]); the name's trademark search (done, below). **No trademark is
  registered** (the authors, 2026-10-25: too costly for its worth): the step only makes sure
  everything the project does is legal.
- **Trademark search, preliminary (owner and Claude, 2026-10-24):** done by us, not by a
  professional, before buying the domain. Web: nothing named "Owneet" or "OwneetOS" (closest:
  OWNet, a 1-Wire library, not a trademark). TMview (EUIPO, UIBM, WIPO; exact names; classes 9
  and 42):
  - **OWNEETM**: USPTO only, class 21 (household containers), Nanjing Kuaiqueyi, registered
    2025-08-19. Not in conflict.
  - **OWN IT**: three EUIPO marks, all ended or expired (Pacaso 018676312, Argent Labs
    018637285, University of the Arts London 004442927). No rights left.
  - **OwnIT** (EUIPO 019194627, dedicom GmbH, figurative, registered 2025-09-14 until
    2035-05-28): class 9 **hardware only** (computers, peripherals, phones, audio, printers,
    storage), 35, 36 (leasing, financing). Low but real risk: same class 9, "Owneet" sounds like
    "own it"; against it, different goods (no software), the weak common word "own", a
    different look.
  - **ownet**: no result.
- **Outcome of the search:** the name can be used legally and the domain was bought (owneetos.org,
  [[step-7.8h-website-domain]]). Registering the trademark was weighed (a professional's opinion on
  dedicom's OwnIT first, then a filing) and **dropped by the authors on 2026-10-25**.
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
