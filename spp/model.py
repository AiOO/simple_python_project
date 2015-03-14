from sqlalchemy import func
from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime, Integer, Unicode

from .db import db


__all__ = 'User'


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False, unique=True)
    created_at = Column(DateTime, default=func.now())
