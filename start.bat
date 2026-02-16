@echo off
REM Knowledge Graph System - Windows Startup Script
REM This script will install dependencies and run the system

echo.
echo ============================================================================
echo  Knowledge Graph Construction System - Auto Setup and Run
echo ============================================================================
echo.

REM Change to project directory
cd /d "%~dp0"

REM Install Python packages
echo [STEP 1/3] Installing dependencies...
echo.

python -m pip install -q Flask Flask-SQLAlchemy Flask-JWT-Extended Flask-CORS Werkzeug streamlit requests pandas networkx 2>nul

if errorlevel 1 (
    echo Error installing packages. Make sure Python is installed.
    pause
    exit /b 1
)

echo [STEP 1/3] OK - Dependencies installed
echo.

REM Display startup information
echo [STEP 2/3] Starting Backend and Frontend...
echo.
echo ============================================================================
echo  System Starting...
echo ============================================================================
echo.
echo Backend API:   http://localhost:5000
echo Frontend UI:   http://localhost:8501
echo.
echo Open http://localhost:8501 in your browser
echo.
echo Press Ctrl+C to stop the system
echo.
echo ============================================================================
echo.

REM Run the Python startup script
python start.py

if errorlevel 1 (
    echo.
    echo Error starting application. Please check:
    echo 1. Python is installed
    echo 2. All dependencies are available
    echo 3. No other service is using ports 5000 or 8501
    echo.
    pause
    exit /b 1
)

exit /b 0
