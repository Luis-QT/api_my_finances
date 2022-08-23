""" Defines the validations of the API SearchTypeOperations """
from libraries.api_manager.validator.validator_api import ValidatorAPI
from .input import SearchTypeOperationsInput

class SearchTypeOperationsValidator(ValidatorAPI):
    """ Class that validates the input of the API """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:SearchTypeOperationsInput

    def validate_api(self):
        """ Function that ejecutes all the validations """
