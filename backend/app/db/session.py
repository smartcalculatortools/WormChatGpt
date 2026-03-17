"""
The Architect 2099 - Database Session Module
المطور: Loard Zoala
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from .base import Base
from app.core.config import settings

# Sync Engine
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Async Engine
async_engine = create_async_engine(settings.DATABASE_ASYNC_URL)
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


def get_db() -> Session:
    """
    الحصول على جلسة قاعدة البيانات
    
    Yields:
        Session: جلسة قاعدة البيانات
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_async_db() -> AsyncSession:
    """
    الحصول على جلسة قاعدة البيانات غير المتزامنة
    
    Yields:
        AsyncSession: جلسة قاعدة البيانات غير المتزامنة
    """
    async with AsyncSessionLocal() as session:
        yield session


def init_db():
    """
    تهيئة قاعدة البيانات وإنشاء الجداول
    """
    Base.metadata.create_all(bind=engine)
