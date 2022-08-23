""" Defines the input schema of the API SearchPeriods """
from pydantic import BaseModel
from libraries.api_manager.input.input_query_search import InputQuerySearch

class SearchPeriodsBody(BaseModel):
    """ Body API """

class SearchPeriodsQuery(InputQuerySearch):
    """ Query API """

class SearchPeriodsHeader(BaseModel):
    """ Header API """

class SearchPeriodsPath(BaseModel):
    """ Path API """

class SearchPeriodsInput(
    SearchPeriodsBody,
    SearchPeriodsQuery,
    SearchPeriodsHeader,
    SearchPeriodsPath
):
    """ Input API """
