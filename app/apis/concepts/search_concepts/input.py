""" Defines the input schema of the API SearchConcepts """
from pydantic import BaseModel
from libraries.api_manager.input.input_query_search import InputQuerySearch

class SearchConceptsBody(BaseModel):
    """ Body API """

class SearchConceptsQuery(InputQuerySearch):
    """ Query API """

class SearchConceptsHeader(BaseModel):
    """ Header API """

class SearchConceptsPath(BaseModel):
    """ Path API """

class SearchConceptsInput(
    SearchConceptsBody,
    SearchConceptsQuery,
    SearchConceptsHeader,
    SearchConceptsPath
):
    """ Input API """
