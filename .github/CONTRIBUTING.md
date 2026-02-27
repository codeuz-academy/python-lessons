# Contributing to Belajarpython.com

Thank you for contributing.

## Development Setup

1. Install dependencies:
   ```bash
   npm ci
   ```
2. Start local development:
   ```bash
   npm run dev
   ```
3. Build the site:
   ```bash
   npm run build
   ```
4. Run validation checks:
   ```bash
   npm run check
   ```

## Content Guidelines

- Keep tutorials clear, practical, and beginner-friendly.
- Use consistent front matter (`layout`, `title`, `order`, `permalink`).
- Place tutorials under `content/{en|uz}/tutorial/{basic|intermediate|advanced}/`.
- Use locale-first permalinks only:
  - English tutorial: `/en/tutorial/{slug}/`
  - Uzbek tutorial: `/uz/tutorial/{slug}/`
- Use `lang: en` or `lang: uz` in localized pages/tutorials.
- Wrap code-related prose tokens in inline code (for example: `if`, `else`, `for`, `while`, `True`, `False`, `None`, `{}`).
- Add descriptive image `alt` text.
- Verify internal links and JSON-LD output with `npm run check`.
- Keep localized repository docs under `docs/i18n/uz/` (these are not website pages).

## Pull Request Checklist

- `npm run build` succeeds.
- `npm run check` succeeds.
- New/updated content has working links and metadata.
- Changes are scoped to the issue/task.

## Reporting Issues

Please open an issue with:
- A clear description of the problem.
- Steps to reproduce (if applicable).
- Expected and actual behavior.
