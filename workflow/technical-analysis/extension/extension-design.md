---
type: technical-analysis
description: "How the Brave extension drives web pages with a controller: targets, spatial navigation, B, the bridge to owneetd, the console keyboard."
component: extension
tags: [technical-analysis, extension]
---
# Brave extension — design (step 5.2)

Status: **agreed with the owner on 2026-10-15** ([[step-5.2-extension-core]]); being implemented.
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

- From the focused target (or, when there is none, the first target at the top left of the screen)
  the candidates are those whose box lies past the current one in the pressed direction.
- **Distance** = the gap along the direction + 2 × the offset across it; a candidate that overlaps
  the current one across the direction wins over one that does not.
- Off-screen candidates count: the chosen one is scrolled fully into view (its scrolling row, then
  the page). When there is no candidate at all in that direction, the page (or the focused
  element's scrolling container) scrolls one step.
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
