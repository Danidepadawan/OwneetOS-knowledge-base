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
- While the console's keyboard is open the loop pauses: the frontend reads the controller.

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
  whatever is nearer outside; with none, left goes to the target **just before the current element**
  in the page's order and right to the one **just after** it, wherever they are on screen (for the
  first / last of a row: the target before / after the row; a full-width banner: the elements before
  / after it; accepted side effect: in a vertical list, left / right go to the item above / below).
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
- Text is **inserted by the extension** (`document.execCommand('insertText')`, which fires the
  page's `input` events), not typed through owneetd's virtual keyboard: it works whichever window
  has the focus. The virtual keyboard ([[owneetd-api-input]]) stays a fallback for sites that
  reject it.

## Bridge to owneetd

- An extension cannot reach owneetd's Unix socket, so it talks to a small native-messaging host,
  `owneet-bridge` (Go; messages are JSON with a 4-byte length in front, on stdin / stdout), which
  Brave starts and which talks to owneetd.
- The extension is loaded unpacked from `/usr/share/owneet/extension`, so its id is derived from
  that path and never changes; **no key pair** is made. owneetd writes the host's manifest
  (`allowed_origins` = that id) into each web app's profile (`NativeMessagingHosts/`) at every
  launch.
- The frontend sends the accent colours and the language with its request to open the web app;
  owneetd keeps them and the bridge passes them to the extension when it connects.
- owneetd's endpoints (`/v1/webapps/look`, `/keyboard`, `/text`, `/ask-close`) and events
  (`webapp.keyboard`, `webapp.text`, `webapp.ask_close`): [[owneetd-api-apps]].

## Terms of service

The extension only moves the focus, clicks, scrolls and types; it changes no content and no user
agent. Checked against each service's terms before shipping ([[legal-compliance]]).
