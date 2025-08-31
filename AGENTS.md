# Repository Guidelines

These guidelines help contributors keep the Gamedev Survival Guide organized, consistent, and easy to maintain. Adjust as the project evolves.

## Project Structure & Module Organization
- `docs/`: Markdown chapters and guides. Use numbered prefixes for order (e.g., `01-introduction.md`, `02-production-pipelines.md`).
- `assets/`: Images and media referenced by docs. Prefer `images/` and `audio/` subfolders.
- `examples/`: Minimal, runnable samples referenced by chapters.
- `scripts/`: Local automation (lint, link-check, image optimization).
- `tests/`: Content checks (broken links, style rules).

## Build, Test, and Development Commands
This repo currently has no enforced tooling. When adding it, prefer a simple Makefile or `scripts/` wrappers so commands stay stable across machines. Recommended targets:
- `make serve`: Start a local docs server (e.g., MkDocs/Docusaurus) with live reload.
- `make build`: Produce a static site or exportable bundle.
- `make check`: Run all content checks (lint, links, spelling).
Example equivalents: `scripts/serve.sh`, `scripts/build.sh`, `scripts/check.sh`.

## Coding Style & Naming Conventions
- Markdown: ATX headers (`#`, `##`), one H1 per file; sentence case titles; wrap at ~100 chars where reasonable.
- Filenames: kebab-case; chapters use numeric prefixes for ordering.
- Code blocks: fenced with language hint (e.g., ```json, ```cpp).
- Images: store under `assets/images/`; use relative paths and meaningful alt text.
- Links: prefer relative links within `docs/`; avoid hard-coded domains when possible.

## Testing Guidelines
- Linting: Use `markdownlint` with a repo config (`.markdownlint.json`).
- Spelling: Use `cspell` with custom dictionaries for gamedev terms.
- Links: Use a link checker (e.g., `lychee`) pinned via `scripts/check.sh`.
Naming: tests mirror docs (e.g., `tests/02-production-links.spec.yml`). Run with `make check` or the script wrapper.

## Commit & Pull Request Guidelines
- Commits: Follow Conventional Commits (e.g., `docs: add physics chapter intro`, `fix: correct shader code block`).
- PRs: Keep focused; include a clear summary, linked issues (`Closes #123`), and screenshots for visual changes.
- Content changes: note major restructures in the PR body; avoid committing large binaries—use `assets/` and consider Git LFS if needed.

## Security & Configuration Tips
- Do not commit secrets. Place sample variables in `.env.example` and document usage.
- Large assets or project files should be optimized and versioned thoughtfully (prefer links or small extracts in `examples/`).

