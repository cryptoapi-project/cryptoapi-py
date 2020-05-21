from typing import Any, List, Dict, Union


class Testnet:

    def __init__(self, http: Any, validators: Any, utils: Any, api_key: str, debug: bool) -> None:
        self._http: Any = http
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_coins(self) -> Union[
        List[str],
        Dict[str, Union[List[Dict[str, str]], int]]
    ]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)
        validators.update({200: self._validators.get_coins})

        return self._http.get(url='/coins', params=api_key, validators=validators)
