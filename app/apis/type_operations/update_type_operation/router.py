""" Módulo enrutador de APIs """
from fastapi import APIRouter, Depends, Body
from requests import Session
from app.apis.type_operations.update_type_operation.output import UpdateTypeOperationOutput

from app.connections.database import get_db
from libraries.utils.auth_bearer import JWTBearer
from .module import UpdateTypeOperationModule
from .input import UpdateTypeOperationBody, UpdateTypeOperationHeader, UpdateTypeOperationPath, UpdateTypeOperationQuery, UpdateTypeOperationInput

API_MODULE = "TypeOperation"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.put("/api/type_operations/{type_operation_id}", response_model=UpdateTypeOperationOutput)
def api_update_type_operation(
    path: UpdateTypeOperationPath = Depends(),
    header: UpdateTypeOperationHeader = Depends(),
    body: UpdateTypeOperationBody = Body(),
    query: UpdateTypeOperationQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    module =  UpdateTypeOperationModule(UpdateTypeOperationInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **body.dict(),
        **query.dict()
    }), db)
    return module.use_api()
