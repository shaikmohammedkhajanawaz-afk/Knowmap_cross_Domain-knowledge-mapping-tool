#!/usr/bin/env python
"""
Script to create a demo user account for testing
Run this script before testing the application
"""

import sys
import os

# Add the backend to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'kg_backend'))

from kg_backend.app import create_app
from kg_backend.models.user import db, User

def create_demo_user():
    """Create a demo user for testing"""
    app = create_app()
    
    with app.app_context():
        # Check if demo user already exists
        demo_user = User.query.filter_by(username='demo').first()
        
        if demo_user:
            print("✓ Demo user 'demo' already exists")
            print(f"  Email: {demo_user.email}")
            return
        
        # Create new demo user
        user = User(
            username='demo',
            email='demo@example.com'
        )
        user.set_password('demo123')
        
        db.session.add(user)
        db.session.commit()
        
        print("✓ Demo user created successfully!")
        print("  Username: demo")
        print("  Password: demo123")
        print("  Email: demo@example.com")

if __name__ == '__main__':
    create_demo_user()
