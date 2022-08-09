""" AccountPeriod model """
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin

class AccountPeriod(BasePsql, GuidMixin, TimestampMixin):
    """ The account_periods table """
    __tablename__ = 'account_periods'
    amount_start = Column(Float(precision=2), nullable=False)
    amount_end = Column(Float(precision=2), nullable=False)
    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False)
    period_id = Column(UUID(as_uuid=True), ForeignKey("periods.id"), nullable=False)

    account = relationship("Account", back_populates="account_periods")
    period = relationship("Period", back_populates="account_periods")
    operations = relationship("Operation", back_populates="account_period")
