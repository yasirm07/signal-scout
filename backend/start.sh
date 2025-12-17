#!/bin/bash
# Simple startup script for the backend
# Run this from the backend directory: bash start.sh

echo "🚀 Starting Signal Scout Backend..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "   Create a .env file with your API keys (see README.md)"
    echo ""
fi

# Check if virtual environment exists (optional but recommended)
if [ ! -d "venv" ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

echo "✅ Starting server on http://localhost:8000"
echo "   Press Ctrl+C to stop"
echo ""

uvicorn app.main:app --reload --port 8000

