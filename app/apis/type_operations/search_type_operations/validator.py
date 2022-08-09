""" Define las validaciones de la API SearchTypeOperations """
from app.apis.auth.register.input import RegisterInput
from libraries.classes.validator.validator_api import ValidatorAPI
from libraries.translator.translator import Traslator

class SearchTypeOperationsValidatorData:
    def __init__(self):
        """ Constructor de la clase """
        pass

class SearchTypeOperationsValidator(ValidatorAPI, SearchTypeOperationsValidatorData):
    """ Clase que valida la API SearchTypeOperations """

    def __init__(self, request:RegisterInput):
        """ Constructor de la clase """
        super().__init__()
        self.translator = Traslator(request.language)
        self.request = request
        self.db = None

    def validate(self):
        """ Función que ejecuta las validaciones de la API """
        return SearchTypeOperationsValidatorData()
