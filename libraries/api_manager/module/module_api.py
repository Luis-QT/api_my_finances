import math

class ModuleAPI:
    def __init__(self):
        self.request = None
        self.input_api = None
        self.validator_api = None
        self.flow_api = None
        self.response_api = None
        self.module_data = {}
        self.db = None
        self.is_searchable_api = False

    def use_api(self):
        """ Función que ejecuta la API """
        self.validator_api.init_attributes(self.request, self.db, self.module_data)
        self.validator_api.validate()
        self.flow_api.init_attributes(self.request, self.db, self.module_data)
        response_flow = self.flow_api.execute()
        if self.response_api is None:
            return response_flow
        self.response_api.value = response_flow
        response = self.response_api.get_response()
        if self.is_searchable_api:
            return {
                'items': response,
                'total': self.flow_api.total,
                'page': self.request.page,
                'pages': math.ceil(self.flow_api.total / self.request.limit),
                'limit': self.request.limit,
            }
        return response
