""" Defines the module of the API StorePeriod """
from libraries.api_manager.module.module_api import ModuleAPI
from .response import StorePeriodResponse
from .flow import StorePeriodFlow
from .validator import StorePeriodValidator

class StorePeriodModule(ModuleAPI):
    """ Class that controls the components of the API """

    def __init__(self, request, db):
        super().__init__()
        self.request = request
        self.validator_api = StorePeriodValidator()
        self.flow_api = StorePeriodFlow()
        self.response_api = StorePeriodResponse()
        self.is_searchable = False
        self.db = db
