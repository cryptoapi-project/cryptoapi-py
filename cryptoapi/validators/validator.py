from cerberus import Validator as CerberusValidator


class Validator:

    def __init__(self, schema, item=False, custom_validator=object):
        if not isinstance(schema, (dict, custom_validator)):
            raise Exception('Validator schema must be a dict or CustomValidator types object')
        if isinstance(schema, dict):
            schema = CerberusValidator(schema)
        self._validator = schema
        self._item = item

    @property
    def errors(self):
        return self._validator.errors

    def validate(self, data):
        if self._item:
            return all([self._validator.validate(item) for item in data])
        return self._validator.validate(data)
