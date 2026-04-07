#!/bin/bash
echo "Starting Base Platform..."
cd backend
if [ ! -d "venv" ]; then
  echo "Creating virtualenv..."
  python -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt -q
if [ ! -f ".env" ]; then
  cp .env.example .env
  echo "⚠️  Created .env — please add your OPENAI_API_KEY"
  exit 1
fi
echo "✓ Backend starting at http://localhost:8000"
echo "✓ Open frontend/index.html in your browser"
uvicorn app.main:app --reload --port 8000
