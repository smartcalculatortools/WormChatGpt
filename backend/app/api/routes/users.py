"""
The Architect 2099 - Users Routes
المطور: Loard Zoala
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

router = APIRouter()


class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    is_admin: bool = False


@router.post("/register", response_model=UserResponse)
async def register(user: UserRegister):
    """Register new user"""
    # TODO: Implement user registration
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/login")
async def login(user: UserLogin):
    """User login"""
    # TODO: Implement user login
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/profile", response_model=UserResponse)
async def get_profile():
    """Get user profile"""
    # TODO: Implement get profile
    raise HTTPException(status_code=501, detail="Not implemented")


@router.put("/profile", response_model=UserResponse)
async def update_profile():
    """Update user profile"""
    # TODO: Implement update profile
    raise HTTPException(status_code=501, detail="Not implemented")
