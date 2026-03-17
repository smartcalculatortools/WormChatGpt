"""
The Architect 2099 - API Routes
المطور: Loard Zoala
"""

from .chat import router as chat_router
from .conversations import router as conversations_router
from .users import router as users_router
from .settings import router as settings_router

__all__ = ["chat_router", "conversations_router", "users_router", "settings_router"]
