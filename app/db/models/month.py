""" Month model """
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin

class Month(BasePsql, GuidMixin, TimestampMixin):
    """ The months table """
    __tablename__ = 'months'
    number = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    periods = relationship("Period", back_populates="month")
