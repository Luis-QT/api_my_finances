""" Define el modulo de la API UpdateConcept """
from .flow import UpdateConceptFlow
from .validator import UpdateConceptValidator
from libraries.api_manager.module.module_api import ModuleAPI

class UpdateConceptModule(ModuleAPI):
    """ Clase que controla los componentes de la API UpdateConcept """

    def __init__(self, request, db):
        """ Constructor de la clase """
        super().__init__()
        self.request = request
        self.validator_api = UpdateConceptValidator()
        self.flow_api = UpdateConceptFlow()
        self.is_searchable_api = False
        self.db = db
