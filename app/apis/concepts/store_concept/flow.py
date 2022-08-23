""" Defines the flow of the API StoreConcept """
from app.db.models import Concept
from libraries.api_manager.flow.flow_api import FlowAPI
from .input import StoreConceptInput

class StoreConceptFlow(FlowAPI):
    """ Class that defines the API flow """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:StoreConceptInput

    def execute(self):
        """ Function that ejecutes the flow """
        concept = Concept(
            name=self.request.name,
        )
        self.db.add(concept)
        self.db.commit()
        return concept
