""" Defines the validations of the API SearchPeriods """
from libraries.api_manager.validator.validator_api import ValidatorAPI
from .input import SearchPeriodsInput

class SearchPeriodsValidator(ValidatorAPI):
    """ Class that validates the input of the API """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:SearchPeriodsInput

    def validate_api(self):
        """ Function that ejecutes all the validations """
