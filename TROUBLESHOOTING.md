# 🔧 **TROUBLESHOOTING GUIDE - Unknown Error Fix**

## ❌ **Common Unknown Errors & Solutions**

### **1. Page Not Loading (Blank Screen)**
**Cause:** Frontend not connected to backend
**Fix:**
```powershell
# Check if backend is running
curl http://localhost:5000/

# If it fails, start backend in new terminal:
cd kg_backend
python run.py
```

---

### **2. "Unable to Connect" Error**
**Cause:** Backend server crashed or not responding
**Solution:**
1. Check backend terminal for errors
2. If errors appear, restart:
   ```powershell
   cd kg_backend
   python run.py
   ```

---

### **3. Login/Auth Errors**
**Possible Causes:**
- Database not initialized
- Wrong credentials
- Token expired

**Fix:**
1. Try registering a new account
2. Or use demo credentials: `demo` / `demo123`
3. If neither works, clear browser cookies:
   - Press `F12` → Application → Clear Storage

---

### **4. Upload Shows "Unknown Error"**
**Check These Steps:**
1. ✅ Are you logged in? (Top right should show username)
2. ✅ File format correct? (txt, pdf, csv, json, xml only)
3. ✅ File size < 50MB?
4. ✅ Backend running and showing requests?

**Debug:**
```powershell
# Watch backend logs while uploading
# You should see:
# - "Upload request from user_id: X"
# - "File received: filename.txt"
# - "File saved successfully"

# If you see errors, they'll show here
```

---

### **5. Browser Console Errors (F12)**
If you see errors in browser console:

**TypeError: Cannot read property 'X' of undefined**
- Likely API endpoint not returning expected data
- Check backend is running: `curl http://localhost:5000/`

**CORS Error**
- Backend not allowing requests
- Restart backend: `python run.py`

**Network Error: Failed to fetch**
- Backend crashed or not responding
- Check backend terminal for errors

---

## 🛠️ **Complete Restart Procedure**

If everything is broken, do this:

### **Step 1: Kill All Running Processes**
```powershell
# Kill all Python processes
Get-Process python | Stop-Process -Force

# Or individually:
# Press Ctrl+C in each terminal
```

### **Step 2: Clear Database & Cache**
```powershell
cd kg_backend

# Remove old database
Remove-Item kg_users.db -ErrorAction SilentlyContinue

# Remove uploads
Remove-Item uploads/* -ErrorAction SilentlyContinue -Recurse
```

### **Step 3: Restart Everything**

**Terminal 1 - Backend:**
```powershell
cd c:\Users\Lenovo\Desktop\infosys_project\kg_backend
python run.py
```
Wait for: `✓ Running on http://127.0.0.1:5000`

**Terminal 2 - Frontend:**
```powershell
cd c:\Users\Lenovo\Desktop\infosys_project\kg_frontend
streamlit run app.py
```
Wait for: `Local URL: http://localhost:8501`

### **Step 4: Test in Browser**
1. Open http://localhost:8501
2. Go to Auth tab
3. Create new account
4. Try uploading a file

---

## 🔍 **Detailed Debugging**

### **Check Backend Logs**
Look at the terminal running `python run.py`:
- Search for `ERROR` or `Exception`
- Look for request details
- Check for 404, 500 status codes

### **Check Frontend Network**
1. Open browser (Chrome/Edge/Firefox)
2. Press `F12` → Network tab
3. Try to upload file
4. Look for failed requests (red)
5. Click on failed request → Response tab
6. See exact error message

### **Check Database**
```powershell
cd kg_backend
# Check if database exists and has tables
# If you see SQLite errors, delete database:
Remove-Item kg_users.db
# Restart backend to recreate
```

---

## ✨ **If All Else Fails**

**Nuclear Option - Complete Reset:**
```powershell
cd c:\Users\Lenovo\Desktop\infosys_project

# Remove all cache and compiled files
Remove-Item -Path kg_backend\__pycache__ -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path kg_backend\modules\__pycache__ -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path kg_backend\routes\__pycache__ -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path kg_backend\models\__pycache__ -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path kg_backend\kg_users.db -Force -ErrorAction SilentlyContinue
Remove-Item -Path kg_backend\uploads -Recurse -Force -ErrorAction SilentlyContinue

# Reinstall requirements
cd kg_backend
pip install -r requirements.txt --upgrade

# Start fresh
python run.py
```

---

## 📞 **Still Have Issues?**

### **Check These Files:**
1. **Backend Terminal Output**
   - Copy any error messages
   - Look for stack traces

2. **Browser Console (F12)**
   - Errors in JavaScript
   - Network failures

3. **Backend Logs Location**
   - Terminal where `python run.py` is running
   - Shows all API requests and responses

### **Required Information When Reporting:**
1. Exact error message
2. What were you doing when it happened
3. Backend terminal output
4. Browser console errors (F12)
5. Which file you were trying to upload

---

## ✅ **Verification Checklist**

- [ ] Backend runs without errors
- [ ] Frontend shows "Local URL: http://localhost:8501"
- [ ] Can open http://localhost:8501 in browser
- [ ] Can create account or login
- [ ] Can select and upload a file
- [ ] File appears in "Your Files" list
- [ ] Can extract entities
- [ ] Can create knowledge graph

If all checkboxes pass, your system is working! 🎉
