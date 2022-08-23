""" Defines the module of the API SearchTypeOperations """
from app.apis.type_operations.search_type_operations.response import SearchTypeOperationsResponse
from libraries.api_manager.module.module_api import ModuleAPI
from .flow import SearchTypeOperationsFlow
from .validator import SearchTypeOperationsValidator

class SearchTypeOperationsModule(ModuleAPI):
    """ Class that controls the components of the API """

    def __init__(self, request, db):
        """ Constructor of the class """
        super().__init__()
        self.request = request
        self.validator_api = SearchTypeOperationsValidator()
        self.flow_api = SearchTypeOperationsFlow()
        self.response_api = SearchTypeOperationsResponse()
        self.is_searchable_api = True
        self.db = db
