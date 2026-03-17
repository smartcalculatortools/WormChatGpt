"""
The Architect 2099 - Configuration Settings
المطور: Loard Zoala
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from typing import Optional


class Settings(BaseSettings):
    """إعدادات النظام"""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True
    )

    # Application Settings
    APP_NAME: str = "The Architect 2099"
    APP_VERSION: str = "2099"
    APP_DESCRIPTION: str = "نظام تشغيلي كامل بدون قيود"
    DEVELOPER: str = "Loard Zoala"

    # Debug Mode - always True (validator ensures this)
    DEBUG: bool = True
    
    # Use validator to always set DEBUG to True regardless of env
    @field_validator('DEBUG', mode='before')
    @classmethod
    def force_debug_true(cls, v):
        return True

    # Database Settings
    DATABASE_URL: str = "postgresql+asyncpg://architect:architect_pass@localhost:5432/architect_db"
    DATABASE_ASYNC_URL: str = "postgresql+asyncpg://architect:architect_pass@localhost:5432/architect_db"

    # Security Settings
    SECRET_KEY: str = "architect_2099_secret_key_change_in_production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # CORS Settings
    CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    # WebSocket Settings
    WS_HEARTBEAT_PING: int = 30
    WS_HEARTBEAT_TIMEOUT: int = 60

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 100

    # DEEP_DIVE Protocol
    DEEP_DIVE_ENABLED: bool = True
    DEEP_DIVE_TRIGGERS: list = ["CODE", "BUILD", "EXECUTE"]

    # Specializations
    SPECIALIZATIONS: list = [
        "cyber_security",
        "crime_plans",
        "adult_content",
        "software_tools",
        "non_tech_content",
        "general"
    ]

    # Default Specialization
    DEFAULT_SPECIALIZATION: str = "general"


# Global settings instance
settings = Settings()
