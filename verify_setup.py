import os
import sys

# Quick test script to verify setup

print("Knowledge Graph System - Setup Verification")
print("=" * 50)

# Check Python version
print(f"✓ Python Version: {sys.version}")

# Check key packages
required_packages = {
    'flask': 'Flask',
    'flask_sqlalchemy': 'Flask-SQLAlchemy',
    'flask_jwt_extended': 'Flask-JWT-Extended',
    'spacy': 'spaCy',
    'streamlit': 'Streamlit',
    'networkx': 'NetworkX'
}

print("\nChecking required packages:")
missing = []
for module, name in required_packages.items():
    try:
        __import__(module)
        print(f"  ✓ {name} installed")
    except ImportError:
        print(f"  ✗ {name} NOT installed")
        missing.append(name)

if missing:
    print(f"\nMissing packages: {', '.join(missing)}")
    print("Run: pip install -r requirements.txt")
else:
    print("\n✓ All packages installed!")

# Check spaCy model (optional)
print("\nChecking spaCy model (optional):")
try:
    try:
        import spacy as sp
        sp.load('en_core_web_sm')
        print("  ✓ en_core_web_sm model available")
    except:
        print("  - en_core_web_sm model not found (optional, system will use fallback)")
except:
    pass

# Check directories
print("\nChecking directories:")
dirs = ['uploads', 'kg_backend', 'kg_frontend']
for d in dirs:
    if os.path.exists(d):
        print(f"  ✓ {d}/ exists")
    else:
        print(f"  ✗ {d}/ NOT found")

print("\n" + "=" * 50)
print("Setup verification complete!")
print("\nTo start the application:")
print("  Windows: run_app.bat")
print("  Linux/Mac: bash run_app.sh")
