# Repository Guidelines

## Project Structure & Module Organization
- `docs/`: Markdown chapters and guides. Use numeric prefixes for order (e.g., `01-introduction.md`, `02-production-pipelines.md`).
- `assets/`: Media referenced by docs. Prefer `assets/images/` and `assets/audio/`.
- `examples/`: Minimal, runnable samples linked from chapters.
- `scripts/`: Local automation (lint, link-check, image optimization).
- `tests/`: Content checks mirroring docs structure.

## Build, Test, and Development Commands
This repo has no enforced tooling yet. Prefer a simple `Makefile` or `scripts/` wrappers so commands stay stable across machines.

```sh
# Local docs server with live reload
make serve        # or: scripts/serve.sh

# Build static site / exportable bundle
make build        # or: scripts/build.sh

# Run all content checks (lint, links, spelling)
make check        # or: scripts/check.sh
```

## Coding Style & Naming Conventions
- Markdown: ATX headers (`#`, `##`), one H1 per file; sentence‑case titles; wrap lines ~100 chars when practical.
- Filenames: kebab‑case; chapters use numeric prefixes (e.g., `03-art-pipeline.md`).
- Code blocks: fenced with language hints (e.g., ```json, ```cpp).
- Images: store under `assets/images/`; use relative paths and meaningful alt text.
- Links: prefer relative links within `docs/`; avoid hard‑coded domains.

## Testing Guidelines
- Linting: `markdownlint` using repo config (`.markdownlint.json`).
- Spelling: `cspell` with custom dictionaries for gamedev terms.
- Links: link checker (e.g., `lychee`) pinned via `scripts/check.sh`.
- Naming: tests mirror docs (e.g., `tests/02-production-links.spec.yml`).
- Run: `make check` or `scripts/check.sh`.

## Commit & Pull Request Guidelines
- Commits: use Conventional Commits (e.g., `docs: add physics chapter intro`, `fix: correct shader code block`).
- PRs: keep focused; include a clear summary, linked issues (e.g., `Closes #123`), and screenshots for visual changes.
- Content changes: note major restructures in the PR body; avoid committing large binaries—use `assets/` and consider Git LFS when necessary.

## Security & Configuration Tips
- Never commit secrets. Provide sample variables in `.env.example` and document usage in `docs/`.
- Optimize large assets and version thoughtfully; prefer links or small extracts in `examples/` when appropriate.

