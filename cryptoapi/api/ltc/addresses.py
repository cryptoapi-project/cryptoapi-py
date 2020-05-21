from typing import Any, Dict, List, Union

error_static_type = Dict[str, Union[List[Dict[str, str]], int]]


class Addresses:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_outputs_by_addresses(self,
                                 addresses: List[str],
                                 status: str,
                                 skip: int = None,
                                 limit: int = None) -> Union[List[Dict[str, Any]], error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[int, str, List[str]]] = {
            'addresses': addresses,
            'status': status
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(self._validators.ltc.requests.get_outputs_by_addresses, params)

        params.update(api_key)

        validators.update({200: self._validators.ltc.responses.get_outputs_by_addresses})

        return self._http.get(
            url='{}/addresses/{}/outputs'.format(self._coin_url, ','.join(params.pop('addresses'))),
            params=params,
            validators=validators
        )

    def get_utxo_coin_addresses_info(self, addresses: List[str]) -> Union[List[Dict[str, Any]], error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, List[str]] = {
            'addresses': addresses
        }

        self._utils.validate_data(self._validators.ltc.requests.get_utxo_coin_addresses_info, params)

        validators.update({200: self._validators.ltc.responses.get_utxo_coin_addresses_info})

        return self._http.get(
            url='{}/addresses/{}'.format(self._coin_url, ','.join(params.pop('addresses'))),
            params=api_key,
            validators=validators
        )

    def get_utxo_coin_addresses_history(self,
                                        addresses: List[str],
                                        skip: int = None,
                                        limit: int = None) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[List[str], int]] = {
            'addresses': addresses
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(self._validators.ltc.requests.get_utxo_coin_addresses_history, params)

        params.update(api_key)

        validators.update({200: self._validators.ltc.responses.get_utxo_coin_addresses_history})

        return self._http.get(
            url='{}/addresses/{}/transactions'.format(self._coin_url, ','.join(params.pop('addresses'))),
            params=params,
            validators=validators
        )
