""" Defines the router funtion of the API SearchConcepts """
from fastapi import APIRouter, Depends
from requests import Session
from app.apis.concepts.search_concepts.output import SearchConceptsOutput
from app.connections.database import get_db
from libraries.utils.auth_bearer import JWTBearer
from .module import SearchConceptsModule
from .input import (
    SearchConceptsHeader,
    SearchConceptsPath,
    SearchConceptsQuery,
    SearchConceptsInput
)

API_MODULE = "Concept"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.get("/api/concepts", response_model=SearchConceptsOutput)
def api_router(
    path: SearchConceptsPath = Depends(),
    header: SearchConceptsHeader = Depends(),
    query: SearchConceptsQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    """ Instance and run the API module """
    module =  SearchConceptsModule(SearchConceptsInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **query.dict()
    }), db)
    return module.use_api()
