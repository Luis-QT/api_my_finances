""" Account model """
from sqlalchemy import Column, String
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin
from sqlalchemy.orm import relationship

class Account(BasePsql, GuidMixin, TimestampMixin):
    """ The accounts table """
    __tablename__ = 'accounts'
    name = Column(String, nullable=False)

    account_periods = relationship("AccountPeriod", back_populates="account")
