""" Defines the output schema of the API SearchTypeOperations """
from typing import List
from app.base_schemas import (
    TypeOperationBase, PageBase
)

class SearchTypeOperationsOutput(PageBase):
    """ Output API """
    items: List[TypeOperationBase]
