""" Defines the router funtion of the API DeleteConcept """
from fastapi import APIRouter, Depends
from requests import Session
from app.connections.database import get_db
from libraries.utils.auth_bearer import JWTBearer
from .module import DeleteConceptModule
from .input import (
    DeleteConceptHeader,
    DeleteConceptPath,
    DeleteConceptQuery,
    DeleteConceptInput
)
from .output import DeleteConceptOutput

API_MODULE = "Concept"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.delete("/api/concepts/{concept_id}", response_model=DeleteConceptOutput)
def api_router(
    path: DeleteConceptPath = Depends(),
    header: DeleteConceptHeader = Depends(),
    query: DeleteConceptQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    """ Instance and run the API module """
    module =  DeleteConceptModule(DeleteConceptInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **query.dict()
    }), db)
    return module.use_api()
