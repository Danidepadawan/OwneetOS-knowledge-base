---
type: step
description: "Adding or changing the cover of a local game with an image from a USB stick or disk: Options on the game, a list of the images by name, the chosen one kept by the console."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.9"
status: todo
tags: [step, phase-6]
---
# 6.9 Cover images from a disk *(added 2026-11-09)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **to do**

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
    (French: `Images`), at the top of the disk (its sub-folders too; to be confirmed with the demo).
  - **Every disk but the console's own** in Wave 1 (USB sticks and disks, and the other internal disks).
  - **A preview** of the selected picture beside the list.
  - The cover is **copied into the game's folder** as `cover.<ext>`, where the console already looks for a game's cover
    (`cover.jpg` / `cover.png` / `cover.jpeg` / `cover.webp`); an earlier `cover.*` is replaced. Proposed, to be confirmed with
    the demo: not offered for a game on a read-only disk (as deleting, [[step-6.8-games-on-disk-delete-and-progress]]).
  - Formats: PNG, JPEG, WebP.
  - **When:** after the fixes already open (the late sound, Steam's virtual controller, the time left, the authors in the credits).
