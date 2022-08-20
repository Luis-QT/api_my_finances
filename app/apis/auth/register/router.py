""" Módulo enrutador de APIs """
from fastapi import APIRouter, Depends, Body
from app.base_schemas import UserBase
from app.connections.database import get_db
from app.db.base import Session
from .module import RegisterModule
from .input import RegisterBody, RegisterHeader, RegisterPath, RegisterQuery, RegisterInput

API_MODULE = "Auth"
router = APIRouter(tags=[API_MODULE])

@router.post("/apis/auth/register", response_model=UserBase)
def api_register(
    path: RegisterPath = Depends(),
    header: RegisterHeader = Depends(),
    body: RegisterBody = Body(),
    query: RegisterQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    module =  RegisterModule(RegisterInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **body.dict(),
        **query.dict()
    }), db)
    return module.use_api()
