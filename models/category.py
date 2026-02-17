from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.sql import func
from sqlalchemy import DateTime
from database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    default_priority = Column(String(20), nullable=False, default="low")  # low/medium/high/critical
    default_expiry_action = Column(String(20), nullable=False, default="drop")  # drop/archive/re_remind
    default_re_remind_interval_mins = Column(Integer, nullable=True)
    default_pre_reminder_offsets_mins = Column(JSON, nullable=True)  # e.g. [120, 60, 15]
    is_system = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
