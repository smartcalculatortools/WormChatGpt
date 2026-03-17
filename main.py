"""
The Architect 2099 - Main Entry Point for Vercel
المطور: Loard Zoala

This file serves as the main entry point for Vercel deployment.
"""

import sys
import os

# Add backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Import the FastAPI app from backend
from app.main import app

# Vercel expects the app to be exposed as 'app' or 'application'
application = app
