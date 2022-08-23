""" Concept model """
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin

class Concept(BasePsql, GuidMixin, TimestampMixin):
    """ The concepts table """
    __tablename__ = 'concepts'
    name = Column(String, nullable=False)
    deleted = Column(Boolean, default=False)

    operations = relationship("Operation", back_populates="concept")
