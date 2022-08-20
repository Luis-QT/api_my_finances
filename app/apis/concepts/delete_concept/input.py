from uuid import UUID
from pydantic import BaseModel
from fastapi import Path

class DeleteConceptBody(BaseModel):
    pass

class DeleteConceptQuery(BaseModel):
    pass

class DeleteConceptHeader(BaseModel):
    pass

class DeleteConceptPath(BaseModel):
    concept_id: UUID = Path(..., example="6dff6e3f-cd4a-4ca7-8482-6d31a33b8542")

class DeleteConceptInput(
    DeleteConceptBody,
    DeleteConceptQuery,
    DeleteConceptHeader,
    DeleteConceptPath
):
    pass
