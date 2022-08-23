from libraries.utils.exception import dao_exception

class ValidatorAPI:
    def __init__(self):
        self.request = None
        self.module_data = None
        self.db = None

    def init_attributes(self, request, db, module_data):
        self.request = request
        self.db = db
        self.module_data = module_data

    def validate(self):
        return None

    def validation_exception(self, field, message):
        """ Validation exception """
        return dao_exception(
            400, field, message
        )
