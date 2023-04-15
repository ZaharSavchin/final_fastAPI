from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from pydantic import BaseModel

from app.db.base_class import Base


class BackCall(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    contacts = Column(Text, nullable=False)
    message = Column(Text, nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow(), nullable=False)


class BackCallCreate(BaseModel):
    contacts: str
    message: str
