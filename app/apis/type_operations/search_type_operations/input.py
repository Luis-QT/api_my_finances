""" Defines the input schema of the API SearchTypeOperations """
from pydantic import BaseModel
from libraries.api_manager.input.input_query_search import InputQuerySearch

class SearchTypeOperationsBody(BaseModel):
    """ Body API """

class SearchTypeOperationsQuery(InputQuerySearch):
    """ Query API """

class SearchTypeOperationsHeader(BaseModel):
    """ Header API """

class SearchTypeOperationsPath(BaseModel):
    """ Path API """

class SearchTypeOperationsInput(
    SearchTypeOperationsBody,
    SearchTypeOperationsQuery,
    SearchTypeOperationsHeader,
    SearchTypeOperationsPath
):
    """ Input API """
