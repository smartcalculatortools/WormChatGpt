"""
The Architect 2099 - Security Module
المطور: Loard Zoala
"""

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from .config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    التحقق من صحة كلمة المرور
    
    Args:
        plain_password: كلمة المرور الأصلية
        hashed_password: كلمة المرور المشفرة
        
    Returns:
        bool: True إذا كانت كلمة المرور صحيحة
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    تشفير كلمة المرور
    
    Args:
        password: كلمة المرور الأصلية
        
    Returns:
        str: كلمة المرور المشفرة
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    إنشاء رمز وصول (JWT)
    
    Args:
        data: البيانات المراد تشفيرها في الرمز
        expires_delta: مدة صلاحية الرمز
        
    Returns:
        str: رمز JWT
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """
    فك تشفير رمز الوصول
    
    Args:
        token: رمز JWT
        
    Returns:
        Optional[dict]: البيانات المفككة أو None إذا فشل فك التشفير
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None
