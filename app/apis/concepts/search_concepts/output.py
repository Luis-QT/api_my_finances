""" Defines the output schema of the API SearchConcepts """
from typing import List
from app.base_schemas import (
    PageBase, ConceptBase
)

class SearchConceptsOutput(PageBase):
    """ Output API """
    items: List[ConceptBase]
