""" Defines the router funtion of the API StorePeriod """
from fastapi import APIRouter, Depends, Body
from requests import Session
from app.connections.database import get_db
from libraries.utils.auth_bearer import JWTBearer
from .module import StorePeriodModule
from .input import (
    StorePeriodBody,
    StorePeriodHeader,
    StorePeriodPath,
    StorePeriodQuery,
    StorePeriodInput
)
from .output import StorePeriodOutput

API_MODULE = "Period"
router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])

@router.post("api/periods", response_model=StorePeriodOutput)
def api_store_period(
    path: StorePeriodPath = Depends(),
    header: StorePeriodHeader = Depends(),
    query: StorePeriodQuery = Depends(),
    body: StorePeriodBody = Body(),
    db: Session = Depends(get_db)
    ):
    """ Instance and run the API module """

    module = StorePeriodModule(StorePeriodInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **body.dict(),
        **query.dict()
    }), db)
    return module.use_api()
