""" Defines the module of the API SearchConcepts """
from app.apis.concepts.search_concepts.flow import SearchConceptsFlow
from libraries.api_manager.module.module_api import ModuleAPI
from .validator import SearchConceptsValidator
from .response import SearchConceptsResponse

class SearchConceptsModule(ModuleAPI):
    """ Class that controls the components of the API """

    def __init__(self, request, db):
        """ Constructor of the class """
        super().__init__()
        self.request = request
        self.validator_api = SearchConceptsValidator()
        self.flow_api = SearchConceptsFlow()
        self.response_api = SearchConceptsResponse()
        self.is_searchable_api = True
        self.db = db
