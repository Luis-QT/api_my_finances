""" Módulo enrutador de APIs """
from fastapi import APIRouter, Depends, Body
from requests import Session
from app.connections.database import get_db
from libraries.utils.auth_bearer import JWTBearer
from .module import DeleteConceptModule
from .input import DeleteConceptBody, DeleteConceptHeader, DeleteConceptPath, DeleteConceptQuery, DeleteConceptInput
from .output import DeleteConceptOutput

API_MODULE = "Concept"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.delete("/api/concepts/{concept_id}", response_model=DeleteConceptOutput)
def api_update_concept(
    path: DeleteConceptPath = Depends(),
    header: DeleteConceptHeader = Depends(),
    query: DeleteConceptQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    module =  DeleteConceptModule(DeleteConceptInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **query.dict()
    }), db)
    return module.use_api()
