"""
The Architect 2099 - Main Entry Point for Vercel
المطور: Loard Zoala

This file serves as the main entry point for Vercel deployment.
It creates a simple FastAPI app without complex imports.
"""

from fastapi import FastAPI
import time

# Create a simple FastAPI application
app = FastAPI(
    title="The Architect 2099",
    version="1.0.0",
    description="Simple FastAPI app for Vercel",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "The Architect 2099",
        "version": "1.0.0",
        "developer": "Loard Zoala",
        "status": "operational"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": time.time()
    }

# Vercel expects the app to be exposed as 'app' or 'application'
application = app
