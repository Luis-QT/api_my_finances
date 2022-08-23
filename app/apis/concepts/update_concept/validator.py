""" Defines the validations of the API UpdateConcept """
from app.db.models.concept import Concept
from libraries.api_manager.validator.validator_api import ValidatorAPI
from .input import UpdateConceptInput

class UpdateConceptValidator(ValidatorAPI):
    """ Class that validates the input of the API """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:UpdateConceptInput

    def validate_api(self):
        """ Function that ejecutes all the validations """
        self.val_concept_exist()
        self.val_unique_name()

    def val_concept_exist(self):
        """ Validate that the concept exist """
        concept = self.db.query(Concept).filter(
            Concept.id == self.request.concept_id,
            Concept.deleted == 'false'
        ).first()
        if concept:
            self.validation_exception('concept_id', 'No se encontró el concepto')
        self.module_data['concept'] = concept

    def val_unique_name(self):
        """ Validate that the name is unique """
        result = self.db.query(Concept).filter(
            Concept.name.ilike(self.request.name),
            Concept.id != self.request.concept_id
        ).first()
        if result is not None:
            raise self.validation_exception(
                'name', 'El nombre de concepto ya existe'
            )
