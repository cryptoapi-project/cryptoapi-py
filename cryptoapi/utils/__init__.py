from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from cerberus import Validator as CerberusValidator  # type: ignore

api_method_preprocessing_validators_static_type = Dict[int, Dict[str, Any]]
api_method_preprocessing_return_static_type = Tuple[Dict[str, str],
                                                    api_method_preprocessing_validators_static_type]


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


class Validator:

    def __init__(self, schema: Union[Dict[Any, Any], Tuple[Callable, str]], item: bool = False) -> None:
        if not isinstance(schema, (dict, tuple)):
            raise Exception('Validator schema must be a dict or tuple(callable, str) types object')
        if isinstance(schema, dict):
            schema = CerberusValidator(schema)

        if isinstance(schema, tuple):
            schema = CustomValidator(*schema)

        self._validator = schema
        self._item = item

    @property
    def errors(self) -> List[str]:
        return self._validator.errors

    def validate(self, data: Any) -> bool:
        if self._item:
            return all([self._validator.validate(item) for item in data])
        return self._validator.validate(data)


class Utils:

    def __init__(self) -> None:
        self.validator = Validator

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
    def validate_data(validator: Union[CustomValidator, Validator], data: Any) -> None:
        if not validator.validate(data):
            raise Exception(validator.errors)
