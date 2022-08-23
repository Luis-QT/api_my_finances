""" Defines the router funtion of the API UpdateConcept """
from fastapi import APIRouter, Depends, Body
from requests import Session
from app.connections.database import get_db
from libraries.utils.auth_bearer import JWTBearer
from .module import UpdateConceptModule
from .input import (
    UpdateConceptBody,
    UpdateConceptHeader,
    UpdateConceptPath,
    UpdateConceptQuery,
    UpdateConceptInput
)
from .output import UpdateConceptOutput

API_MODULE = "Concept"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.put("/api/concepts/{concept_id}", response_model=UpdateConceptOutput)
def api_router(
    path: UpdateConceptPath = Depends(),
    header: UpdateConceptHeader = Depends(),
    body: UpdateConceptBody = Body(),
    query: UpdateConceptQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    """ Instance and run the API module """
    module =  UpdateConceptModule(UpdateConceptInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **body.dict(),
        **query.dict()
    }), db)
    return module.use_api()
