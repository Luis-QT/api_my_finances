""" Output Schema """
from typing import List
from app.base_schemas import (
    TypeOperationBase, PageBase
)

class SearchTypeOperationsOutput(PageBase):
    """ Page TypeOperation data """
    items: List[TypeOperationBase]
