"""
The Architect 2099 - User Model
المطور: Loard Zoala
"""

import uuid
from sqlalchemy import Column, String, Boolean, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..base import Base


class User(Base):
    """
    نموذج المستخدم
    
    Attributes:
        id: المعرف الفريد للمستخدم
        username: اسم المستخدم
        email: البريد الإلكتروني
        password_hash: كلمة المرور المشفرة
        is_admin: هل المستخدم مدير
        created_at: تاريخ الإنشاء
        updated_at: تاريخ آخر تحديث
    """
    
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(255), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    conversations = relationship("Conversation", back_populates="user", cascade="all, delete-orphan")
    settings = relationship("Settings", back_populates="user", cascade="all, delete-orphan", uselist=False)
    
    def __repr__(self):
        return f"<User {self.username}>"
