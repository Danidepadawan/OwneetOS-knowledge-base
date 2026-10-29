---
type: decision
description: "The chosen component for each layer: boot, session, frontend, daemon, browser, media, stores, Proton, emulation."
area: architecture
status: active
decided: 2026-10-03
updated: 2026-10-29
legacy: "PROJECT_RULES.md §4"
tags: [decision, architecture]
---
# Architecture stack

| Layer | Choice | Notes |
|---|---|---|
| Boot | **systemd-boot** + **Plymouth** | Silent boot with logo. Auto-detects Windows. [[boot-experience]] |
| Login | **systemd getty autologin** on tty1 for the fixed console user **`owneet`** | No display manager. People's profiles live in the console UI, not in Linux accounts. [[console-session]] |
| Session / compositor | **gamescope** (main), **cage** (fallback) | Inspired by ChimeraOS `gamescope-session`. Overlay via gamescope overlay layer. |
| Frontend / home | **Fork of Pegasus Frontend** (`mmatyas/pegasus-frontend`, `master`, cloned with submodules) + custom QML theme | Qt 5.15 now; **Qt 6 port** planned for a later phase. [[frontend-fork]] |
| Gamepad mappings | **SDL2** + **SDL_GameControllerDB** | |
| System daemon | **`owneetd`**, own component in **Go**, single static binary, **systemd user service of `owneet` (not root)** | Reads controllers via evdev; Guide button (home / quick menu); system-wide on-screen keyboard via uinput; **HTTP + JSON over a Unix socket** (`$XDG_RUNTIME_DIR/owneetd.sock`, no TCP port) for Wi-Fi (NetworkManager), Bluetooth (BlueZ), audio (PipeWire), power; process launch/kill. Root-only tasks (install, updates, disks) go to small separate privileged helpers. [[owneetd]] |
| Streaming apps | **Brave**, installed system-wide (`brave-bin` in `[owneet]`, bundled in the ISO: [[optional-apps]]) | Controlled by the app via **Chromium managed policies** + launch flags (kiosk, **one profile per web app**: each runs and closes on its own). **Widevine turned on by the console** (downloaded by Brave at runtime, never redistributed) **after the user consents to Google's terms**, asked once by the console and again at every new Widevine version ([[step-5.4-netflix]]; until then development builds turn it on silently, 2026-10-19). In Wave 1 a web app stays open until the user closes it, like a game ([[step-5.1-brave-in-the-os]]). |
| Browser extension | **Manifest V3**, Gamepad API, **own spatial navigation** (structure first, sideways by the page's order; WICG polyfill rejected: unmaintained), per-site content scripts; talks to owneetd through a native-messaging host (`owneet-bridge`); text fields use the **console's on-screen keyboard** ([[extension-design]]) | Prefer TV interfaces where they exist (e.g. `youtube.com/tv`). Note: Netflix on Linux is limited to 720p (Widevine L3). |
| Local media | **mpv** | Kodi rejected (too heavy). |
| Steam | System package (multilib, in the image with 32-bit drivers), launched with `-gamepadui` for login/store | [[steam-integration]] |
| Other stores (later) | **legendary** (Epic), **gogdl** / lgogdownloader (GOG) | Heroic rejected (Electron, heavy). |
| Windows games (Wave 1: DRM-free games on disk; stores later) | **umu-launcher** + GE-Proton | [[games-on-disk]] |
| Emulation (later, nice-to-have) | **RetroArch** | |

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-14 | Brave in the OS (step 5.1): one Brave profile per web app; Widevine turned on silently; a web app is closed by the user like a game (staying open in the background is Wave 2). |
| 2026-10-15 | Extension core (step 5.2): own spatial navigation (focusable elements, any tabindex, interactive ARIA roles), a native-messaging bridge to owneetd, the console's keyboard over Brave (full screen in the fallback session). |
| 2026-10-16 | The bridge's native-messaging manifest is one static file installed system-wide by the owneetd package (`/etc/opt/chrome/native-messaging-hosts/`): Brave does not read hosts from the web apps' profiles. A per-user file in Brave's default folder rejected. |
| 2026-10-19 | Widevine: the console asks for the user's consent to Google's terms (once, and again at every new Widevine version) instead of turning it on silently; in step 5.4. Brave's own Widevine question is turned off. |
| 2026-10-24 | Brave's windows that need a mouse are turned off by the managed policies: also its password saving, password leak warnings and address saving (`PasswordManagerEnabled`, `PasswordLeakDetectionEnabled`, `AutofillAddressEnabled` false; found on Spotify's sign-in, verified in the test VM). Each web app keeps its sign-in in its own profile, so nothing is lost. |
| 2026-10-26 | Brave opens only the address owneetd gives (managed policy `RestoreOnStartup` = 5: the session's tabs were reopened at every opening) and its performance alert is off (`--disable-features=PerformanceInterventionUI` in owneetd's command, together with the extension's feature in one switch). |
| 2026-10-29 | Brave's reading views are off for the web apps: Chromium's Reading mode (`ReadAnything` in owneetd's `--disable-features`) and Brave's Speedreader (managed policy `BraveSpeedreaderEnabled` = false). |
