"""
The Architect 2099 - Vercel Serverless Entry Point
المطور: Loard Zoala

This file serves as the entry point for Vercel serverless deployment.
It imports and exposes the FastAPI application.
"""

import sys
import os

# Add backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

# Import the FastAPI app from backend
from app.main import app

# Vercel expects the app to be exposed as 'app' or 'application'
application = app
