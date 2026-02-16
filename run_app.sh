#!/bin/bash
# Knowledge Graph System - Startup Script for Linux/Mac

echo "========================================"
echo "Knowledge Graph System - Starting Up"
echo "========================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/Update dependencies
echo "Installing backend dependencies..."
cd kg_backend
pip install -r requirements.txt -q
python -m spacy download en_core_web_sm -q

cd ..
echo "Installing frontend dependencies..."
cd kg_frontend
pip install -r requirements.txt -q

cd ..

# Start backend and frontend
echo ""
echo "========================================"
echo "Starting Backend (Flask) on port 5000"
echo "Starting Frontend (Streamlit) on port 8501"
echo "========================================"
echo ""

# Start Flask backend in background
cd kg_backend
python app.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 3

# Start Streamlit frontend
cd ../kg_frontend
streamlit run app.py

# Kill backend when frontend closes
kill $BACKEND_PID
