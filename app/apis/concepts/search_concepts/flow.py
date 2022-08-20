""" Define el flujo del API SearchConcepts """
import math
from app.apis.concepts.search_concepts.input import SearchConceptsInput
from app.db.models import Concept
from libraries.utils.paginator import paginate
from libraries.api_manager.flow.flow_api import FlowAPI

class SearchConceptsFlow(FlowAPI):
    """ Clase que definir el flujo de la API SearchConcepts """

    def __init__(self, request: SearchConceptsInput):
        """ Constructor de la clase """
        self.request = request

    def execute(self):
        """ Función que ejecuta el flujo de la API SearchConcepts """
        self.search_concepts()
        self.prepare_response()
        return {
            'items': self.array_response,
            'total': self.total,
            'page': self.request.page,
            'pages': math.ceil(self.total / self.request.limit),
            'limit': self.request.limit
        }

    def search_concepts(self):
        """ Buscar conceptos """
        query = self.db.query(
            Concept
        ).filter(
            Concept.deleted == 'false',
            Concept.name.ilike(f'%{self.request.search}%')
        ).order_by(
            getattr(getattr(Concept, self.request.sort), self.request.order)()
        )
        self.total, self.results = paginate(query, self.request)

    def prepare_response(self):
        """ Preparar respuesta """
        self.array_response = []
        for type_operation in self.results:
            response = {
                **type_operation.as_dict(),
            }
            self.array_response.append(response)
