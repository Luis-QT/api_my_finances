""" Defines the module of the API StoreConcept """
from app.apis.concepts.store_concept.response import StoreConceptResponse
from libraries.api_manager.module.module_api import ModuleAPI
from .flow import StoreConceptFlow
from .validator import StoreConceptValidator

class StoreConceptModule(ModuleAPI):
    """ Class that controls the components of the API """

    def __init__(self, request, db):
        """ Constructor of the class """
        super().__init__()
        self.request = request
        self.validator_api = StoreConceptValidator()
        self.flow_api = StoreConceptFlow()
        self.response_api = StoreConceptResponse()
        self.is_searchable_api = False
        self.db = db
