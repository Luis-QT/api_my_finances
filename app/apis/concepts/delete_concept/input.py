""" Defines the input schema of the API DeleteConcept """
from uuid import UUID
from pydantic import BaseModel
from fastapi import Path

class DeleteConceptBody(BaseModel):
    """ Body API """

class DeleteConceptQuery(BaseModel):
    """ Query API """

class DeleteConceptHeader(BaseModel):
    """ Header API """

class DeleteConceptPath(BaseModel):
    """ Path API """
    concept_id: UUID = Path(..., example="6dff6e3f-cd4a-4ca7-8482-6d31a33b8542")

class DeleteConceptInput(
    DeleteConceptBody,
    DeleteConceptQuery,
    DeleteConceptHeader,
    DeleteConceptPath
):
    """ Input API """
