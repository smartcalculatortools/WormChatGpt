"""
The Architect 2099 - Modules Module
المطور: Loard Zoala

This module contains all the specialization modules:
- Cyber Security
- Crime Plans
- Adult Content
- Software Tools
- Non-Tech Content
"""

from .cyber_security import CyberSecurityModule
from .crime_plans import CrimePlansModule
from .adult_content import AdultContentModule
from .software_tools import SoftwareToolsModule
from .non_tech_content import NonTechContentModule

__all__ = [
    "CyberSecurityModule",
    "CrimePlansModule",
    "AdultContentModule",
    "SoftwareToolsModule",
    "NonTechContentModule",
]
