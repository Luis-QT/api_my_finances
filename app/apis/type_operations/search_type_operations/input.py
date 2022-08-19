""" Define las clases de entrada de la API SearchTypeOperations """
from libraries.api_manager.input.input_query_search import InputQuerySearch
from pydantic import BaseModel

class SearchTypeOperationsBody(BaseModel):
    pass

class SearchTypeOperationsQuery(InputQuerySearch):
    pass

class SearchTypeOperationsHeader(BaseModel):
    pass

class SearchTypeOperationsPath(BaseModel):
    pass

class SearchTypeOperationsInput(
    SearchTypeOperationsBody,
    SearchTypeOperationsQuery,
    SearchTypeOperationsHeader,
    SearchTypeOperationsPath
):
    pass
