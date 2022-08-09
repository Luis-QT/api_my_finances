""" Define el modulo de la API SearchTypeOperations """
from requests import Session
from app.apis.type_operations.search_type_operations.flow import SearchTypeOperationsFlow
from app.apis.type_operations.search_type_operations.input import SearchTypeOperationsInput
from app.apis.type_operations.search_type_operations.validator import SearchTypeOperationsValidator
from libraries.classes.module.module_api import ModuleAPI

class SearchTypeOperationsModule(ModuleAPI):
    """ Clase que controla a los componentes de la API SearchTypeOperations """

    def __init__(self, request: SearchTypeOperationsInput, db: Session):
        """ Constructor de la clase """
        super().__init__()
        self.validator_api = SearchTypeOperationsValidator(request)
        self.flow_api = SearchTypeOperationsFlow(request)
        self.db = db
