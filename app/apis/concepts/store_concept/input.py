""" Defines the input schema of the API StoreConcept """
from pydantic import BaseModel
from fastapi import Body

class StoreConceptBody(BaseModel):
    """ Body API """
    name: str = Body(..., example="Concepto de prueba")

class StoreConceptQuery(BaseModel):
    """ Query API """

class StoreConceptHeader(BaseModel):
    """ Header API """

class StoreConceptPath(BaseModel):
    """ Path API """

class StoreConceptInput(
    StoreConceptBody,
    StoreConceptQuery,
    StoreConceptHeader,
    StoreConceptPath
):
    """ Input API """
