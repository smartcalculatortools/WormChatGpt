"""
The Architect 2099 - Main Application
المطور: Loard Zoala

FastAPI application entry point.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger
import time

from .core.config import settings
from .core.logging import log
from .db.session import init_db
from .api.routes import chat, conversations, users, settings as settings_router

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Startup event
@app.on_event("startup")
async def startup_event():
    """Application startup"""
    try:
        log.info("The Architect 2099 is starting...")
        log.info(f"Developer: {settings.DEVELOPER}")
        log.info(f"Version: {settings.APP_VERSION}")
        log.info(f"Debug Mode: {settings.DEBUG}")

        # Initialize database (async)
        from .db.session import init_db_async
        await init_db_async()
        log.info("Database initialized")

        # Load modules
        from .modules import (
            CyberSecurityModule,
            CrimePlansModule,
            AdultContentModule,
            SoftwareToolsModule,
            NonTechContentModule
        )
        log.info("All modules loaded successfully")

        log.info("The Architect 2099 is ready")
    except Exception as e:
        log.warning(f"Startup warning: {e}")
        log.info("The Architect 2099 is ready (without database)")


# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all requests"""
    start_time = time.time()
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    log.info(f"{request.method} {request.url.path} - {response.status_code} - {duration:.2f}s")
    
    return response


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "developer": settings.DEVELOPER,
        "status": "operational",
        "deep_dive_enabled": settings.DEEP_DIVE_ENABLED
    }


# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": time.time()
    }


# Include routers
app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(conversations.router, prefix="/api/v1/conversations", tags=["Conversations"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(settings_router.router, prefix="/api/v1/settings", tags=["Settings"])


# Exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    log.error(f"Global exception: {exc}")
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": str(exc) if settings.DEBUG else "An unexpected error occurred"
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
