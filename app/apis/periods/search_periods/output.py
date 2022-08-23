""" Defines the output schema of the API SearchPeriods """
from typing import List
from app.base_schemas import PageBase
from app.base_schemas.period import PeriodBase

class SearchPeriodsOutput(PageBase):
    """ Output API """
    items: List[PeriodBase]
