""" Define el flujo del API UpdateConcept """
from app.db.models import Concept
from .input import UpdateConceptInput
from libraries.api_manager.flow.flow_api import FlowAPI

class UpdateConceptFlow(FlowAPI):
    """ Clase que definir el flujo de la API UpdateConcept """

    def __init__(self):
        """ Constructor de la clase """
        self.request:UpdateConceptInput

    def execute(self):
        """ Función que ejecuta el flujo de la API register """
        concept = self.module_data['concept']
        concept.name = self.request.name
        self.db.commit()
        return concept.as_dict()
