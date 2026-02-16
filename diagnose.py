#!/usr/bin/env python
"""
Troubleshooting script to diagnose and fix application issues
"""

import requests
import sys
import os

def test_backend():
    """Test if backend is responding"""
    print("\n" + "="*60)
    print("TESTING BACKEND")
    print("="*60)
    
    try:
        response = requests.get("http://localhost:5000/", timeout=5)
        if response.status_code == 200:
            print("✅ Backend is responding")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Backend returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend at http://localhost:5000")
        print("   Make sure backend is running with: cd kg_backend && python run.py")
        return False
    except Exception as e:
        print(f"❌ Backend error: {str(e)}")
        return False

def test_frontend():
    """Test if frontend is responding"""
    print("\n" + "="*60)
    print("TESTING FRONTEND")
    print("="*60)
    
    try:
        response = requests.get("http://localhost:8501", timeout=5)
        if response.status_code == 200:
            print("✅ Frontend is responding")
            return True
        else:
            print(f"❌ Frontend returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to frontend at http://localhost:8501")
        print("   Make sure frontend is running with: cd kg_frontend && streamlit run app.py")
        return False
    except Exception as e:
        print(f"❌ Frontend error: {str(e)}")
        return False

def test_auth():
    """Test authentication endpoints"""
    print("\n" + "="*60)
    print("TESTING AUTHENTICATION")
    print("="*60)
    
    try:
        # Test register
        reg_data = {
            "username": f"test_{os.urandom(4).hex()}",
            "email": f"test_{os.urandom(4).hex()}@example.com",
            "password": "testpass123"
        }
        
        response = requests.post("http://localhost:5000/api/auth/register", json=reg_data, timeout=5)
        if response.status_code in [201, 409]:  # 201=Created, 409=Already exists
            print("✅ Registration endpoint working")
            if response.status_code == 201:
                print(f"   Created user: {reg_data['username']}")
        else:
            print(f"❌ Registration failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
        # Test login
        login_data = {"username": reg_data['username'], "password": reg_data['password']}
        response = requests.post("http://localhost:5000/api/auth/login", json=login_data, timeout=5)
        if response.status_code == 200:
            print("✅ Login endpoint working")
            token = response.json().get('access_token')
            if token:
                print(f"   Token received: {token[:20]}...")
                return token
        else:
            print(f"❌ Login failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Auth test error: {str(e)}")
        return False

def test_upload(token):
    """Test file upload"""
    print("\n" + "="*60)
    print("TESTING FILE UPLOAD")
    print("="*60)
    
    if not token:
        print("⚠️  Skipping upload test - no auth token")
        return False
    
    try:
        # Create test file
        test_file_path = "/tmp/test_upload.txt"
        with open(test_file_path, 'w') as f:
            f.write("Test content for knowledge graph")
        
        with open(test_file_path, 'rb') as f:
            files = {'file': ('test_upload.txt', f, 'text/plain')}
            data = {'name': 'Test Upload'}
            headers = {'Authorization': f'Bearer {token}'}
            
            response = requests.post(
                "http://localhost:5000/api/dataset/upload",
                files=files,
                data=data,
                headers=headers,
                timeout=10
            )
            
        if response.status_code == 201:
            print("✅ File upload working")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Upload failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Upload test error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*15 + "APPLICATION DIAGNOSTICS" + " "*19 + "║")
    print("╚" + "="*58 + "╝")
    
    backend_ok = test_backend()
    frontend_ok = test_frontend()
    
    if backend_ok:
        token = test_auth()
        if token:
            test_upload(token)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Backend:  {'✅ OK' if backend_ok else '❌ FAILED'}")
    print(f"Frontend: {'✅ OK' if frontend_ok else '❌ FAILED'}")
    
    if not backend_ok or not frontend_ok:
        print("\n📌 NEXT STEPS:")
        if not backend_ok:
            print("   1. Start backend: cd kg_backend && python run.py")
        if not frontend_ok:
            print("   2. Start frontend: cd kg_frontend && streamlit run app.py")
    else:
        print("\n✨ All systems operational!")
        print("   Open http://localhost:8501 in your browser")
    
    print()

if __name__ == '__main__':
    main()
