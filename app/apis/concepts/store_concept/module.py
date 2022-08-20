""" Define el modulo de la API SearchTypeOperations """
from .flow import StoreConceptFlow
from .validator import StoreConceptValidator
from libraries.api_manager.module.module_api import ModuleAPI

class StoreConceptModule(ModuleAPI):
    """ Clase que controla los componentes de la API StoreConcept """

    def __init__(self, request, db):
        """ Constructor de la clase """
        super().__init__()
        self.validator_api = StoreConceptValidator(request)
        self.flow_api = StoreConceptFlow(request)
        self.db = db
