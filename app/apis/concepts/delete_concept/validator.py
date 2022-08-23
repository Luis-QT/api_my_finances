""" Define las validaciones de la API DeleteConcept """
from app.db.models.concept import Concept
from .input import DeleteConceptInput
from libraries.api_manager.validator.validator_api import ValidatorAPI

class DeleteConceptValidator(ValidatorAPI):
    """ Clase que valida la API DeleteConcept """

    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.request:DeleteConceptInput

    def validate(self):
        """ Función que ejecuta las validaciones de la API """
        self.val_concept_exist()
    
    def val_concept_exist(self):
        """ Validar si existe el concepto """
        concept = self.db.query(Concept).filter(
            Concept.id == self.request.concept_id,
            Concept.deleted == 'false'
        ).first()
        if concept:
            self.validation_exception('concept_id', 'No se encontró el concepto')
        self.module_data['concept'] = concept
