# GameDev Survival Guide

An interactive documentation project providing practical notes on surviving and thriving in the video game industry.

## Quick Start

### Running Locally

This project requires a local web server to run (due to data loading via fetch API):

```bash
# Option 1: Use the serve script
./scripts/serve.sh

# Option 2: Use Python directly
python3 -m http.server 8000

# Option 3: Use Node.js http-server
npm install -g http-server
http-server -p 8000
```

Then open your browser to: **http://localhost:8000**

### Editing Quest Data

Quest content is stored in `data/quests.json`. Edit this file to update quest information without touching the HTML/CSS/JavaScript code.

Each quest has the following structure:

```json
{
  "id": 1,
  "title": "Quest Title",
  "image": null,
  "questType": "main",
  "level": 10,
  "description": "Quest description...",
  "tools": ["Tool1", "Tool2"],
  "xpGained": 300,
  "monstersDefeated": [
    { "name": "Challenge", "description": "Description" }
  ],
  "lootDropped": [
    { "name": "Lesson", "description": "Description" }
  ]
}
```

## Project Structure

- `index.html` - Main interactive matrix tool (layout only)
- `data/quests.json` - Quest content data
- `scripts/serve.sh` - Local development server script
- `AGENTS.md` - Repository guidelines for contributors
- `CLAUDE.md` - AI assistant guidance for code work

## Contributing

See `AGENTS.md` for guidelines and conventions.
