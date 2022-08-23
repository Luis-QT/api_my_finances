""" Módulo enrutador de APIs """
from fastapi import APIRouter
from app.apis.auth.login.router import \
    router as login_router
from app.apis.auth.register.router import \
    router as register_router
from app.apis.type_operations.search_type_operations.router import \
    router as search_type_operations_router
from app.apis.concepts.search_concepts.router import \
    router as search_concepts_router
from app.apis.concepts.store_concept.router import \
    router as store_concept_router
from app.apis.concepts.update_concept.router import \
    router as update_concept_router
from app.apis.concepts.delete_concept.router import \
    router as delete_concept_router
from app.apis.periods.search_periods.router import \
    router as search_periods_router
from app.apis.periods.store_period.router import \
    router as store_period_router

router = APIRouter()

def route(app):
    """ Enrutar APIs """
    app.include_router(login_router)
    app.include_router(register_router)
    app.include_router(search_type_operations_router)
    app.include_router(search_concepts_router)
    app.include_router(store_concept_router)
    app.include_router(update_concept_router)
    app.include_router(delete_concept_router)
    app.include_router(search_periods_router)
    app.include_router(store_period_router)
