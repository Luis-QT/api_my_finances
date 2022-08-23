""" Define el modulo de la API SearchConcepts """
from app.apis.concepts.search_concepts.flow import SearchConceptsFlow
from .validator import SearchConceptsValidator
from .response import SearchConceptsResponse
from libraries.api_manager.module.module_api import ModuleAPI

class SearchConceptsModule(ModuleAPI):
    """ Clase que controla los componentes de la API SearchConcepts """

    def __init__(self, request, db):
        """ Constructor de la clase """
        super().__init__()
        self.request = request
        self.validator_api = SearchConceptsValidator()
        self.flow_api = SearchConceptsFlow()
        self.response_api = SearchConceptsResponse()
        self.is_searchable_api = True
        self.db = db
