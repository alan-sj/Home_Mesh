from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str
    default_priority: Optional[str] = "low"
    default_expiry_action: Optional[str] = "drop"
    default_re_remind_interval_mins: Optional[int] = None
    default_pre_reminder_offsets_mins: Optional[List[int]] = None
    is_system: Optional[bool] = False


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    default_priority: Optional[str] = None
    default_expiry_action: Optional[str] = None
    default_re_remind_interval_mins: Optional[int] = None
    default_pre_reminder_offsets_mins: Optional[List[int]] = None
    is_system: Optional[bool] = None


class CategoryResponse(BaseModel):
    id: int
    name: str
    default_priority: str
    default_expiry_action: str
    default_re_remind_interval_mins: Optional[int]
    default_pre_reminder_offsets_mins: Optional[List[int]]
    is_system: bool
    created_at: Optional[datetime]

    class Config:
        from_attributes = True
