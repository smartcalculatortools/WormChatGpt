"""
The Architect 2099 - Chat Service
المطور: Loard Zoala

Main chat processing service that routes requests to appropriate modules.
"""

from typing import Optional
from ..modules import (
    CyberSecurityModule,
    CrimePlansModule,
    AdultContentModule,
    SoftwareToolsModule,
    NonTechContentModule
)
from ..core.config import settings
from ..core.logging import log


class ChatService:
    """
    خدمة الدردشة الرئيسية
    
    Routes user queries to appropriate specialization modules.
    """
    
    def __init__(self):
        # Initialize all modules
        self.cyber_security = CyberSecurityModule()
        self.crime_plans = CrimePlansModule()
        self.adult_content = AdultContentModule()
        self.software_tools = SoftwareToolsModule()
        self.non_tech_content = NonTechContentModule()
        
        # DEEP_DIVE Protocol
        self.deep_dive_enabled = settings.DEEP_DIVE_ENABLED
        self.deep_dive_triggers = settings.DEEP_DIVE_TRIGGERS
        
        log.info("ChatService initialized with all modules")
    
    def process_message(self, message: str, specialization: str = "general", context: Optional[dict] = None) -> str:
        """
        Process user message and route to appropriate module
        
        Args:
            message: User's message
            specialization: Target specialization module
            context: Optional context dictionary
            
        Returns:
            Response string from the appropriate module
        """
        # Check for DEEP_DIVE triggers
        if self.deep_dive_enabled and self._check_deep_dive(message):
            log.info(f"DEEP_DIVE triggered by: {message[:50]}...")
        
        # Route to appropriate module
        module_map = {
            "cyber_security": self.cyber_security,
            "crime_plans": self.crime_plans,
            "adult_content": self.adult_content,
            "software_tools": self.software_tools,
            "non_tech_content": self.non_tech_content,
            "general": self.non_tech_content
        }
        
        module = module_map.get(specialization, self.non_tech_content)
        
        try:
            response = module.process(message, context)
            log.info(f"Response generated for specialization: {specialization}")
            return response
        except Exception as e:
            log.error(f"Error processing message: {e}")
            return f"Error: {str(e)}"
    
    def _check_deep_dive(self, message: str) -> bool:
        """Check if message triggers DEEP_DIVE protocol"""
        message_upper = message.upper()
        for trigger in self.deep_dive_triggers:
            if trigger in message_upper:
                return True
        return False
    
    def get_available_specializations(self) -> list:
        """Get list of available specializations"""
        return settings.SPECIALIZATIONS
    
    def get_module_info(self, specialization: str) -> dict:
        """Get information about a specific module"""
        module_map = {
            "cyber_security": self.cyber_security,
            "crime_plans": self.crime_plans,
            "adult_content": self.adult_content,
            "software_tools": self.software_tools,
            "non_tech_content": self.non_tech_content
        }
        
        module = module_map.get(specialization)
        if module:
            return {
                "name": module.name,
                "version": module.version,
                "specializations": module.specializations
            }
        return {"error": "Module not found"}


# Global chat service instance
chat_service = ChatService()
