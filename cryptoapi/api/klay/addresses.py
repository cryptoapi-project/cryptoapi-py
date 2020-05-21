from typing import Any, Dict, List, Optional, Union

error_static_type = Dict[str, Union[List[Dict[str, str]], int]]


class Addresses:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_transactions_by_addresses(
        self,
        addresses: List[str],
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        positive: Optional[str] = None
    ) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[int, str, List[str]]] = {
            'addresses': addresses
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if positive is not None:
            params.update({'positive': positive})

        self._utils.validate_data(self._validators.klay.requests.get_transactions_by_addresses, params)

        params.update(api_key)

        validators.update({200: self._validators.klay.responses.get_transactions_by_addresses})

        return self._http.get(
            url='{}/addresses/{}/transfers'.format(self._coin_url, ','.join(params.pop('addresses'))),
            params=params,
            validators=validators
        )

    def get_transaction_intersections_by_addresses(
        self, addresses: List[str], skip: Optional[int] = None, limit: Optional[int] = None
    ) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[int, str, List[str]]] = {
            'addresses': addresses
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(
            self._validators.klay.requests.get_transaction_intersections_by_addresses, params
        )

        params.update(api_key)

        validators.update({200: self._validators.klay.responses.get_transaction_intersections_by_addresses})

        return self._http.get(
            url='{}/addresses/{}/transactions'.format(self._coin_url, ','.join(params.pop('addresses'))),
            params=params,
            validators=validators
        )

    def get_balances_by_addresses(self, addresses: List[str]) -> Union[List[Dict[str, str]], error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, List[str]] = {
            'addresses': addresses
        }

        self._utils.validate_data(self._validators.klay.requests.get_balances_by_addresses, params)

        validators.update({200: self._validators.klay.responses.get_balances_by_addresses})

        return self._http.get(
            url='{}/addresses/{}/balance'.format(self._coin_url, ','.join(params.pop('addresses'))),
            params=api_key,
            validators=validators
        )

    def get_general_information_by_addresses(
        self, addresses: List[str]
    ) -> Union[List[Dict[str, Any]], error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, List[str]] = {
            'addresses': addresses
        }

        self._utils.validate_data(self._validators.klay.requests.get_general_information_by_addresses, params)

        validators.update({200: self._validators.klay.responses.get_general_information_by_addresses})

        return self._http.get(
            url='{}/addresses/{}'.format(self._coin_url, ','.join(params.pop('addresses'))),
            params=api_key,
            validators=validators
        )

    def get_token_transfers_by_addresses(
        self,
        addresses: List[str],
        token: str,
        skip: Optional[int] = None,
        limit: Optional[int] = None
    ) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[int, str, List[str]]] = {
            'addresses': addresses,
            'token': token
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(self._validators.klay.requests.get_token_transfers_by_addresses, params)
        token = params.pop('token')
        addresses = ','.join(params.pop('addresses'))
        params.update(api_key)

        validators.update({200: self._validators.klay.responses.get_token_transfers_by_addresses})

        return self._http.get(
            url='{}/addresses/{}/transfers/tokens/{}'.format(self._coin_url, addresses, token),
            params=params,
            validators=validators
        )

    def get_tokens_balances_by_holders(
        self, addresses: List[str], skip: Optional[int] = None, limit: Optional[int] = None
    ) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[int, str, List[str]]] = {
            'addresses': addresses
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(self._validators.klay.requests.get_tokens_balances_by_holders, params)

        params.update(api_key)

        validators.update({200: self._validators.klay.responses.get_tokens_balances_by_holders})

        return self._http.get(
            url='{}/addresses/{}/balance/tokens'.format(self._coin_url, ','.join(params.pop('addresses'))),
            params=params,
            validators=validators
        )

    def get_token_balance_by_holders_and_token(
        self,
        addresses: List[str],
        token: str,
        skip: Optional[int] = None,
        limit: Optional[int] = None
    ) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[int, str, List[str]]] = {
            'addresses': addresses,
            'token': token
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(self._validators.klay.requests.get_token_balance_by_holders_and_token, params)
        token = params.pop('token')
        addresses = ','.join(params.pop('addresses'))
        params.update(api_key)

        validators.update({200: self._validators.klay.responses.get_token_balance_by_holders_and_token})

        return self._http.get(
            url='{}/addresses/{}/balance/tokens/{}'.format(self._coin_url, addresses, token),
            params=params,
            validators=validators
        )
