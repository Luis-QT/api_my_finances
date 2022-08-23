""" Defines the flow of the API DeleteConcept """
from libraries.api_manager.flow.flow_api import FlowAPI
from .input import DeleteConceptInput

class DeleteConceptFlow(FlowAPI):
    """ Class that defines the API flow """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:DeleteConceptInput

    def execute(self):
        """ Function that ejecutes the flow """
        concept = self.module_data['concept']
        concept.deleted = True
        self.db.commit()
        return concept
