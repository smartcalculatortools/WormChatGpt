"""
The Architect 2099 - Vercel Serverless Entry Point
المطور: Loard Zoala

This file serves as the entry point for Vercel serverless deployment.
It imports and exposes the FastAPI application.
"""

# Import from root main.py
from main import app

# Vercel expects the app to be exposed as 'app' or 'application'
application = app
