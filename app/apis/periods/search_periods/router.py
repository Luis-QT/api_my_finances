""" Defines the router funtion of the API SearchPeriods """
from fastapi import APIRouter, Depends
from requests import Session
from app.apis.periods.search_periods.output import SearchPeriodsOutput
from app.connections.database import get_db
from libraries.utils.auth_bearer import JWTBearer
from .module import SearchPeriodsModule
from .input import (
    SearchPeriodsHeader,
    SearchPeriodsPath,
    SearchPeriodsQuery,
    SearchPeriodsInput
)

API_MODULE = "Period"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.get("/api/periods", response_model=SearchPeriodsOutput)
def api_router(
    path: SearchPeriodsPath = Depends(),
    header: SearchPeriodsHeader = Depends(),
    query: SearchPeriodsQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    """ Instance and run the API module """
    module =  SearchPeriodsModule(SearchPeriodsInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **query.dict()
    }), db)
    return module.use_api()
