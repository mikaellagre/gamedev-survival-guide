# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the GameDev Survival Guide - a documentation project providing practical notes on surviving and thriving in the video game industry. The repository contains an interactive HTML tool for capturing software engineering expectations across different levels, with plans for additional markdown-based documentation chapters.

## Project Structure

### Core Application Files
- `index.html`: Published output (standalone, generated from editor, deployed to static hosting)
- `index.template.html`: Template for publishing with `{{QUESTS_DATA}}` and `{{CHARACTER_DATA}}` placeholders
- `editor.html`: Visual quest editor with drag-and-drop support

### Data Files
- `data/quests.json`: Quest content data (16 quests with full metadata)
- `data/character.json`: Character traits and curses (editable via editor)

### Backend
- `scripts/editor_server.py`: Flask API server providing quest/character CRUD and publishing
- `scripts/editor.sh`: Launcher script for editor server
- `scripts/serve.sh`: Simple static file server for published site

### Documentation
- `AGENTS.md`: Repository guidelines and conventions for contributors
- `CLAUDE.md`: This file - AI assistant guidance

### Planned Structure
- `docs/`: Markdown chapters and guides with numbered prefixes for ordering
- `assets/`: Images and media referenced by documentation
- `examples/`: Minimal, runnable samples referenced by chapters
- `tests/`: Content validation checks

## Development Commands

### Viewing the Published Site

To view the published site locally:

```bash
# Start static file server
./scripts/serve.sh

# Or use Python directly
python3 -m http.server 8000
```

Then open: http://localhost:8000

### Using the Quest Editor

To edit quests, character traits, and publish:

```bash
# Start editor server (Flask with auto-save API)
./scripts/editor.sh

# Or manually
python3 scripts/editor_server.py
```

Then open: http://localhost:5001/editor.html

**Editor Features:**
- Visual quest editor with forms for all fields
- Drag-and-drop quest reordering
- Multi-file support: Load and edit different quest JSON files
- Character traits/curses editor
- Auto-save (1-second debounce)
- Publish button generates standalone `index.html`

**Publishing Workflow:**
1. Make changes in editor at http://localhost:5001/editor.html
2. Select the quest file you want to publish from the dropdown
3. Click **🚀 Publish** button
4. `index.html` is generated with embedded data from the selected quest file
5. Deploy `index.html` to static hosting (works without backend)

**Architecture:**
- `editor.html` loads data from Flask API (`/api/quests?file=...`, `/api/character`)
- Quest file selector allows switching between different quest JSON files
- Changes auto-save back to the selected `data/*.json` file
- Publishing uses the currently selected quest file and injects into `index.template.html` → `index.html`
- Published `index.html` is standalone (no fetch, no backend needed)

### Planned Commands

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