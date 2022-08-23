""" Defines the response of the API SearchPeriods """
from libraries.api_manager.response.response_api import ResponseAPI
from libraries.api_manager.response.model_fields import ModelFields

class SearchPeriodsResponse(ResponseAPI):
    """ Class that defines the API response """

    def set_response(self):
        """ Function that sets the response structure """
        self.set_structure([
            ModelFields()
        ])
