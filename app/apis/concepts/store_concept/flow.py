""" Define el flujo del API StoreConcept """
from app.db.models import Concept
from .input import StoreConceptInput
from libraries.api_manager.flow.flow_api import FlowAPI

class StoreConceptFlow(FlowAPI):
    """ Clase que definir el flujo de la API StoreConcept """

    def __init__(self):
        """ Constructor de la clase """
        self.request:StoreConceptInput

    def execute(self):
        """ Función que ejecuta el flujo de la API register """
        concept = Concept(
            name=self.request.name,
        )
        self.db.add(concept)
        self.db.commit()
        return concept.as_dict()
