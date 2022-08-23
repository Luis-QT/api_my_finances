""" Defines the validations of the API DeleteConcept """
from app.db.models.concept import Concept
from libraries.api_manager.validator.validator_api import ValidatorAPI
from .input import DeleteConceptInput

class DeleteConceptValidator(ValidatorAPI):
    """ Class that validates the input of the API """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:DeleteConceptInput

    def validate_api(self):
        """ Function that ejecutes all the validations """
        self.val_concept_exist()

    def val_concept_exist(self):
        """ Validate if the concept exist """
        concept = self.db.query(Concept).filter(
            Concept.id == self.request.concept_id,
            Concept.deleted == 'false'
        ).first()
        if concept:
            self.validation_exception('concept_id', 'No se encontró el concepto')
        self.module_data['concept'] = concept
