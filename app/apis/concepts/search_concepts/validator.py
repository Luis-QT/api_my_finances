""" Define las validaciones de la API SearchConcepts """
from .input import SearchConceptsInput
from libraries.api_manager.validator.validator_api import ValidatorAPI

class SearchConceptsValidator(ValidatorAPI):
    """ Clase que valida la API UpdateTypeOperation """

    def __init__(self, request: SearchConceptsInput):
        """ Constructor de la clase """
        super().__init__()
        self.request = request

    def validate(self):
        """ Función que ejecuta las validaciones de la API SearchConcepts"""
        pass
