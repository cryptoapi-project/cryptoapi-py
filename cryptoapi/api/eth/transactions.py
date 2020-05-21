from typing import Any, Dict, Optional


class Transactions:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_transactions(
        self,
        _from: Optional[str] = None,
        to: Optional[str] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        block_number: Optional[int] = None
    ) -> Dict[str,
              Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str,
                     Union[str,
                           int]] = {}

        if _from is not None:
            params.update({'from': _from})

        if to is not None:
            params.update({'to': to})

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if block_number is not None:
            params.update({'block_number': block_number})

        self._utils.validate_data(self._validators.api.eth.requests.get_transactions, params)

        params.update(api_key)

        validators.update({200: self._validators.api.eth.responses.get_transactions})

        return self._http.get(url='{}/transactions'.format(self._coin_url), params=params, validators=validators)

    def get_transaction_information(self, _hash: str) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str,
                     str] = {
                         'hash': _hash
                     }

        self._utils.validate_data(self._validators.api.eth.requests.get_transaction_information, params)

        validators.update({200: self._validators.api.eth.responses.get_transaction_information})

        return self._http.get(
            url='{}/transactions/{}'.format(self._coin_url,
                                            params['hash']),
            params=api_key,
            validators=validators
        )

    def get_transaction_receipt(self, _hash: str) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str,
                     str] = {
                         'hash': _hash
                     }

        self._utils.validate_data(self._validators.api.eth.requests.get_transaction_receipt, params)

        validators.update({200: self._validators.api.eth.responses.get_transaction_receipt})

        return self._http.get(
            url='{}/transactions/{}/receipt'.format(self._coin_url,
                                                    params['hash']),
            params=api_key,
            validators=validators
        )

    def send_transaction(self, tx: str) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        data: Dict[str,
                   str] = {
                       'tx': tx
                   }

        self._utils.validate_data(self._validators.api.eth.requests.send_transaction, data)

        validators.update({200: self._validators.api.eth.responses.send_transaction})

        return self._http.post(
            url='{}/transactions/raw/send'.format(self._coin_url),
            data=data,
            params=api_key,
            validators=validators
        )

    def decode_transaction(self, tx: str) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        data: Dict[str,
                   str] = {
                       'tx': tx
                   }

        self._utils.validate_data(self._validators.api.eth.requests.decode_transaction, data)

        validators.update({200: self._validators.api.eth.responses.decode_transaction})

        return self._http.post(
            url='{}/transactions/raw/decode'.format(self._coin_url),
            data=data,
            params=api_key,
            validators=validators
        )
