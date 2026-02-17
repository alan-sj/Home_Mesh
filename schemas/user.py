from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    name: str
    timezone: str
    preferred_input: str  # text / voice


class UserUpdate(BaseModel):
    name: Optional[str] = None
    timezone: Optional[str] = None
    preferred_input: Optional[str] = None
    is_active: Optional[bool] = None


class UserResponse(BaseModel):
    id: int
    name: str
    timezone: str
    preferred_input: str
    is_active: bool
    created_at: Optional[datetime]

    class Config:
        from_attributes = True  # important for SQLAlchemy
