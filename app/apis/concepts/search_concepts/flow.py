""" Defines the flow of the API SearchConcepts """
from app.apis.concepts.search_concepts.input import SearchConceptsInput
from app.db.models import Concept
from libraries.utils.paginator import paginate
from libraries.api_manager.flow.flow_api import FlowAPI

class SearchConceptsFlow(FlowAPI):
    """ Class that defines the API flow """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:SearchConceptsInput

    def execute(self):
        """ Function that ejecutes the flow """
        self.search_concepts()
        return self.response

    def search_concepts(self):
        """ Search concepts """
        query = self.db.query(
            Concept
        ).filter(
            Concept.deleted == 'false',
            Concept.name.ilike(f'%{self.request.search}%')
        ).order_by(
            getattr(getattr(Concept, self.request.sort), self.request.order)()
        )
        self.total, self.response = paginate(query, self.request)
