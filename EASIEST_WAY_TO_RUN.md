# ✅ EASIEST WAY TO RUN

## Option 1: One-Click Windows Startup (Recommended)

Double-click this file:
```
start.bat
```

Or run in PowerShell:
```powershell
.\start.bat
```

That's it! The system will:
- ✓ Install all dependencies
- ✓ Start the backend (port 5000)
- ✓ Start the frontend (port 8501)
- ✓ Open automatically

---

## Option 2: Python One-Liner

```powershell
python start.py
```

---

## Option 3: Manual (Two Terminals)

### Terminal 1 - Backend:
```powershell
cd kg_backend
python run.py
```

### Terminal 2 - Frontend:
```powershell
cd kg_frontend
pip install streamlit requests pandas
streamlit run app.py
```

Then open: **http://localhost:8501**

---

## If Something Goes Wrong

### Error: "Python not found"
- Install Python from python.org
- Make sure to check "Add Python to PATH"

### Error: "Port already in use"
```powershell
# Kill process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Error: "Module not found"
```powershell
pip install Flask Flask-SQLAlchemy Flask-JWT-Extended Flask-CORS streamlit requests pandas
```

### Still not working?
Check the detailed guides:
- `RUN_WITHOUT_ERRORS.md` - Complete troubleshooting
- `ERROR_FIX_GUIDE.md` - Advanced issues

---

## Once Running

1. Go to http://localhost:8501
2. Register a user (username, email, password)
3. Login
4. Upload a document
5. Process text
6. Create knowledge graphs
7. Explore the system

**Enjoy your Knowledge Graph System!** 🎉
