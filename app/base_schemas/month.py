""" Month Schema """
from uuid import UUID
from pydantic import BaseModel

class MonthBase(BaseModel):
    """ Month data """
    id: UUID
    name: str
