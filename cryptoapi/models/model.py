from cerberus import Validator


class Model:

    def __init__(self, schema):
        self.validator = Validator(schema)

    def validate(self, data):
        return self.validator.validate(data)
