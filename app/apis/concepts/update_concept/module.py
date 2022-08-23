""" Defines the module of the API UpdateConcept """
from app.apis.concepts.update_concept.response import UpdateConceptResponse
from libraries.api_manager.module.module_api import ModuleAPI
from .flow import UpdateConceptFlow
from .validator import UpdateConceptValidator

class UpdateConceptModule(ModuleAPI):
    """ Class that controls the components of the API """

    def __init__(self, request, db):
        """ Constructor of the class """
        super().__init__()
        self.request = request
        self.validator_api = UpdateConceptValidator()
        self.flow_api = UpdateConceptFlow()
        self.response_api = UpdateConceptResponse()
        self.is_searchable_api = False
        self.db = db
