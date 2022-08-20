""" Define las clases de entrada de la API SearchConcepts """
from libraries.api_manager.input.input_query_search import InputQuerySearch
from pydantic import BaseModel

class SearchConceptsBody(BaseModel):
    pass

class SearchConceptsQuery(InputQuerySearch):
    pass

class SearchConceptsHeader(BaseModel):
    pass

class SearchConceptsPath(BaseModel):
    pass

class SearchConceptsInput(
    SearchConceptsBody,
    SearchConceptsQuery,
    SearchConceptsHeader,
    SearchConceptsPath
):
    pass
