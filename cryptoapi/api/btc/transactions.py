from typing import Any, Dict, Optional, Union


class Transactions:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_transactions(
        self,
        block_height_or_hash: Optional[Union[int, str]] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        _from: Optional[str] = None,
        to: Optional[str] = None
    ) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[int, str]] = {}

        if _from is not None:
            params.update({'from': _from})

        if to is not None:
            params.update({'to': to})

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if block_height_or_hash is not None:
            params.update({'block_height_or_hash': block_height_or_hash})

        self._utils.validate_data(self._validators.btc.requests.get_transactions, params)

        params.update(api_key)

        validators.update({200: self._validators.btc.responses.get_transactions})

        return self._http.get(url='{}/transactions'.format(self._coin_url), params=params, validators=validators)

    def get_transaction_by_hash(self, _hash: str) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, str] = {
            'hash': _hash
        }

        self._utils.validate_data(self._validators.btc.requests.get_transaction_by_hash, params)

        validators.update({200: self._validators.btc.responses.get_transaction_by_hash})

        return self._http.get(
            url='{}/transactions/{}'.format(self._coin_url, params['hash']), params=api_key, validators=validators
        )

    def send_transaction(self, _hash: str) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        data: Dict[str, str] = {
            'hash': _hash
        }

        self._utils.validate_data(self._validators.btc.requests.send_transaction, data)

        validators.update({200: self._validators.btc.responses.send_transaction})

        return self._http.post(
            url='{}/transactions/raw/send'.format(self._coin_url),
            data=data,
            params=api_key,
            validators=validators
        )

    def decode_transaction(self, _hash: str) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        data: Dict[str, str] = {
            'hash': _hash
        }

        self._utils.validate_data(self._validators.btc.requests.decode_transaction, data)

        validators.update({200: self._validators.btc.responses.decode_transaction})

        return self._http.post(
            url='{}/transactions/raw/decode'.format(self._coin_url),
            data=data,
            params=api_key,
            validators=validators
        )
