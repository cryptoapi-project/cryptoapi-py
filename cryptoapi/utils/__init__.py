class CustomValidator:

    def __init__(self, func, error_text):
        self._func = func
        self._error_text = error_text
        self._errors = None

    @property
    def errors(self):
        return self._errors

    def validate(self, data):
        if not self._func(data):
            self._errors = self._error_text
            return False
        self._errors = None
        return True


class Utils:

    def __init__(self):
        self.custom_validator = CustomValidator

    @staticmethod
    def api_method_preprocessing(api):
        if not api._api_key:
            raise Exception('API-KEY for this Client is not set')

        validators = {
            401: api._models.error,
            422: api._models.error
        }

        return {'token': api._api_key}, validators

    @staticmethod
    def validate_data(validator, data):
        if not validator.validate(data):
            raise Exception(validator.errors)
