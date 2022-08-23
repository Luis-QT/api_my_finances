""" Defines the flow of the API StorePeriod """
from libraries.api_manager.flow.flow_api import FlowAPI
from .input import StorePeriodInput

class StorePeriodFlow(FlowAPI):
    """ Class that defines the API flow """

    def __init__(self):
        super().__init__()
        self.request:StorePeriodInput

    def execute(self):
        """ Function that ejecutes the flow """
        return dict()
