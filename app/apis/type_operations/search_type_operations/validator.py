""" Define las validaciones de la API SearchTypeOperations """
from .input import SearchTypeOperationsInput
from libraries.api_manager.validator.validator_api import ValidatorAPI

class SearchTypeOperationsValidator(ValidatorAPI):
    """ Clase que valida la API UpdateTypeOperation """

    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.request:SearchTypeOperationsInput

    def validate(self):
        """ Función que ejecuta las validaciones de la API SearchTypeOperations"""
        pass
