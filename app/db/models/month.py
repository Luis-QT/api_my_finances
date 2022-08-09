""" Month model """
from sqlalchemy import Column, String
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin
from sqlalchemy.orm import relationship

class Month(BasePsql, GuidMixin, TimestampMixin):
    """ The months table """
    __tablename__ = 'months'
    name = Column(String, nullable=False)

    periods = relationship("Period", back_populates="month")
