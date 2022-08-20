""" Módulo enrutador de APIs """
from fastapi import APIRouter, Depends, Body
from requests import Session
from app.connections.database import get_db
from libraries.utils.auth_bearer import JWTBearer
from .module import StoreConceptModule
from .input import StoreConceptBody, StoreConceptHeader, StoreConceptPath, StoreConceptQuery, StoreConceptInput
from .output import StoreConceptOutput

API_MODULE = "Concept"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.post("/api/concepts", response_model=StoreConceptOutput)
def api_store_concept(
    path: StoreConceptPath = Depends(),
    header: StoreConceptHeader = Depends(),
    body: StoreConceptBody = Body(),
    query: StoreConceptQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    module =  StoreConceptModule(StoreConceptInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **body.dict(),
        **query.dict()
    }), db)
    return module.use_api()
