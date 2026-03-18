# The Architect 2099 - Vercel Entry Point
# This file serves as the main entry point for Vercel Serverless Functions

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the app from main.py
from main import app

# Vercel expects 'application' or 'app'
application = app
