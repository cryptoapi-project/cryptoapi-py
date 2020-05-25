from typing import Any, Dict, List, Union

error_static_type = Dict[str, Union[List[Dict[str, str]], int]]


class Common:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_network_information(self) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        validators.update({200: self._validators.btc.responses.get_network_information})

        return self._http.get(url='{}/network'.format(self._coin_url), params=api_key, validators=validators)

    def get_estimate_fee(self) -> Union[str, error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        validators.update({200: self._validators.btc.responses.get_estimate_fee})

        return self._http.get(url='{}/estimate-fee'.format(self._coin_url), params=api_key, validators=validators)
