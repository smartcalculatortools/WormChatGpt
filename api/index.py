# Vercel Serverless Function Handler for FastAPI
# This file is the entry point for Vercel serverless functions

import sys
import os

# Add the backend directory to the path so we can import app
backend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'backend')
sys.path.insert(0, backend_path)

# Import the FastAPI app
from app.main import app

# Export the app for Vercel (must be named 'app' or 'handler')
application = app
