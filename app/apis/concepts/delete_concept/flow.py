""" Define el flujo del API DeleteConcept """
from .input import DeleteConceptInput
from libraries.api_manager.flow.flow_api import FlowAPI

class DeleteConceptFlow(FlowAPI):
    """ Clase que definir el flujo de la API DeleteConcept """

    def __init__(self):
        """ Constructor de la clase """
        self.request:DeleteConceptInput

    def execute(self):
        """ Función que ejecuta el flujo de la API register """
        concept = self.module_data['concept']
        concept.deleted = True
        self.db.commit()
        return concept.as_dict()
