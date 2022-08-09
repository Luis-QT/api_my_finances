""" Define las clases de entrada de la API register """
from fastapi import Depends
from libraries.classes.input.input_api import InputAPI, input_api
from libraries.classes.input.input_search import InputSearch, input_search
from libraries.classes.input.input_jwt import InputJWT, input_jwt


class SearchTypeOperationsInput(InputAPI, InputSearch):
    pass

def search_type_operations_input(
    input_api: InputAPI = Depends(input_api),
    input_search: InputSearch = Depends(input_search),
    input_jwt: InputJWT = Depends(input_jwt),
    ):
    return SearchTypeOperationsInput.parse_obj({
        **input_api.dict(),
        **input_search.dict(),
        **input_jwt.dict()
    })
