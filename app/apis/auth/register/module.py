""" Define el modulo de la API Register """
from requests import Session
from .flow import RegisterFlow
from .validator import RegisterValidator
from .input import RegisterInput
from libraries.api_manager.module.module_api import ModuleAPI

class RegisterModule(ModuleAPI):
    """ Clase que controla los componentes de la API Register """

    def __init__(self, request, db):
        """ Constructor de la clase """
        super().__init__()
        self.validator_api = RegisterValidator(request)
        self.flow_api = RegisterFlow(request)
        self.db = db
