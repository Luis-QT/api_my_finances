""" TypeOperation model """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin

class TypeOperation(BasePsql, GuidMixin, TimestampMixin):
    """ The type_operations table """
    __tablename__ = 'type_operations'
    name = Column(String, nullable=False)

    operations = relationship("Operation", back_populates="type_operation")
