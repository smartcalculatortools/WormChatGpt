"""
The Architect 2099 - Settings Model
المطور: Loard Zoala
"""

import uuid
from sqlalchemy import Column, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..base import Base


class Settings(Base):
    """
    نموذج الإعدادات
    
    Attributes:
        id: المعرف الفريد للإعدادات
        user_id: معرف المستخدم
        theme: الثيم (dark/light)
        default_specialization: التخصص الافتراضي
        deep_dive_enabled: تفعيل بروتوكول DEEP_DIVE
        created_at: تاريخ الإنشاء
        updated_at: تاريخ آخر تحديث
    """
    
    __tablename__ = "settings"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    theme = Column(String(50), default="dark")
    default_specialization = Column(String(100), default="general")
    deep_dive_enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="settings")
    
    def __repr__(self):
        return f"<Settings {self.user_id} - {self.theme}>"
