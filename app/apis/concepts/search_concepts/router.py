""" Módulo enrutador de APIs """
from fastapi import APIRouter, Depends
from requests import Session
from app.apis.concepts.search_concepts.output import SearchConceptsOutput
from libraries.utils.auth_bearer import JWTBearer
from .module import SearchConceptsModule
from .input import SearchConceptsHeader, SearchConceptsPath, SearchConceptsQuery, SearchConceptsInput
from app.connections.database import get_db

API_MODULE = "Concept"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.get("/api/concepts", response_model=SearchConceptsOutput)
def api_search_type_operations(
    path: SearchConceptsPath = Depends(),
    header: SearchConceptsHeader = Depends(),
    query: SearchConceptsQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    module =  SearchConceptsModule(SearchConceptsInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **query.dict()
    }), db)
    return module.use_api()
