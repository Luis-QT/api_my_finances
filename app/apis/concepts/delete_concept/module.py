""" Defines the module of the API DeleteConcept """
from libraries.api_manager.module.module_api import ModuleAPI
from .flow import DeleteConceptFlow
from .validator import DeleteConceptValidator

class DeleteConceptModule(ModuleAPI):
    """ Class that controls the components of the API """

    def __init__(self, request, db):
        """ Constructor of the class """
        super().__init__()
        self.request = request
        self.validator_api = DeleteConceptValidator()
        self.flow_api = DeleteConceptFlow()
        self.is_searchable_api = False
        self.db = db
