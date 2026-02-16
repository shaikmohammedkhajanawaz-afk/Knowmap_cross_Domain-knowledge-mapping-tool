@echo off
REM Knowledge Graph System - Startup Script for Windows

echo ========================================
echo Knowledge Graph System - Starting Up
echo ========================================

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install/Update dependencies
echo Installing backend dependencies...
cd kg_backend
pip install -r requirements.txt -q
REM Optional: Download spaCy model (comment out if want to skip)
REM python -m spacy download en_core_web_sm -q

cd ..
echo Installing frontend dependencies...
cd kg_frontend
pip install -r requirements.txt -q

cd ..

REM Start backend and frontend
echo.
echo ========================================
echo Starting Backend (Flask) on port 5000
echo Starting Frontend (Streamlit) on port 8501
echo ========================================
echo.

REM Start Flask backend in new window
start cmd /k "cd kg_backend && python app.py"

REM Wait for backend to start
timeout /t 3 /nobreak

REM Start Streamlit frontend
cd kg_frontend
streamlit run app.py

pause
