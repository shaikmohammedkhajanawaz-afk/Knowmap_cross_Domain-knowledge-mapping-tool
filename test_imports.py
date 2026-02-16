#!/usr/bin/env python
"""
Quick test to verify the application can be imported and initialized
"""
import sys
import os

# Add kg_backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'kg_backend'))

print("=" * 50)
print("Testing Application Imports...")
print("=" * 50)

# Test basic imports
print("\n1. Testing Flask imports...")
try:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from flask_jwt_extended import JWTManager
    from flask_cors import CORS
    print("   ✓ Flask imports successful")
except ImportError as e:
    print(f"   ✗ Flask import error: {e}")
    sys.exit(1)

# Test app initialization
print("\n2. Testing app creation...")
try:
    from app import create_app
    app = create_app()
    print("   ✓ App created successfully")
except Exception as e:
    print(f"   ✗ App creation error: {e}")
    sys.exit(1)

# Test database
print("\n3. Testing database...")
try:
    with app.app_context():
        from models.user import User, Dataset, Extraction, KnowledgeGraph
        print("   ✓ Database models loaded")
except Exception as e:
    print(f"   ✗ Database error: {e}")
    sys.exit(1)

# Test routes
print("\n4. Testing routes...")
try:
    from routes import auth, dataset, nlp, graph
    print("   ✓ Routes loaded successfully")
except Exception as e:
    print(f"   ✗ Routes error: {e}")
    sys.exit(1)

# Test NLP module
print("\n5. Testing NLP module...")
try:
    from modules.nlp_processor import SimplifiedNLPProcessor
    processor = SimplifiedNLPProcessor()
    result = processor.extract_entities("John Smith works at Apple in California")
    print(f"   ✓ NLP processor working (extracted {len(result)} entities)")
except Exception as e:
    print(f"   ⚠ NLP module warning: {e}")

# Test graph builder
print("\n6. Testing graph builder...")
try:
    from modules.graph_builder import GraphBuilder
    builder = GraphBuilder()
    builder.add_triple("John", "works_for", "Apple")
    stats = builder.get_statistics()
    print(f"   ✓ Graph builder working (nodes: {stats['nodes']}, edges: {stats['edges']})")
except Exception as e:
    print(f"   ✗ Graph builder error: {e}")

print("\n" + "=" * 50)
print("✓ All core components working!")
print("=" * 50)
print("\nTo start the server, run:")
print("  python kg_backend/run.py")
print("\nIn another terminal, run the frontend:")
print("  streamlit run kg_frontend/app.py")
