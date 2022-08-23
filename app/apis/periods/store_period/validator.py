""" Defines the validations of the API StorePeriod """
from libraries.api_manager.validator.validator_api import ValidatorAPI
from .input import StorePeriodInput

class StorePeriodValidator(ValidatorAPI):
    """ Class that validates the input of the API """

    def __init__(self):
        super().__init__()
        self.request:StorePeriodInput

    def validate_api(self):
        """ Function that ejecutes all the validations """
