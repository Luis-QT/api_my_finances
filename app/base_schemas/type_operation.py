""" TypeOperation Schema """
from uuid import UUID
from pydantic import BaseModel

class TypeOperationBase(BaseModel):
    """ TypeOperation data """
    id: UUID
    name: str
