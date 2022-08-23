""" Define el modulo de la API DeleteConcept """
from .flow import DeleteConceptFlow
from .validator import DeleteConceptValidator
from libraries.api_manager.module.module_api import ModuleAPI

class DeleteConceptModule(ModuleAPI):
    """ Clase que controla los componentes de la API DeleteConcept """

    def __init__(self, request, db):
        """ Constructor de la clase """
        super().__init__()
        self.request = request
        self.validator_api = DeleteConceptValidator()
        self.flow_api = DeleteConceptFlow()
        self.is_searchable_api = False
        self.db = db
