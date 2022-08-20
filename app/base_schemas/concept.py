""" Concept Schema """
from uuid import UUID
from pydantic import BaseModel

class ConceptBase(BaseModel):
    """ Concept data """
    id: UUID
    name: str
    deleted: bool
