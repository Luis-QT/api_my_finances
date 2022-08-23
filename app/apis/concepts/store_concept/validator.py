""" Defines the validations of the API StoreConcept """
from app.db.models.concept import Concept
from libraries.api_manager.validator.validator_api import ValidatorAPI
from .input import StoreConceptInput

class StoreConceptValidator(ValidatorAPI):
    """ Class that validates the input of the API """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:StoreConceptInput

    def validate_api(self):
        """ Function that ejecutes all the validations """
        self.val_unique_name()

    def val_unique_name(self):
        """ Validate that the name is unique """
        result = self.db.query(Concept).filter(
            Concept.name.ilike(self.request.name),
        ).first()
        if result is not None:
            raise self.validation_exception(
                'name', 'El nombre de concepto ya existe'
            )
