""" Módulo enrutador de APIs """
from fastapi import APIRouter
from app.apis.auth.login.router import router as login_router
from app.apis.auth.register.router import router as register_router

API_MODULE = "Auth"
router = APIRouter(prefix="/api/auth")

def route(app):
    """ Enrutar APIs """
    app.include_router(login_router, tags=[API_MODULE])
    app.include_router(register_router, tags=[API_MODULE])
