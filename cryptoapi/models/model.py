from cerberus import Validator
from cryptoapi.utils.models import CustomValidator


class Model:

    def __init__(self, schema, item=False):
        if not isinstance(schema, (dict, CustomValidator)):
            raise Exception('Validator schema must be a dict or CustomValidator types object')
        if isinstance(schema, dict):
            schema = Validator(schema)
        self._validator = schema
        self._item = item

    @property
    def errors(self):
        return self._validator.errors

    def validate(self, data):
        if self._item:
            return all([self._validator.validate(item) for item in data])
        return self._validator.validate(data)
