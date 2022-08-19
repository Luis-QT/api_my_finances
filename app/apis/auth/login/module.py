""" Define el modulo de la API Login """
from .flow import LoginFlow
from .validator import LoginValidator
from libraries.api_manager.module.module_api import ModuleAPI

class LoginModule(ModuleAPI):
    """ Clase que controla los componentes de la API Login """

    def __init__(self, request, db):
        """ Constructor de la clase """
        super().__init__()
        self.validator_api = LoginValidator(request)
        self.flow_api = LoginFlow(request)
        self.db = db
