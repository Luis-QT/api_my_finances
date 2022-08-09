""" Concept model """
from sqlalchemy import Column, String
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin
from sqlalchemy.orm import relationship

class Concept(BasePsql, GuidMixin, TimestampMixin):
    """ The concepts table """
    __tablename__ = 'concepts'
    name = Column(String, nullable=False)

    operations = relationship("Operation", back_populates="concept")
