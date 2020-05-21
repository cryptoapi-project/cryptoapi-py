from typing import Any, Dict


class Common:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_network_info(self) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        validators.update({200: self._validators.api.klay.responses.get_network_info})

        return self._http.get(url='{}/network'.format(self._coin_url), params=api_key, validators=validators)

    def estimate_gas(self, _from: str, to: str, data: str, value: str) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        data: Dict[str,
                   str] = {
                       'from': _from,
                       'to': to,
                       'data': data,
                       'value': value
                   }

        self._utils.validate_data(self._validators.api.klay.requests.estimate_gas, data)

        validators.update({200: self._validators.api.klay.responses.estimate_gas})

        return self._http.post(
            url='{}/estimate-gas'.format(self._coin_url),
            data=data,
            params=api_key,
            validators=validators
        )
