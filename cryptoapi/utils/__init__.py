from typing import Any, Callable, Dict, Tuple, Union, Optional

api_method_preprocessing_validators_static_type = Dict[int, Dict[str, Any]]
api_method_preprocessing_return_static_type = Tuple[
    Dict[str, str],
    api_method_preprocessing_validators_static_type
]


class CustomValidator:

    def __init__(self, func: Callable, error_text: str) -> None:
        self._func: Callable = func
        self._error_text: str = error_text
        self._errors: Optional[str] = None

    @property
    def errors(self) -> Optional[str]:
        return self._errors

    def validate(self, data: Any) -> bool:
        if not self._func(data):
            self._errors = self._error_text
            return False
        self._errors = None
        return True


class Utils:

    def __init__(self) -> None:
        self.custom_validator = CustomValidator

    @staticmethod
    def api_method_preprocessing(api: Any) -> api_method_preprocessing_return_static_type:
        if not api._api_key:
            raise Exception('API-KEY for this Client is not set')

        validators: api_method_preprocessing_validators_static_type = {
            401: api._validators.error,
            422: api._validators.error,
            500: api._validators.error
        }

        return {
            'token': api._api_key
        }, validators

    @staticmethod
    def validate_data(validator: CustomValidator, data: Any):
        if not validator.validate(data):
            raise Exception(validator.errors)
