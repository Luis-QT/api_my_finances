""" Account model """
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin

class Account(BasePsql, GuidMixin, TimestampMixin):
    """ The accounts table """
    __tablename__ = 'accounts'
    name = Column(String, nullable=False)
    deleted = Column(Boolean, default=False)

    account_periods = relationship("AccountPeriod", back_populates="account")
