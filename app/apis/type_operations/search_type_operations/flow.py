""" Define el flujo del API SearchTypeOperations """
import math
from app.apis.type_operations.search_type_operations.input import SearchTypeOperationsInput
from app.apis.type_operations.search_type_operations.validator import SearchTypeOperationsValidatorData
from app.db.models import TypeOperation
from libraries.utils.paginator import paginate

class SearchTypeOperationsFlow:
    """ Clase que definir el flujo de la API SearchTypeOperations """

    def __init__(self, request: SearchTypeOperationsInput):
        """ Constructor de la clase """
        self.data: SearchTypeOperationsValidatorData
        self.request = request
        self.db = None

    def execute(self):
        """ Función que ejecuta el flujo de la API register """
        self.search_type_operations()
        self.prepare_response()
        return {
            'items': self.array_response,
            'total': self.total,
            'page': self.request.page,
            'pages': math.ceil(self.total / self.request.limit),
            'limit': self.request.limit
        }

    def search_type_operations(self):
        """ Buscar tipos de operaciones """
        query = self.db.query(
            TypeOperation
        ).order_by(
            getattr(getattr(TypeOperation, self.request.sort), self.request.order)()
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
