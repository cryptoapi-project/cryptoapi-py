from typing import Any, Dict, List, Union

from .validators import Validators


class Testnet:

    def __init__(self, http: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._api_key: str = api_key
        self._utils: Any = utils
        self._validators: Validators = Validators(self._utils)

    def get_coins(self) -> Union[List[str], Dict[str, Union[List[Dict[str, str]], int]]]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)
        validators.update({200: self._validators.get_coins})

        return self._http.get(url='/coins', params=api_key, validators=validators)
