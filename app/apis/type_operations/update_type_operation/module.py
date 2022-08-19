""" Define el modulo de la API SearchTypeOperations """
from requests import Session
from .flow import UpdateTypeOperationFlow
from .validator import UpdateTypeOperationValidator
from libraries.api_manager.module.module_api import ModuleAPI

class UpdateTypeOperationModule(ModuleAPI):
    """ Clase que controla los componentes de la API UpdateTypeOperation """

    def __init__(self, request, db):
        """ Constructor de la clase """
        super().__init__()
        self.validator_api = UpdateTypeOperationValidator(request)
        self.flow_api = UpdateTypeOperationFlow(request)
        self.db = db
