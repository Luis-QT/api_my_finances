""" Define las validaciones de la API UpdateTypeOperation """
from .input import UpdateTypeOperationInput
from libraries.api_manager.validator.validator_api import ValidatorAPI

class UpdateTypeOperationValidator(ValidatorAPI):
    """ Clase que valida la API UpdateTypeOperation """

    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.request:UpdateTypeOperationInput

    def validate(self):
        """ Función que ejecuta las validaciones de la API """
        pass
