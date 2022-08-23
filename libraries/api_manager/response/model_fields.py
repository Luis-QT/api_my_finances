from libraries.api_manager.response.handler_response import HandlerResponse
from libraries.api_manager.response.response_field import ResponseField

class ModelFields(ResponseField):
	'''Parent class for model field'''
	def __init__(self):
		self.registry = None

	def get_field(self):
		return self.registry.as_dict()
