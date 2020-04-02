from cerberus import Validator


class Model:

    def __init__(self, schema, item=False):
        if isinstance(schema, dict):
            schema = Validator(schema)
        self._validator = schema
        self._item = item

    def _validate(self, data):
        if isinstance(self._validator, Validator):
            return self._validator.validate(data)
        return self._validator(data)

    def validate(self, data):
        if self._item:
            return all([self._validate(item) for item in data])
        return self._validate(data)
