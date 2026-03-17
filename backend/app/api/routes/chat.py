"""
The Architect 2099 - Chat Routes
المطور: Loard Zoala
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
import uuid

from ...services.chat_service import chat_service
from ...core.logging import log

router = APIRouter()


class ChatMessage(BaseModel):
    """Chat message schema"""
    message: str
    specialization: str = "general"
    conversation_id: Optional[str] = None


class ChatResponse(BaseModel):
    """Chat response schema"""
    response: str
    specialization: str
    conversation_id: str


@router.post("/completions", response_model=ChatResponse)
async def chat_completions(chat_input: ChatMessage):
    """
    Send a message and get response from The Architect
    
    Args:
        chat_input: ChatMessage with message and specialization
        
    Returns:
        ChatResponse with response text
    """
    try:
        log.info(f"Processing chat request for specialization: {chat_input.specialization}")
        
        # Process message through chat service
        response = chat_service.process_message(
            message=chat_input.message,
            specialization=chat_input.specialization
        )
        
        # Generate or use existing conversation ID
        conversation_id = chat_input.conversation_id or str(uuid.uuid4())
        
        return ChatResponse(
            response=response,
            specialization=chat_input.specialization,
            conversation_id=conversation_id
        )
        
    except Exception as e:
        log.error(f"Error in chat completions: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/specializations")
async def get_specializations():
    """Get available specializations"""
    return {"specializations": chat_service.get_available_specializations()}


@router.get("/module/{specialization}")
async def get_module_info(specialization: str):
    """Get module information"""
    info = chat_service.get_module_info(specialization)
    if "error" in info:
        raise HTTPException(status_code=404, detail=info["error"])
    return info
