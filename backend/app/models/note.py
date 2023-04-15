from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from app.db.base_class import Base


class Note(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(150), nullable=False)
    text = Column(Text, nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow(), nullable=False)


class NoteCreate(BaseModel):
    title: str
    text: str


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None
