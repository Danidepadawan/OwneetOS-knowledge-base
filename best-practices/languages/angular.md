---
type: best-practice
description: "Angular conventions of the website: folders, file names (.component.ts, .service.ts), models and enums next to their component, signals, texts and colours."
scope: language
tags: [best-practice, angular, website]
---
# Angular (the website)

Comes from: [[website]] (owner, 2026-10-20). Applies to `OwneetOS-website/`.

- **A real Angular application structure**, one folder per component or service:
  - `src/app/core/components/<name>/` — the site's components, the root and the pages too (`app`,
    `intro`, `header`, `footer`, `page`, `home`, `console-screen`, `feature-carousel`, `guide`,
    `faq`, `credits`, `privacy`, `contribute`), next to
  - `src/app/core/services/<name>/` — app-wide services (`i18n`, `sections`, `notice`);
  - `src/app/shared/components/<name>/` — components used in several places (`icon`, `wordmark`).
  - No `pages` folder and no `components` folder inside a component (owner, 2026-10-20); related
    components may be grouped in a sub-folder of `core/components/`.
  - Only configuration stays in `src/app/` (`app.config*.ts`, `app.routes*.ts`).
- **File names carry their type** (Angular's "2016" style): `header.component.ts`, `.html`,
  `.scss`, `.spec.ts`; `i18n.service.ts`; classes `HeaderComponent`, `I18nService`.
  `angular.json` sets it for `ng generate`, so generated files follow it.
- **Interfaces and types** go in `<name>.model.ts`, **enums** in `<name>.enum.ts`, **inside the
  component's (or service's) folder but outside its `.component.ts`**. Constant data generated
  from other sources goes in `<name>.data.ts` (e.g. `icon.data.ts`).
- Components are standalone, with `templateUrl` and `styleUrl` (no inline templates); state in
  signals; `inject()` for dependencies; browser-only code in `afterNextRender` (the pages are
  prerendered).
- Texts only through `I18nService` and the JSON files in `src/i18n/` ([[ui-text-and-i18n]]);
  colours only through the tokens in `src/styles.scss` ([[design-tokens]]).
- **Never link the site's own files from the root** (`/fonts/...`): the site lives under a base
  path on GitHub Pages (`/OwneetOS-website/` until the domain). Links go through the router and
  `<base href>`; stylesheet URLs to `public/` are relative (`fonts/...`) and listed in
  `externalDependencies` ([[step-7.8c-website-publishing]]).
- SPDX header on every file ([[license-headers]]); the Angular CLI's statistics stay off.
