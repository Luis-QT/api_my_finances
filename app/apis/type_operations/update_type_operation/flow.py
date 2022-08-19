""" Define el flujo del API UpdateTypeOperation """
from .input import UpdateTypeOperationInput
from libraries.api_manager.flow.flow_api import FlowAPI

class UpdateTypeOperationFlow(FlowAPI):
    """ Clase que definir el flujo de la API UpdateTypeOperation """

    def __init__(self, request: UpdateTypeOperationInput):
        """ Constructor de la clase """
        self.request = request

    def execute(self):
        """ Función que ejecuta el flujo de la API register """
        return self.request.type_operation_id
