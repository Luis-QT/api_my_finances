""" Output Schema """
from typing import List
from app.base_schemas import (
    PageBase, ConceptBase
)

class SearchConceptsOutput(PageBase):
    """ Page TypeOperation data """
    items: List[ConceptBase]
