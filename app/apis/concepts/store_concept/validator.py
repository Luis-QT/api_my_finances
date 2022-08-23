""" Define las validaciones de la API StoreConcept """
from app.db.models.concept import Concept
from .input import StoreConceptInput
from libraries.api_manager.validator.validator_api import ValidatorAPI

class StoreConceptValidator(ValidatorAPI):
    """ Clase que valida la API StoreConcept """

    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.request:StoreConceptInput

    def validate(self):
        """ Función que ejecuta las validaciones de la API """
        self.val_unique_name()


    def val_unique_name(self):
        """ Validar que el nombre sea único """
        result = self.db.query(Concept).filter(
            Concept.name.ilike(self.request.name),
        ).first()
        if result is not None:
            raise self.validation_exception(
                'name', 'El nombre de concepto ya existe'
            )
