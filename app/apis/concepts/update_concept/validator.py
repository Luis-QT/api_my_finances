""" Define las validaciones de la API UpdateConcept """
from app.db.models.concept import Concept
from .input import UpdateConceptInput
from libraries.api_manager.validator.validator_api import ValidatorAPI

class UpdateConceptValidator(ValidatorAPI):
    """ Clase que valida la API UpdateConcept """

    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.request:UpdateConceptInput

    def validate(self):
        """ Función que ejecuta las validaciones de la API """
        self.val_concept_exist()
        self.val_unique_name()
    
    def val_concept_exist(self):
        """ Validar si existe el concepto """
        concept = self.db.query(Concept).filter(
            Concept.id == self.request.concept_id,
            Concept.deleted == 'false'
        ).first()
        if concept:
            self.validation_exception('concept_id', 'No se encontró el concepto')
        self.module_data['concept'] = concept

    def val_unique_name(self):
        """ Validar que el nombre sea único """
        result = self.db.query(Concept).filter(
            Concept.name.ilike(self.request.name),
            Concept.id != self.request.concept_id
        ).first()
        if result is not None:
            raise self.validation_exception(
                'name', 'El nombre de concepto ya existe'
            )
