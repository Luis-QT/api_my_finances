""" Módulo enrutador de APIs """
from fastapi import APIRouter, Depends
from requests import Session

from app.apis.type_operations.search_type_operations.output import SearchTypeOperationsOutput
from libraries.utils.auth_bearer import JWTBearer
from .module import SearchTypeOperationsModule
from .input import SearchTypeOperationsHeader, SearchTypeOperationsPath, SearchTypeOperationsQuery, SearchTypeOperationsInput
from app.connections.database import get_db

API_MODULE = "TypeOperation"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.get("/api/type_operations", response_model=SearchTypeOperationsOutput)
def api_search_type_operations(
    path: SearchTypeOperationsPath = Depends(),
    header: SearchTypeOperationsHeader = Depends(),
    query: SearchTypeOperationsQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    module =  SearchTypeOperationsModule(SearchTypeOperationsInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **query.dict()
    }), db)
    return module.use_api()
