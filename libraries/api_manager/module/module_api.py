from app.connections.database import get_db
from app.db.base import Session
from fastapi import Depends

class ModuleAPI:
    def __init__(self):
        self.input_api = None
        self.validator_api = None
        self.flow_api = None
        self.module_data = {}
        self.db = None

    def use_api(self):
        """ Función que ejecuta la API """
        self.validator_api.init_attributes(self.db, self.module_data)
        self.validator_api.validate()
        self.flow_api.init_attributes(self.db, self.module_data)
        response = self.flow_api.execute()
        return response
