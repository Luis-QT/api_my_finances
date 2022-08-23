""" Define el flujo del API Register """
from app.apis.auth.register.input import RegisterInput
from app.db.models.user import User
from libraries.utils.crypto import hash_password
from libraries.utils.avatar import generate_avatar_url
from app.apis.auth.register.input import RegisterInput
from libraries.api_manager.flow.flow_api import FlowAPI

class RegisterFlow(FlowAPI):
    """ Clase que definir el flujo de la API Register """

    def __init__(self):
        """ Constructor de la clase """
        self.request:RegisterInput

    def execute(self):
        """ Función que ejecuta el flujo de la API Register """
        self.register_user()
        self.db.commit()
        return self.user.as_dict()

    def register_user(self):
        """ Registrar usuario """
        self.user = User(
            email=self.request.email,
            name=self.request.name,
            password=hash_password(self.request.password),
            avatar_url=generate_avatar_url(self.request.email)
        )
        self.db.add(self.user)
        self.db.flush()
