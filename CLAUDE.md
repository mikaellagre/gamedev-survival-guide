# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the GameDev Survival Guide - a documentation project providing practical notes on surviving and thriving in the video game industry. The repository contains an interactive HTML tool for capturing software engineering expectations across different levels, with plans for additional markdown-based documentation chapters.

## Project Structure

- `index.html`: Interactive matrix tool for mapping software engineering expectations by level and topic (layout only)
- `data/quests.json`: Quest content data (separate from layout)
- `scripts/serve.sh`: Local development server
- `AGENTS.md`: Repository guidelines and conventions for contributors
- `docs/` (planned): Markdown chapters and guides with numbered prefixes for ordering
- `assets/` (planned): Images and media referenced by documentation
- `examples/` (planned): Minimal, runnable samples referenced by chapters
- `tests/` (planned): Content validation checks

## Development Commands

To run the project locally (required for data loading):

```bash
# Start local development server
./scripts/serve.sh

# Or use Python directly
python3 -m http.server 8000
```

Then open: http://localhost:8000

**Note:** The project uses `fetch()` to load quest data from `data/quests.json`, which requires a web server (file:// protocol will not work).

### Planned Commands

When implemented, the following commands are planned:
- `make build` or `scripts/build.sh`: Generate static site or exportable bundle
- `make check` or `scripts/check.sh`: Run all content checks (lint, links, spelling)

## Content Guidelines

### Markdown Conventions
- Use ATX headers (`#`, `##`), one H1 per file
- Sentence case for titles
- Wrap at ~100 characters where reasonable
- Fenced code blocks with language hints (e.g., ```json, ```cpp)

### File Naming
- Use kebab-case for all filenames
- Chapters use numeric prefixes for ordering (e.g., `01-introduction.md`, `02-production-pipelines.md`)

### Testing & Validation (Planned)
- Markdown linting: `markdownlint` with `.markdownlint.json` config
- Spelling checks: `cspell` with custom gamedev dictionaries
- Link validation: `lychee` or similar tool
- Test files mirror docs structure (e.g., `tests/02-production-links.spec.yml`)

### Commit Guidelines
Follow Conventional Commits:
- `docs:` for documentation changes
- `fix:` for corrections
- `feat:` for new features or chapters
- Example: `docs: add physics chapter intro`

### Assets & Media
- Store images under `assets/images/`
- Use relative paths and meaningful alt text
- Consider Git LFS for large binary files
- Optimize images before committing