# Vercel Serverless Handler for FastAPI
# This file allows FastAPI to run on Vercel's serverless functions

# Import from root main.py
from main import app as application
import os

# Expose the ASGI app for Vercel
__all__ = ["application"]

# Vercel expects a callable named 'app' or 'handler'
app = application
