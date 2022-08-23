""" Define el modulo de la API SearchTypeOperations """
from requests import Session
from .flow import SearchTypeOperationsFlow
from .validator import SearchTypeOperationsValidator
from .input import SearchTypeOperationsInput
from libraries.api_manager.module.module_api import ModuleAPI

class SearchTypeOperationsModule(ModuleAPI):
    """ Clase que controla los componentes de la API SearchTypeOperations """

    def __init__(self, request, db):
        """ Constructor de la clase """
        super().__init__()
        self.request = request
        self.validator_api = SearchTypeOperationsValidator()
        self.flow_api = SearchTypeOperationsFlow()
        self.is_searchable_api = False
        self.db = db
