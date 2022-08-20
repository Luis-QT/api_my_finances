from pydantic import BaseModel
from fastapi import Body

class StoreConceptBody(BaseModel):
    name: str = Body(..., example="Concepto de prueba")

class StoreConceptQuery(BaseModel):
    pass

class StoreConceptHeader(BaseModel):
    pass

class StoreConceptPath(BaseModel):
    pass

class StoreConceptInput(
    StoreConceptBody,
    StoreConceptQuery,
    StoreConceptHeader,
    StoreConceptPath
):
    pass
