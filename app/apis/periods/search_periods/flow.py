""" Defines the flow of the API SearchPeriods """
from app.apis.periods.search_periods.input import SearchPeriodsInput
from app.db.models import Period
from libraries.utils.paginator import paginate
from libraries.api_manager.flow.flow_api import FlowAPI

class SearchPeriodsFlow(FlowAPI):
    """ Class that defines the API flow """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:SearchPeriodsInput

    def execute(self):
        """ Function that ejecutes the flow """
        self.search_periods()
        return self.response

    def search_periods(self):
        """ Search periods """
        query = self.db.query(
            Period
        ).order_by(
            getattr(getattr(Period, self.request.sort), self.request.order)()
        )
        self.total, self.response = paginate(query, self.request)
