""" Defines the flow of the API UpdateConcept """
from libraries.api_manager.flow.flow_api import FlowAPI
from .input import UpdateConceptInput

class UpdateConceptFlow(FlowAPI):
    """ Class that defines the API flow """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:UpdateConceptInput

    def execute(self):
        """ Function that ejecutes the flow """
        concept = self.module_data['concept']
        concept.name = self.request.name
        self.db.commit()
        return concept
