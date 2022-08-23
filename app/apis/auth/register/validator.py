""" Define las validaciones de la API Register """
from app.apis.auth.register.input import RegisterInput
from libraries.api_manager.validator.validator_api import ValidatorAPI

class RegisterValidator(ValidatorAPI):
    """ Clase que valida la API Register """

    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.request:RegisterInput

    def validate(self):
        """ Función que ejecuta las validaciones de la API """
        pass
