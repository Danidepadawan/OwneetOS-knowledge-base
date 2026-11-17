---
type: step
description: "Adding or changing the cover of a local game with an image from a USB stick or disk: Options on the game, a list of the images by name, the chosen one kept by the console."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.9"
status: in-progress
tags: [step, phase-6]
---
# 6.9 Cover images from a disk *(added 2026-11-09)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **in progress**

- **Why (owner, 2026-11-09):** games on disks often have no cover; picture albums come in a later wave, so Wave 1 takes a cover
  from a stick or disk the player plugs in.
- **What (owner, 2026-11-09):** the player plugs in a stick or external disk with games, videos and pictures. The pictures are
  **not announced** (no notice). Options on a **local game** (with or without a cover) offers **"Add cover image"** (no cover) or
  **"Change cover image"** (it has one), **only while a disk or stick with pictures is connected**. It opens a window that scrolls
  vertically (as the credits list) through the pictures **by name**; a preview only if it is simple enough for Wave 1. The chosen
  picture is **kept** and shown as the game's new cover.
- **Demo first** ([[demo-before-code]]). Texts in the five languages ([[ui-text-and-i18n]]).
- **Choices (owner, 2026-11-09):**
  - The pictures are read from a folder named **Images** in the disk's language: `Images`, `Immagini`, `Bilder`, `Imágenes`
    (French: `Images`), in any case of letters as the Games folder, at the top of the disk (its sub-folders too; to be confirmed with the demo).
  - **Every disk but the console's own** in Wave 1 (USB sticks and disks, and the other internal disks).
  - **A preview** of the selected picture beside the list.
  - The cover is **copied into the game's folder** as `cover.<ext>`, where the console already looks for a game's cover
    (`cover.jpg` / `cover.png` / `cover.jpeg` / `cover.webp`); an earlier `cover.*` is replaced. Proposed, to be confirmed with
    the demo: not offered for a game on a read-only disk (as deleting, [[step-6.8-games-on-disk-delete-and-progress]]).
  - Formats: PNG, JPEG, WebP.
  - **When:** after the fixes already open (the late sound, Steam's virtual controller, the time left, the authors in the credits).
- **Started (owner, 2026-11-17):** the demo first.
- **Demo (2026-11-17):** `design/demos/6.9-cover-images.html`: Options on a local game, "Add / Change cover image" only with
  a disk of pictures plugged in and the game's disk writable; a window with the pictures by name on the left (the Images
  folder's and its sub-folders', a sub-folder's name in front of the file's) and the selected one on the right as the cover
  will look (its middle, cut to the cover's shape); A uses it (the cover changes at once, a short notice), B cancels.
  Waits for the owner's approval.
- **Demo approved (owner, 2026-11-17):** the sub-folders' pictures too (their names in front); the preview as the cover;
  **not offered for a game on a read-only disk** (confirmed). Approved on the condition that down in the Options window
  goes down on the console: it does (the console's windows move by place, `Nav.find`; the demo moved along the list).
- **Built (2026-11-17, owneet-frontend 0.38.37):** `coverImages` (`src/backend/owneet/CoverImages.cpp`) reads the
  pictures of every disk but the console's own (at the start and whenever a disk comes or goes; hidden files and links
  left out; sorted as people read them, 2 before 10) and copies the chosen one as `cover.<ext>`, written apart first and
  then renamed, an earlier `cover.*` removed; `CoverSheet.qml` is the window (the preview is read at the cover's size,
  so a big photo never loads whole). A cover's address carries the file's time, so a cover replaced by one of the same
  name shows at once. Pictures on more than one disk: the disks' names in the line under the title and in front of
  the folders. A picture that cannot be used says so ("This picture could not be used."). Preview steps:
  `tools/preview-steps/cover-images.txt` (`@pictures`). On OWNEETLOG: waits for the owner's test.
- **Open (owner's decision):** WebP needs Qt's image formats plugin (`qt5-imageformats`), which nothing installs today;
  until then the console offers PNG and JPEG only (it lists only what it can read).
