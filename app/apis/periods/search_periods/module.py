""" Defines the module of the API SearchPeriods """
from app.apis.periods.search_periods.response import SearchPeriodsResponse
from libraries.api_manager.module.module_api import ModuleAPI
from .flow import SearchPeriodsFlow
from .validator import SearchPeriodsValidator

class SearchPeriodsModule(ModuleAPI):
    """ Class that controls the components of the API """

    def __init__(self, request, db):
        """ Constructor of the class """
        super().__init__()
        self.request = request
        self.validator_api = SearchPeriodsValidator()
        self.flow_api = SearchPeriodsFlow()
        self.response_api = SearchPeriodsResponse()
        self.is_searchable_api = True
        self.db = db
