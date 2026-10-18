---
type: step
description: "TV interface, playback controls on the gamepad."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.3"
status: in-progress
legacy: "ROADMAP.md 5.3"
tags: [step, phase-5]
---
# 5.3 YouTube

Up: [[phase-5-streaming-apps-and-media]] · Status: **in progress**

- **Deliverables:** TV interface, playback controls on the gamepad.
- **Before shipping (2026-10-18):** check the TV interface (`youtube.com/tv`) and any TV user agent
  it needs against YouTube's Terms of Service ("access … to the extent made available to you"; no
  circumventing; [[legal-compliance]]). **Owner's view (2026-10-18):** a TV user agent is not a
  problem: the terms forbid altering the service except in the modes it makes available, and the
  TV interface is one of them; a user agent does not alter the app or its content. The question
  still goes to the legal review of [[step-7.5-legal-review-before-the-public-launch]], with the
  exact string chosen.
- **Agreed (owner, 2026-10-18):**
  - YouTube opens its **TV interface** (`https://www.youtube.com/tv`, already the catalogue's
    address) with a **TV user agent**, set by owneetd from the catalogue: a field `userAgent` of
    the web app's entry in `/usr/share/owneet/apps.json`, passed to Brave as `--user-agent=…`
    ([[owneetd-api-apps]]). The interface still sends no flags.
  - **The string is brand-neutral first:** a generic TV string without a manufacturer's name; a
    device's string (e.g. Samsung Tizen, PS4) only if no generic one works.
  - **No demo:** on the TV interface YouTube draws its own selection and keyboard and the console
    draws nothing new; the "Inside YouTube" bindings are agreed in [[controller-input-map]] before
    any code. A demo comes only if the console must draw something (a ring, a hint)
    ([[demo-before-code]]).
  - **Brave's ad blocking stays as it is** (Shields are on by default; the managed policies do not
    turn them off) and goes to the legal review of 7.5 ([[legal-compliance]]).
  - **Plan change:** the desktop site's cards with several buttons, left to 5.3 by
    [[step-5.2-extension-core]], are dropped: the TV interface replaces the desktop site. The
    extension's general navigation stays for every other page (e.g. Google's sign-in pages).
- **Sub-steps** (one per prompt, each tested by the owner):
  1. **The TV user agent:** the catalogue field and owneetd's launch (owneetd 0.12.5, owneet-base
     0.0.44); the string chosen in the test VM (cage, visible) by changing YouTube's line of the
     VM's catalogue and opening YouTube again (owneetd reads the catalogue at every opening);
     approved by the owner.
  2. **The controller on the TV interface, checked in the test VM; then the bindings** (vault
     only): whether the TV interface reads the controller itself, which keys it takes (arrows,
     Enter, Escape or Backspace, media keys) and whether keys sent by a script work (else real keys
     through owneetd's virtual keyboard, [[owneetd-api-input]]); what B does at its home screen;
     signing in without a keyboard; what the ads do with Shields on (noted for 7.5). Then the
     "Inside YouTube" section of [[controller-input-map]] and [[extension-design]], with the owner.
  3. **The extension's mode for the TV interface:** on `www.youtube.com/tv` the gamepad loop sends
     the TV interface's keys instead of moving the ring (same repeat timing, held buttons counted
     again, no ring, Guide never read); other addresses keep 5.2's behaviour.
  4. **Playback and text:** the player's bindings agreed in 2; search and signing in.
  5. **Close:** terms of service, known limits, the hardware check batched with the next one
     (with 5.2's follow-ups: the ring during typing, the keyboard's sounds), outcome.
- **Server side (2026-10-18, checked from the developer's PC with `curl`):** `youtube.com/tv`
  serves the TV client (`"clientName":"TVHTML5"`) to user agents with `(Linux; SMART-TV)` or
  `(Linux; TV)`, also without a Chrome version, and to Tizen, PS4 and Cobalt strings; a desktop
  string (also `(X11; Linux x86_64; TV)`) gets a short page that sends the browser to the desktop
  site (`location.assign('https://www.youtube.com/?app=desktop…')`). What the TV client does in
  Brave is checked in the VM (sub-step 1).
- **Sub-step 1 checked** (owner, 2026-10-18, test VM, cage; owneetd 0.12.5, owneet-base 0.0.44):
  with `Mozilla/5.0 (Linux; SMART-TV) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36` YouTube
  opens its TV interface, and its own on-screen keyboard works. **The navigation is broken there:**
  the extension's navigation of 5.2 still runs on the TV interface, against the TV interface's own
  selection (expected; sub-steps 2 and 3). **The string is approved by the owner (2026-10-18):
  sub-step 1 is done.** Typing with YouTube's own keyboard worked although the navigation was
  broken: a hint that the TV interface reads the controller itself, checked first in sub-step 2.
- **Sub-step 2, the check** (owner, 2026-10-18, test VM, cage; the extension moved aside, then a
  probe extension of the VM only, `vm/run/probe-5.3/`, never shipped):
  - **The TV interface does not read the controller:** without the extension no button did
    anything (only the mouse worked). The typing seen in sub-step 1 most likely came from the
    extension's own focus moves and clicks on the keys of YouTube's keyboard.
  - **It takes keyboard keys:** real keys (sent with `vm/test.sh keys`) work: arrows, Enter,
    Escape, Backspace and the play/pause media key. **Keys sent by a script work too**:
    `KeyboardEvent`s with `key`, `code` and `keyCode` (Brave keeps the `keyCode`) moved YouTube's
    own selection, Enter opened the tile, Escape went back from it, Backspace on a tile moved to
    YouTube's left menu. So the extension can drive the TV interface by sending keys itself;
    owneetd's virtual keyboard is not needed.
  - **Signing in:** only "Sign in with your phone": a QR code, or `yt.be/activate` and a code
    typed on a phone or a computer. Nothing is typed on the console.
  - Seen in the screenshots: **Brave's sidebar** (bookmarks, reading list, add, settings) at the
    right edge, mouse-only; and a black band under the page (the VM's screen is 640 × 480: only the
    resolution, owner).
  - **Escape goes back up to YouTube's "Welcome back" account page** ("Sign in with your phone",
    "Add a kid account", "Watch as guest") and then does nothing: YouTube shows no exit prompt of
    its own.
- **Bindings agreed (owner, 2026-10-18):** [[controller-input-map]] "Inside YouTube" and
  [[extension-design]] "YouTube's TV interface": D-pad = arrows, A = Enter, B = Escape and
  "Close YouTube?" on the account page, LT / RT = ±10 s in the player if a key does exactly that,
  no ring. **Brave's sidebar is hidden** for every web app (owner, 2026-10-18), in sub-step 3
  (the profile's setting, checked in the VM). Still to find before the code (a second probe): how
  the account page is told apart (its address), and which key seeks by 10 s.
- **Second probe** (owner, 2026-10-19, test VM; it shows the address and the focused element, and
  measures how far keys sent by a script move the video, on the video's own clock):
  - **The account page has the same address as the home grid** (`/tv#/`); a video is
    `/tv#/watch?v=ID`. The address cannot tell the account page apart.
  - **No key moves the video by 10 s** (watch page): fast-forward (`MediaFastForward`) and rewind
    (`MediaRewind`) pause it (a remote's scrubbing, waiting for a confirmation), the arrows move
    nothing (on a remote they bring up YouTube's controls), `l` and `j` pause it. The play/pause
    media key sent by a script resumes it. (A first run of the probe hit the home grid's preview
    video, which plays in the background: those numbers are discarded.)
  - Brave 1.97.57 has the setting `brave.sidebar.sidebar_show_option` (found in its program).
- **Decided (owner, 2026-10-19):** B asks "Close YouTube?" when **Escape changed nothing** (neither
  the address nor the focused element, about half a second later); **LT / RT stay unused** (seeking
  with YouTube's own progress bar; seeking the video directly rejected). **Sub-step 2 is done.**
