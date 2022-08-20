""" User model """
from sqlalchemy import Column, String, Text, Boolean
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin

class User(BasePsql, GuidMixin, TimestampMixin):
    """ The users table """
    __tablename__ = 'users'
    name = Column(String, nullable=False)
    password = Column(String, nullable=True)
    email = Column(String, nullable=False)
    avatar_url = Column(Text, nullable=False)
    deleted = Column(Boolean, default=False)
