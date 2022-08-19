from pydantic import BaseModel
from fastapi import Path

class UpdateTypeOperationBody(BaseModel):
    name: str

class UpdateTypeOperationQuery(BaseModel):
    pass

class UpdateTypeOperationHeader(BaseModel):
    pass

class UpdateTypeOperationPath(BaseModel):
    type_operation_id: int = Path()

class UpdateTypeOperationInput(
    UpdateTypeOperationBody,
    UpdateTypeOperationQuery,
    UpdateTypeOperationHeader,
    UpdateTypeOperationPath
):
    pass
