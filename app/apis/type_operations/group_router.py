""" Módulo enrutador de APIs """
from fastapi import APIRouter
from app.apis.type_operations.search_type_operations.router import router as search_type_operations_router
from app.apis.type_operations.update_type_operation.router import router as update_type_operation_router

API_MODULE = "TypeOperation"
router = APIRouter()

def route(app):
    """ Enrutar APIs """
    app.include_router(update_type_operation_router, tags=[API_MODULE])
    app.include_router(search_type_operations_router, tags=[API_MODULE])
