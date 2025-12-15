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

### Using the Quest Editor

The project includes a visual quest editor with drag-and-drop support:

```bash
# Start the editor server
./scripts/editor.sh

# Or manually:
python3 scripts/editor_server.py
```

Then open your browser to: **http://localhost:5001/editor.html**

**Editor Features:**
- ✏️ **Add/Edit/Delete Quests** - Visual forms for all quest fields
- 🔄 **Drag & Drop Reordering** - Rearrange quests by dragging
- 📁 **Multi-File Support** - Load and edit different quest JSON files
- ✨ **Character Traits & Curses** - Edit character attributes
- 💾 **Auto-Save** - Changes automatically saved to backend
- 🚀 **Publish** - Generate static `index.html` for deployment

**Publishing Workflow:**
1. Select the quest file you want to work with from the dropdown (defaults to `quests.json`)
2. Make changes in the editor
3. Click the **🚀 Publish** button
4. `index.html` is generated with embedded data from the currently selected quest file
5. Deploy `index.html` to any static hosting service

**Note:** The editor supports loading and editing multiple quest files (e.g., `quests-updated.json`, `quests-backup.json`), and publishing will use whichever file is currently selected.

### Manual Editing

You can also edit quest data manually in `data/quests.json`:

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

Character traits and curses are in `data/character.json`.

## Project Structure

### Core Files
- `index.html` - Published output (standalone, generated from editor)
- `index.template.html` - Template for publishing (with data placeholders)
- `editor.html` - Quest editor interface

### Data Files
- `data/quests.json` - Quest content data
- `data/character.json` - Character traits and curses

### Backend
- `scripts/editor_server.py` - Flask API server for editor
- `scripts/editor.sh` - Editor launcher script
- `scripts/serve.sh` - Simple static file server

### Documentation
- `AGENTS.md` - Repository guidelines for contributors
- `CLAUDE.md` - AI assistant guidance for code work

## Contributing

See `AGENTS.md` for guidelines and conventions.
