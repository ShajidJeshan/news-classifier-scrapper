from sqlalchemy import Column, Integer, String, DateTime, text
from .database import Base


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(String)
    title = Column(String, nullable=False)
    post = Column(String, nullable=False)
    category = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=text('now()'), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=text('now()'), onupdate=text('now()'), nullable=False)