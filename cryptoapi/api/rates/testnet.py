from typing import Any, Dict, List, Union

error_static_type = Dict[str, Union[List[Dict[str, str]], int]]


class Testnet:

    def __init__(self, http: Any, validators: Any, utils: Any, api_key: str):
        self._http: Any = http
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_coins_rates(self,
                        coins: List[str]) -> Union[List[Dict[str, Union[str, Dict[str, str]]]], error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)
        params: Dict[str, List[str]] = {
            'coins': coins
        }

        self._utils.validate_data(self._validators.rates.requests.get_coins_rates, params)

        validators.update({200: self._validators.rates.responses.get_coins_rates})

        return self._http.get(url='/rates/{}/'.format(','.join(coins)), params=api_key, validators=validators)

    def get_coins_history(
        self, coins: List[str]
    ) -> Union[List[Dict[str, Union[str, List[Dict[str, Union[str, Dict[str, str]]]]]]], error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)
        params: Dict[str, List[str]] = {
            'coins': coins
        }

        self._utils.validate_data(self._validators.rates.requests.get_coins_history, params)

        validators.update({200: self._validators.rates.responses.get_coins_history})

        return self._http.get(
            url='/rates/{}/history'.format(','.join((coins))), params=api_key, validators=validators
        )
