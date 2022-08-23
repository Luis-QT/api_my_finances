""" Defines the flow of the API SearchTypeOperations """
from app.apis.type_operations.search_type_operations.input import SearchTypeOperationsInput
from app.db.models import TypeOperation
from libraries.utils.paginator import paginate
from libraries.api_manager.flow.flow_api import FlowAPI

class SearchTypeOperationsFlow(FlowAPI):
    """ Class that defines the API flow """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:SearchTypeOperationsInput

    def execute(self):
        """ Function that ejecutes the flow """
        self.search_type_operations()
        return self.response

    def search_type_operations(self):
        """ Search type operations """
        query = self.db.query(
            TypeOperation
        ).order_by(
            getattr(getattr(TypeOperation, self.request.sort), self.request.order)()
        )
        self.total, self.response = paginate(query, self.request)
