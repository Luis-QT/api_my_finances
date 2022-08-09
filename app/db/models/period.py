""" Period model """
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin

class Period(BasePsql, GuidMixin, TimestampMixin):
    """ The periods table """
    __tablename__ = 'periods'
    name = Column(String, nullable=False)
    is_now = Column(Boolean, nullable=False)
    month_id = Column(UUID(as_uuid=True), ForeignKey("months.id"), nullable=False)

    month = relationship("Month", back_populates="periods")
    account_periods = relationship("AccountPeriod", back_populates="period")
