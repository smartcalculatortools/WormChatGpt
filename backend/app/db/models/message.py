"""
The Architect 2099 - Message Model
المطور: Loard Zoala
"""

import uuid
from sqlalchemy import Column, String, Text, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..base import Base


class Message(Base):
    """
    نموذج الرسالة
    
    Attributes:
        id: المعرف الفريد للرسالة
        conversation_id: معرف المحادثة
        role: الدور (user أو assistant)
        content: محتوى الرسالة
        specialization: التخصص
        created_at: تاريخ الإنشاء
    """
    
    __tablename__ = "messages"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False, index=True)
    role = Column(String(50), nullable=False)  # 'user' or 'assistant'
    content = Column(Text, nullable=False)
    specialization = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=func.now())
    
    # Relationships
    conversation = relationship("Conversation", back_populates="messages")
    
    def __repr__(self):
        return f"<Message {self.id} - {self.role}>"
