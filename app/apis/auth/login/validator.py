
""" Define las validaciones de la API Login """
from app.apis.auth.login.input import LoginInput
from app.db.models.user import User
from libraries.api_manager.validator.validator_api import ValidatorAPI
from libraries.translator.translator import Traslator
from libraries.utils.crypto import verify_password

class LoginValidator(ValidatorAPI):
    """ Clase que valida la API Login """

    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.request:LoginInput

    def validate(self):
        """ Función que ejecuta las validaciones de la API """
        self.val_email_exist()
        self.val_password()

    def val_email_exist(self):
        """ Validar si existe el usuario """
        self.user = self.db.query(User).filter_by(
            email=self.request.email
        ).first()
        if self.user is None:
            raise self.validation_exception(
                'email', 'The email not found'
            )
        self.module_data['user'] = self.user

    def val_password(self):
        """ Validar si la contraseña es correcta """
        is_valid = verify_password(self.request.password, self.user.password)
        if not is_valid:
            raise self.validation_exception(
                'email', 'The email not found'
            )
