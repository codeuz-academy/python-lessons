<div align="center">
  <img src="https://belajarpython.com/img/logo-belajarpython-for-github.png" alt="Belajarpython logo"><br><br>
</div>

# Belajarpython

Belajarpython is an open-source Eleventy website for learning Python in English and Uzbek.

## Project Scope

This repository currently includes:

- Step-by-step Python tutorials (`content/en/tutorial`, `content/uz/tutorial`)
- Data Structures & Algorithms roadmap/content pages (`content/{en,uz}/{data-structures,algorithms}`)
- Browser-based Python tools under `tools/` (for example Online IDE and formatter utilities)

This repository does not contain a forum/Q&A backend.

## Tech Stack

- Node.js + npm
- Eleventy (`@11ty/eleventy`)
- Tailwind CSS

## Prerequisites

- Node.js `20.x`
- npm `10.x` (or npm version bundled with Node 20)

## Local Development

Install dependencies:

```bash
npm ci
```

Start development server + Tailwind watch:

```bash
npm run dev
```

Build production output:

```bash
npm run build
```

Run validation checks:

```bash
npm run check
```

## URL Behavior

- Root `/` redirects to `/en/`
- English homepage: `/en/`
- Uzbek homepage: `/uz/`
- Tutorial URLs:
  - `/en/tutorial/{slug}/`
  - `/uz/tutorial/{slug}/`

## Content Structure

- English tutorials: `content/en/tutorial/{basic,intermediate,advanced}/*.md`
- Uzbek tutorials: `content/uz/tutorial/{basic,intermediate,advanced}/*.md`
- Data structures: `content/{en,uz}/data-structures/*.md`
- Algorithms: `content/{en,uz}/algorithms/*.md`

## Quality Gate Expectations

Before opening a pull request, ensure all of these pass:

```bash
npm run build
npm run check
```

`npm run check` validates metadata consistency, localization structure, internal links, and JSON-LD integrity.
It also validates runnable Python snippets for standalone execution (with nearby-snippet context fallback).

If a snippet intentionally requires external setup (network, DB, local modules, framework app context), mark it with:

```python
# non-runnable: requires external environment/setup
```

## Analytics Configuration

Analytics is optional and disabled by default. To enable GA4 tracking, set:

```bash
GA4_MEASUREMENT_ID=G-XXXXXXXXXX
```

## Contributing

See the contribution guide: [.github/CONTRIBUTING.md](./.github/CONTRIBUTING.md)

## License

MIT — see [LICENSE](./LICENSE)
