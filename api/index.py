# Vercel Serverless Function Handler for FastAPI
# This file is the entry point for Vercel serverless functions

import sys
import os

# Add the parent directory to the path so we can import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

# Export the app for Vercel
def handler(request):
    """Vercel serverless handler for FastAPI"""
    return app
