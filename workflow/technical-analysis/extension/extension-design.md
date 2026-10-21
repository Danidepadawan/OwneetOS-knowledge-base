---
type: technical-analysis
description: "How the Brave extension drives web pages with a controller: targets, spatial navigation, B, the bridge to owneetd, the console keyboard."
component: extension
tags: [technical-analysis, extension]
---
# Brave extension — design (step 5.2)

Status: **agreed with the owner on 2026-10-15** (moving: 2026-10-16) ([[step-5.2-extension-core]]); being implemented.
Code: `extension/` (Manifest V3), `daemon/cmd/owneet-bridge`. Bindings: [[controller-input-map]]
(section "Inside a web app").

## Input

- A content script in the **top frame** reads the controller through the Gamepad API (a loop on
  `requestAnimationFrame`). Repeat timing, stick dead zone and analog triggers follow the
  [[controller-input-map]]. Standard button 16 (Guide) is **ignored**: Guide is owneetd's
  ([[guide-button]]).
- **The controller is read in the standard layout**, also when Brave does not know it (`mapping`
  ""): Xbox-style controllers on the xpad driver (11 buttons, 8 axes: D-pad on axes 6 / 7,
  triggers on axes 2 / 5) are translated (`extension/content/pad.js`, 2026-10-22); other layouts
  are read as they come ([[controller-without-standard-layout-in-brave]]).
- While the console's keyboard is open the loop pauses: the frontend reads the controller.
- **While the keyboard is open the ring stays around the field** (owner, 2026-10-17, as in the
  approved demo); the loop only stops reading the controller.
- **When the page gets the controller back** (the keyboard closed, the page in front again), the
  buttons still held count only once released and pressed again, and a held direction waits to
  repeat: B that closed the keyboard used to go back in the page too (found 2026-10-17).

## Targets of the D-pad

- **Targets:** natively focusable elements (links with `href`, buttons, inputs, selects,
  textareas, `contenteditable`, `summary`, `iframe`), every element with a `tabindex` (including
  `-1`, needed for rows of cards that the site focuses with its own code), and elements with an
  interactive ARIA role (`button`, `link`, `tab`, `menuitem`, `menuitemcheckbox`, `menuitemradio`,
  `option`, `checkbox`, `radio`, `switch`, `gridcell`, `treeitem`, `slider`, `textbox`,
  `searchbox`, `combobox`), which get `tabindex="-1"` when chosen so that they can take focus.
- **Skipped:** disabled; hidden (`display: none`, `visibility: hidden`, zero size, `inert`, inside
  `aria-hidden="true"`); a target that contains other targets (the smallest one wins).
- Open shadow roots are searched; same-origin iframes too. Cross-origin iframes (e.g. captchas)
  and native `<select>` popups are not driven in 5.2.

## Moving

Agreed with the owner on 2026-10-16, after comparing three versions in the demo of step 5.2 (the
nearest box; the page's order with geometry as a check; the version below). Code:
`extension/content/spatnav.js`, tests `extension/test/spatnav.test.js`.

- **Up / down — structure first.** Candidates are grouped by the smallest box (DOM ancestor) they
  share with the current element; the search starts in the current element's own box and goes
  outward only when nothing fits there. A first pass accepts only candidates **in line** (overlapping
  the current element across the direction) through every level; diagonal ones only in a second pass.
- **Left / right — the container, then the page's order** (the owner's rule). The container is the
  smallest box holding the current element and another target. The best candidate in it wins,
  whatever is nearer outside; with none, left goes to the target **just before the container** in the
  page's order and right to the one **just after** it, wherever they are on screen. An element whose
  container is large (e.g. a full-width banner among rows in the same box) leaves that whole
  container; going to the element's own neighbours instead was tried and rejected (2026-10-16).
- **Within a group**, the distance of the W3C draft *CSS Spatial Navigation Level 1*
  (<https://www.w3.org/TR/css-nav-1/>, Working Draft 2019): euclidean + displacement − alignment −
  √overlap (displacement weighted ×30 sideways, ×2 up / down; alignment ×5). Ties: page order.
- **The column (or row) is remembered** while moving on the same axis: down, down, up, up comes back
  to the same element; it resets on a sideways move or A.
- From the focused target (or, when there is none, the first target on screen in reading order).
  Off-screen candidates count: the chosen one is scrolled fully into view (its scrolling row, then
  the page, with a 15% margin for sticky headers). With no candidate at all, the page (or the row)
  scrolls one step.
- Pure page order was rejected for up / down (popups and sticky bars sit far from their place on
  screen in the page's order); the nearest box alone jumped to sticky bars (seen on YouTube in the
  test VM). Cards with several buttons (YouTube's site) need the per-site rules of step 5.3.
- The selection is drawn as a ring in the palette's accent colour, handed over by the bridge (no
  colour in the extension's code: [[design-tokens]]).

## Buttons

- **A:** clicks the target; on a text field it focuses it and asks for the keyboard.
- **B:** the first that applies: leave full screen → `Escape` to an open dialog
  (`dialog[open]`, `[aria-modal="true"]`) → `history.back()` when the page can go back
  (`navigation.canGoBack`) → otherwise **ask to close**: the console comes to the front with its
  "Close {name}?" dialog; Cancel brings the web app back.
- **Right stick:** scrolls the focused element's scrolling container, else the page.
- X, Y, Menu, LB / RB, LT / RT: nothing in 5.2 (per-site meanings may come in 5.3–5.5).

## Keyboard for web forms

- The **console's own keyboard** (step 3.10). In gamescope it is drawn over Brave; in the fallback
  session (cage) the console comes to the front with the keyboard and a line showing the text
  (dots for passwords), and Done brings the web app back.
- **How it is drawn over Brave in gamescope** (owner, 2026-10-17): a window of its own that
  gamescope shows as an **external overlay** (X11 property `GAMESCOPE_EXTERNAL_OVERLAY` = 1, set
  before the window is first shown; a surface with an alpha channel). gamescope draws it over the
  app on screen, blended with its transparency, and never focuses it: Brave stays in front and
  focused, so the extension keeps typing into the page. The interface's gamepad keys go to that
  keyboard directly (no focused window of its own), and the interface reads the gamepad while the
  web keyboard is open. `STEAM_OVERLAY` (Steam's own overlay; it takes the input only with
  `STEAM_INPUT_FOCUS`) is not used. Facts from gamescope's `steamcompmgr.cpp`. The property is set
  only once the X server knows the window, checked and read back, and set again after showing;
  hiding goes through opacity 0 first: [[gamescope-overlay-window-not-drawn-or-left-on-screen]].
  Verified on FrankenPC (2026-10-17).
- When the keyboard opens, the extension puts the field's cursor at the end, where the console's
  line starts its own (email and number fields allow no cursor to be set: there cursor moves may
  differ).
- Text is **inserted by the extension** (`document.execCommand('insertText')`, which fires the
  page's `input` events), not typed through owneetd's virtual keyboard: it works whichever window
  has the focus. The virtual keyboard ([[owneetd-api-input]]) stays a fallback for sites that
  reject it.
- **The controller never stays stuck** (owner, 2026-10-16). While the keyboard is open the
  extension waits for `keyboard_closed`; a timer in the extension cannot tell "nobody answered"
  from "still typing", so **owneetd** decides: the interface confirms that it shows the keyboard,
  and without that confirmation within **3 seconds** of the open request, or when the interface
  stops while the keyboard is open, owneetd closes the keyboard itself (`keyboard_closed`, no
  `next`) and the extension takes the controller back. It also takes it back when the bridge
  disconnects. The confirmation's form is defined with the frontend part of 5.2.

## Bridge to owneetd

- An extension cannot reach owneetd's Unix socket, so it talks to a small native-messaging host,
  `owneet-bridge` (Go; messages are JSON with a 4-byte length in front, on stdin / stdout), which
  Brave starts and which talks to owneetd.
- The extension is loaded unpacked from `/usr/share/owneet/extension`, so its id is derived from
  that path and never changes; **no key pair** is made. The host's manifest (`allowed_origins` =
  that id) is a **static file installed system-wide** by the owneetd package:
  `/etc/opt/chrome/native-messaging-hosts/org.owneet.bridge.json`, where this Brave build looks.
  It does **not** look in a profile chosen with `--user-data-dir`, so a manifest in each web app's
  profile is never found: [[brave-native-messaging-host-not-found]].
- **Updates of the worker** (owner, 2026-10-16): a profile already used picks up a changed worker
  only when the manifest's version **and** the worker's file name both change
  ([[brave-extension-worker-cached]]). The owneet-base package installs `background.js` as
  `background-<short hash of its content>.js` and writes that name and its own version
  (`<pkgver>.<pkgrel>`) into the installed `manifest.json`; the build checks both. The repository
  keeps `background.js`, and its manifest's `version` is not shipped. Any script the worker loads
  (`importScripts`, none today) gets the same treatment.
- The frontend sends the accent colours and the language with its request to open the web app;
  owneetd keeps them and the bridge passes them to the extension when it connects.
- owneetd's endpoints (`/v1/webapps/look`, `/keyboard`, `/text`, `/ask-close`) and events
  (`webapp.keyboard`, `webapp.text`, `webapp.ask_close`): [[owneetd-api-apps]].

## One navigation per supported app (owner, 2026-10-20)

- **Each supported web app (YouTube, Netflix, Spotify) has its own navigation**, made for its
  pages; they share common code where it fits (the gamepad loop, the repeat timing, the rule for
  buttons held when the page gets the controller back, B's "Close {name}?").
- **The generic navigation above** (any page, 5.2) stays as it is; it still drives the pages an
  app opens outside its own (e.g. sign-in pages). It is **reworked entirely with free web
  browsing** ([[wave-2]]), not before.

## Netflix (step 5.4)

Agreed with the owner on 2026-10-22 ([[step-5.4-netflix]]; bindings: [[controller-input-map]],
"Inside Netflix"). Netflix has no web TV interface: its desktop site, with a navigation of its own.

- **Browsing pages:** a grid of rows: up / down between rows (about the same column; Netflix's top
  menu above the first row), left / right between tiles, sliding the row on at the edge of what is
  visible (Netflix's own arrows). A opens the title window and the selection goes into it.
- **Title window:** the selection stays inside it; B closes it and returns to its tile.
- **Player:** Netflix's controls are brought up as a mouse movement does; the D-pad moves between
  them, A presses; hidden controls: A = Space (pause / play); LT / RT send ← / → (Netflix seeks by
  10 s: measured in the test VM, keys sent by a script work); B closes an open menu, otherwise
  leaves the player.
- **Y** on the browsing pages opens Netflix's search (owner, 2026-10-22).
- **Other pages** (start, sign-in, email code, profile picker) use the generic navigation.
- **How the parts are found** (Netflix's site as of 2026-10-22, read with probes in the test VM;
  its older names, e.g. `.lolomoRow`, `.slider-item`, are gone): rows
  `section[data-uia^="carousel-row-section"]`, each with a `carousel-scroller` and its arrows
  `carousel-hawkins-left-button` / `carousel-hawkins-right-button`; tiles are links named by kind,
  `data-uia` `standard-card`, `episodic-card`, `progress-card`, `ranked-card`, `cloud-game-card`,
  with the title as `aria-label` (about 11 per row in the page, a few visible); top bar
  `navigation+subheader` (`nav-home`, `nav-series`…, search `navigation+actions+search+icon` and
  `…+search+input`); banner `billboard` (`play-video-button`, `billboard-more-info`); title window
  `modal-motion-container-DETAIL_MODAL` (`role="dialog"`; `play-button`, `add-to-my-list`,
  `thumbs-rate-button`, close `previewModal-closebtn`); player `watch-video` (focus on
  `[data-uia="player"]`), controls `control-nav-back`, `control-flag`, `timeline-knob`,
  `control-play-pause-*`, `control-back10`, `control-forward10`, `control-volume-*`,
  `control-next`, `control-episodes`, `control-audio-subtitle`, `control-speed`,
  `control-fullscreen-enter`. Netflix renames its site from time to time: these names live in one
  place of `extension/content/netflix.js`, and anything not found falls back to the generic
  navigation.

## YouTube's TV interface (step 5.3)

Agreed with the owner on 2026-10-18 ([[step-5.3-youtube]]; bindings: [[controller-input-map]],
"Inside YouTube"). owneetd opens `youtube.com/tv` with a TV user agent. Code:
`extension/content/youtube-tv.js`, tests `extension/test/youtube-tv.test.js`.

- The TV interface **does not read the controller** (checked in the test VM): it is made for a
  remote and takes **keyboard keys**. On its address (`www.youtube.com/tv`) the gamepad loop sends
  keys instead of moving the ring: `KeyboardEvent`s `keydown` / `keyup` with `key`, `code` and
  `keyCode` (Brave keeps the `keyCode` of the event's init dictionary), bubbling and composed, on
  the focused element. Keys sent by a script were checked in the VM to move YouTube's selection,
  open, and go back; owneetd's virtual keyboard is not needed.
- **No ring and no spatial navigation** there: YouTube draws its own selection. Its own keyboard is
  used for search; signing in is done on a phone (a QR code or `yt.be/activate`).
- The rules of the loop stay: the map's repeat timing; buttons held when the page gets the
  controller back count only once pressed again; Guide is never read.
- **B** sends Escape; where Escape has nothing left to go back to (YouTube's "Welcome back" account
  page, the end of its back chain) it asks to close the web app, as in 5.2. That page has the
  same address as the home grid (`/tv#/`), so **"nothing left" means that Escape changed nothing**:
  about half a second after it, neither the address nor the focused element has changed (owner,
  2026-10-19). It does not depend on YouTube's element names; a slow reaction could rarely bring
  the dialog up by mistake (Cancel is selected, B closes it). Recognising the page by YouTube's
  element names rejected: it would break silently when YouTube renames them.
- **No seeking keys:** no key of the TV interface moves the video by 10 s (fast-forward and rewind
  pause it, waiting for a confirmation, as a remote's scrubbing), so LT / RT do nothing; seeking
  is done with YouTube's own progress bar. The extension never changes the video itself (setting
  its position directly rejected, owner, 2026-10-19).
- Every other page (e.g. Google's sign-in pages) keeps the navigation above.

## Terms of service

The extension only moves the focus, clicks, scrolls and types; it changes no content and no user
agent. Checked against each service's terms before shipping ([[legal-compliance]]). YouTube's TV
user agent is not the extension's: owneetd passes it to Brave from the catalogue
([[step-5.3-youtube]]).
