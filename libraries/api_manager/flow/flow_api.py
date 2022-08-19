
class FlowAPI:
    def __init__(self):
        self.request = None
        self.module_data = None
        self.db = None

    def init_attributes(self, db, module_data):
        self.db = db
        self.module_data = module_data

    def execute(self):
        return None
