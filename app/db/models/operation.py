""" Operation model """
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Float, Date, String, Integer
from sqlalchemy.orm import relationship
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin

class Operation(BasePsql, GuidMixin, TimestampMixin):
    """ The operations table """
    __tablename__ = 'operations'
    date = Column(Date, nullable=False)
    order_day = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Float(precision=2), nullable=False)
    account_period_id = Column(UUID(as_uuid=True), ForeignKey("account_periods.id"), nullable=False)
    concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id"), nullable=True)
    type_operation_id = Column(UUID(as_uuid=True), ForeignKey("type_operations.id"), nullable=False)

    account_period = relationship("AccountPeriod", back_populates="operations")
    concept = relationship("Concept", back_populates="operations")
    type_operation = relationship("TypeOperation", back_populates="operations")
