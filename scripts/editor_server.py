#!/usr/bin/env python3
"""
GameDev Survival Guide - Editor Backend API
Simple Flask server providing quest editor functionality
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from pathlib import Path
import shutil

app = Flask(__name__)
CORS(app)  # Enable CORS for local development

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
QUESTS_FILE = DATA_DIR / 'quests.json'
CHARACTER_FILE = DATA_DIR / 'character.json'
TEMPLATE_FILE = BASE_DIR / 'index.template.html'
OUTPUT_FILE = BASE_DIR / 'index.html'


# ==========================================
# UTILITY FUNCTIONS
# ==========================================

def read_json(filepath):
    """Read JSON file safely"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        return {'error': f'Invalid JSON: {str(e)}'}

def write_json(filepath, data):
    """Write JSON file safely with backup"""
    # Create backup if file exists
    if filepath.exists():
        backup_path = filepath.with_suffix('.json.backup')
        shutil.copy2(filepath, backup_path)

    # Write new data
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return True


# ==========================================
# API ENDPOINTS
# ==========================================

@app.route('/api/quest-files', methods=['GET'])
def get_quest_files():
    """List all available quest JSON files"""
    try:
        quest_files = []
        for file in DATA_DIR.glob('*.json'):
            # Only include files that start with 'quest' or are named quests.json
            if file.name.startswith('quest') or file.name == 'quests.json':
                quest_files.append(file.name)

        # Sort with quests.json first, then alphabetically
        quest_files.sort(key=lambda x: (x != 'quests.json', x))
        return jsonify(quest_files)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/quests', methods=['GET'])
def get_quests():
    """Get all quests from specified file"""
    # Get quest file from query parameter, default to quests.json
    quest_file = request.args.get('file', 'quests.json')

    # Security: prevent directory traversal
    if '..' in quest_file or '/' in quest_file or '\\' in quest_file:
        return jsonify({'error': 'Invalid file name'}), 400

    quest_path = DATA_DIR / quest_file

    # Check file exists
    if not quest_path.exists():
        return jsonify({'error': f'Quest file not found: {quest_file}'}), 404

    data = read_json(quest_path)
    if data is None:
        return jsonify({'error': 'Quests file not found'}), 404
    if isinstance(data, dict) and 'error' in data:
        return jsonify(data), 500
    return jsonify(data)


@app.route('/api/quests', methods=['POST'])
def save_quests():
    """Save quests data to specified file"""
    try:
        # Get quest file from query parameter, default to quests.json
        quest_file = request.args.get('file', 'quests.json')

        # Security: prevent directory traversal
        if '..' in quest_file or '/' in quest_file or '\\' in quest_file:
            return jsonify({'error': 'Invalid file name'}), 400

        quest_path = DATA_DIR / quest_file

        data = request.json

        # Validate data structure
        if not isinstance(data, list):
            return jsonify({'error': 'Data must be an array'}), 400

        # Basic validation for each quest
        for quest in data:
            required = ['id', 'title', 'questType', 'level', 'description',
                       'tools', 'xpGained', 'monstersDefeated', 'lootDropped']
            if not all(field in quest for field in required):
                return jsonify({'error': f'Quest missing required fields: {quest.get("title", "unknown")}'}), 400

            # Validate quest type
            if quest['questType'] not in ['main', 'side']:
                return jsonify({'error': f'Invalid quest type: {quest["questType"]}'}), 400

        # Write to file
        write_json(quest_path, data)
        return jsonify({'success': True, 'message': f'Quests saved to {quest_file}'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/character', methods=['GET'])
def get_character():
    """Get character data"""
    data = read_json(CHARACTER_FILE)
    if data is None:
        # Return default if file doesn't exist
        return jsonify({'traits': [], 'curses': []})
    if isinstance(data, dict) and 'error' in data:
        return jsonify(data), 500
    return jsonify(data)


@app.route('/api/character', methods=['POST'])
def save_character():
    """Save character data"""
    try:
        data = request.json

        # Validate structure
        if not isinstance(data, dict) or 'traits' not in data or 'curses' not in data:
            return jsonify({'error': 'Invalid character data structure'}), 400

        if not isinstance(data['traits'], list) or not isinstance(data['curses'], list):
            return jsonify({'error': 'Traits and curses must be arrays'}), 400

        write_json(CHARACTER_FILE, data)
        return jsonify({'success': True, 'message': 'Character data saved'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/publish', methods=['POST'])
def publish():
    """
    Generate static index.html with embedded data
    Publishes from the specified quest file (default: quests.json)
    """
    try:
        # Get quest file from query parameter, default to quests.json
        quest_file = request.args.get('file', 'quests.json')

        # Security: prevent directory traversal
        if '..' in quest_file or '/' in quest_file or '\\' in quest_file:
            return jsonify({'error': 'Invalid file name'}), 400

        quest_path = DATA_DIR / quest_file

        # Check file exists
        if not quest_path.exists():
            return jsonify({'error': f'Quest file not found: {quest_file}'}), 404

        # Read template
        if not TEMPLATE_FILE.exists():
            return jsonify({'error': 'Template file not found'}), 404

        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
            template = f.read()

        # Read data files
        quests = read_json(quest_path)
        character = read_json(CHARACTER_FILE)

        if quests is None:
            return jsonify({'error': 'Quests data not found'}), 404

        # Default character data if not exists
        if character is None:
            character = {'traits': [], 'curses': []}

        # Embed data in template
        quests_js = f'const quests = {json.dumps(quests, indent=2)};'
        character_js = f'const characterData = {json.dumps(character, indent=2)};'

        # Replace placeholders
        output = template.replace('/* {{QUESTS_DATA}} */', quests_js)
        output = output.replace('/* {{CHARACTER_DATA}} */', character_js)

        # Create backup of existing index.html if it exists
        if OUTPUT_FILE.exists():
            backup_path = OUTPUT_FILE.with_suffix('.html.backup')
            shutil.copy2(OUTPUT_FILE, backup_path)

        # Write output file
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(output)

        return jsonify({
            'success': True,
            'message': f'Published successfully from {quest_file}',
            'file': str(OUTPUT_FILE),
            'source': quest_file
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==========================================
# STATIC FILE SERVING
# ==========================================

@app.route('/')
def serve_editor():
    """Serve editor by default"""
    return send_from_directory(BASE_DIR, 'editor.html')


@app.route('/<path:path>')
def serve_files(path):
    """Serve static files"""
    try:
        return send_from_directory(BASE_DIR, path)
    except:
        return jsonify({'error': 'File not found'}), 404


# ==========================================
# MAIN
# ==========================================

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 GameDev Survival Guide - Editor Server")
    print("=" * 60)
    print(f"📁 Base directory: {BASE_DIR}")
    print(f"📂 Data directory: {DATA_DIR}")
    print()
    print("🌐 Server running at:")
    print("   http://localhost:5001")
    print()
    print("✏️  Editor available at:")
    print("   http://localhost:5001/editor.html")
    print()
    print("📝 API Endpoints:")
    print("   GET      /api/quest-files       - List available quest files")
    print("   GET/POST /api/quests?file=...   - Load/save quests (default: quests.json)")
    print("   GET/POST /api/character          - Load/save character data")
    print("   POST     /api/publish?file=...  - Publish to index.html (default: quests.json)")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)

    app.run(debug=True, port=5001, host='localhost')
