""" Period Schema """
from uuid import UUID
from pydantic import BaseModel

class PeriodBase(BaseModel):
    """ Period data """
    id: UUID
    year: int
    month_id: int
    is_now: bool
