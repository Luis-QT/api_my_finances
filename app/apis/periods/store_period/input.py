""" Defines the input schema of the API StorePeriod """
from uuid import UUID
from pydantic import BaseModel
from fastapi import Body

class StorePeriodBody(BaseModel):
    """ Body API """
    name: str = Body(..., description="Nombre del periodo")
    is_now: bool = Body(..., description="¿Es el periodo actual?")
    month_id: UUID = Body(..., description="Id del mes")

class StorePeriodQuery(BaseModel):
    """ Query API """

class StorePeriodHeader(BaseModel):
    """ Header API """

class StorePeriodPath(BaseModel):
    """ Path API """

class StorePeriodInput(
    StorePeriodBody,
    StorePeriodQuery,
    StorePeriodHeader,
    StorePeriodPath
):
    """ Input API """
