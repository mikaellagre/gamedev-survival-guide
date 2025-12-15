#!/bin/bash
# Launch editor server with Flask backend
# Usage: ./scripts/editor.sh

cd "$(dirname "$0")/.."

echo "🚀 GameDev Survival Guide - Editor"
echo ""

# Check if flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Flask not found. Installing Flask and Flask-CORS..."
    pip3 install flask flask-cors
    echo ""
fi

echo "Starting Editor Server..."
echo ""

python3 scripts/editor_server.py
