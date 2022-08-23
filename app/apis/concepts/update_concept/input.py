""" Defines the input schema of the API UpdateConcept """
from uuid import UUID
from pydantic import BaseModel
from fastapi import Body, Path

class UpdateConceptBody(BaseModel):
    """ Body API """
    name: str = Body(..., example="Concepto de prueba")

class UpdateConceptQuery(BaseModel):
    """ Query API """

class UpdateConceptHeader(BaseModel):
    """ Header API """

class UpdateConceptPath(BaseModel):
    """ Path API """
    concept_id: UUID = Path(..., example="6dff6e3f-cd4a-4ca7-8482-6d31a33b8542")

class UpdateConceptInput(
    UpdateConceptBody,
    UpdateConceptQuery,
    UpdateConceptHeader,
    UpdateConceptPath
):
    """ Input API """
