""" Módulo enrutador de APIs """
from fastapi import APIRouter, Depends
from requests import Session
from app.apis.type_operations.search_type_operations.input import SearchTypeOperationsInput, search_type_operations_input
from app.apis.type_operations.search_type_operations.module import SearchTypeOperationsModule
from app.apis.type_operations.search_type_operations.output import SearchTypeOperationsOutput
from app.connections.database import get_db
from app.main import app

API_MODULE = "TypeOperation"
router = APIRouter(prefix="/api/type_operations")

@router.get("/", response_model=SearchTypeOperationsOutput)
def api_search_type_operations(
    request: SearchTypeOperationsInput = Depends(search_type_operations_input),
    db: Session = Depends(get_db)
    ):
    module =  SearchTypeOperationsModule(request, db)
    return module.use_api()


def route(app):
    """ Enrutar APIs """
    app.include_router(router, tags=[API_MODULE])
