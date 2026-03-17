"""
The Architect 2099 - Conversation Model
المطور: Loard Zoala
"""

import uuid
from sqlalchemy import Column, String, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..base import Base


class Conversation(Base):
    """
    نموذج المحادثة
    
    Attributes:
        id: المعرف الفريد للمحادثة
        user_id: معرف المستخدم
        title: عنوان المحادثة
        specialization: التخصص
        created_at: تاريخ الإنشاء
        updated_at: تاريخ آخر تحديث
    """
    
    __tablename__ = "conversations"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(500), nullable=True)
    specialization = Column(String(100), nullable=False, default="general")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan", order_by="Message.created_at")
    
    def __repr__(self):
        return f"<Conversation {self.id} - {self.title}>"
