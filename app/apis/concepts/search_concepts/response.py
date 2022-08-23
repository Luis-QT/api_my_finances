""" Define la respuesta del API SearchConcepts """
from libraries.api_manager.response.response_api import ResponseAPI
from libraries.api_manager.response.model_fields import ModelFields

class SearchConceptsResponse(ResponseAPI):
    """ Clase para definir la salida del API SearchConcepts """
    def __init__(self):
        """ Constructor de la clase """
        super().__init__()

    def set_response(self):
        """ Función que define la salida del API """
        self.set_structure([
            ModelFields()
        ])
