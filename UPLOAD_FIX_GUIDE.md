# 🚀 Quick Start Guide - Upload File Fix

## ✅ **Complete Setup Instructions**

### **Step 1: Ensure Backend is Running**
```powershell
cd kg_backend
python run.py
```
You should see: `✓ Running on http://127.0.0.1:5000`

---

### **Step 2: Start Frontend in Another Terminal**
```powershell
cd kg_frontend
streamlit run app.py
```
You should see: `Local URL: http://localhost:8501`

---

### **Step 3: Create an Account or Login**

#### **Option A: Create New Account**
1. Open http://localhost:8501 in browser
2. Go to **Auth** tab
3. **Register** section:
   - Username: `testuser`
   - Email: `test@example.com`
   - Password: `test123`
4. Click **Create Account**

#### **Option B: Use Demo Account (After Restart)**
If you restart the backend, use:
- **Username:** `demo`
- **Password:** `demo123`

---

### **Step 4: Login**
1. Go to **Auth** tab
2. **Login** section:
   - Username: (your username)
   - Password: (your password)
3. Click **Sign In**
4. You should see: ✓ Logged in!

---

### **Step 5: Upload File**
1. Go to **Files** tab
2. **Upload** section:
   - Click "Choose file"
   - Select one of these sample files:
     - `sample_data.txt`
     - `sample_relations.csv`
     - `sample_documents.json`
   - Optional: Enter a custom name
   - Click **Upload**
3. You should see: ✅ File uploaded successfully!

---

## 🔧 **If Upload Still Shows Error:**

### **Check Backend Console**
Look at the terminal running the backend - it will show detailed error logs like:
- `Upload request from user_id: 1`
- `File received: sample_data.txt`
- `File saved successfully`

### **Common Issues & Fixes:**

| Error | Cause | Fix |
|-------|-------|-----|
| 🔒 Login first | Not authenticated | Login to the app |
| ❌ Connection error | Backend not running | Start backend with `python run.py` |
| ❌ Invalid credentials | Wrong password | Check username/password |
| ❌ No file provided | Form submission error | Refresh page and try again |
| ❌ File type not allowed | Wrong extension | Use: txt, pdf, csv, json, xml |

---

## 📝 **Debug Steps**

1. **Check if token exists:**
   - Open browser DevTools (F12)
   - Go to Application tab
   - Look for any auth tokens in storage

2. **Monitor backend logs:**
   - Watch the terminal running `python run.py`
   - It shows every request and error

3. **Test API directly:**
   ```powershell
   # Test if backend is responding
   curl http://localhost:5000/
   
   # Should show status
   ```

---

## ✨ **After Successful Upload:**

1. Go to **Process** tab
2. Click **Extract ✓** button
3. View extracted entities and relations
4. Go to **Graphs** tab
5. Create and visualize your knowledge graph!

---

## 📞 **Need Help?**

- Backend errors → Check terminal where `python run.py` is running
- Frontend errors → Check browser console (F12)
- Login issues → Make sure you created account first
- File issues → Use the sample files provided in the project
