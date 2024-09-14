from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import List
from typing import Optional
from database import Base
from uuid import UUID, uuid4

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    usage_history = Column(Optional[String])
    is_active = Column(Boolean, default=True)

    usage = relationship("History", back_populates="user")

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    drug = Column(String, index=True)
    dose = Column(String, index=True)
    roa = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    datetime = Column(String, index=True)

    user = relationship("User", back_populates="history")



class Drug(Base):
    __tablename__ = "drugs"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    duration = Column(String, index=True)
    dosages = Column(String)