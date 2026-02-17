from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__='users'

    id= Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    timezone = Column(String(100), nullable=False)
    preferred_input = Column(String(20), nullable=False)  # text / voice
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    