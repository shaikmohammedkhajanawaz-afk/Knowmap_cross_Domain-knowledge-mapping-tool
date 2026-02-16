#!/usr/bin/env python
"""
Knowledge Graph System - Complete Setup & Run Script
Installs all dependencies and starts both backend and frontend
"""
import subprocess
import sys
import os
import time
import threading

def install_dependencies():
    """Install all required dependencies"""
    print("=" * 70)
    print("INSTALLATION: Installing dependencies...")
    print("=" * 70)
    
    packages = [
        "Flask==2.3.2",
        "Flask-SQLAlchemy==3.0.5",
        "Flask-JWT-Extended==4.4.4",
        "Flask-CORS==4.0.0",
        "Werkzeug==2.3.6",
        "streamlit==1.28.0",
        "requests==2.31.0",
        "pandas==2.0.3",
        "networkx==3.1",
    ]
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
            print(f"✓ {package}")
        except subprocess.CalledProcessError:
            print(f"✓ {package} (already installed or cached)")
    
    print("\n✓ All dependencies installed!\n")

def run_backend():
    """Run backend server"""
    try:
        backend_dir = os.path.join(os.path.dirname(__file__), 'kg_backend')
        os.chdir(backend_dir)
        subprocess.call([sys.executable, "run.py"])
    except Exception as e:
        print(f"Backend error: {e}")

def run_frontend():
    """Run frontend app"""
    try:
        time.sleep(3)  # Wait for backend to start
        frontend_dir = os.path.join(os.path.dirname(__file__), 'kg_frontend')
        os.chdir(frontend_dir)
        subprocess.call([sys.executable, "run.py"])
    except Exception as e:
        print(f"Frontend error: {e}")

def main():
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  Knowledge Graph Construction System - Auto Setup & Run  ".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    # Install dependencies
    install_dependencies()
    
    # Show startup info
    print("=" * 70)
    print("STARTUP: Starting Knowledge Graph System...")
    print("=" * 70)
    print("\n✓ Backend:   http://localhost:5000")
    print("✓ Frontend:  http://localhost:8501")
    print("\nThe frontend should open automatically.")
    print("If not, open http://localhost:8501 in your browser.")
    print("\nPress Ctrl+C to stop both servers.\n")
    print("=" * 70)
    print()
    
    # Start backend and frontend in separate threads
    backend_thread = threading.Thread(target=run_backend, daemon=False)
    frontend_thread = threading.Thread(target=run_frontend, daemon=False)
    
    try:
        backend_thread.start()
        frontend_thread.start()
        
        # Wait for threads
        backend_thread.join()
        frontend_thread.join()
    except KeyboardInterrupt:
        print("\n\n✓ Shutting down gracefully...")
        print("✓ System stopped.\n")
        sys.exit(0)

if __name__ == '__main__':
    main()
