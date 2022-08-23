""" Defines the validations of the API SearchConcepts """
from libraries.api_manager.validator.validator_api import ValidatorAPI
from .input import SearchConceptsInput

class SearchConceptsValidator(ValidatorAPI):
    """ Class that validates the input of the API """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:SearchConceptsInput

    def validate_api(self):
        """ Function that ejecutes all the validations """
