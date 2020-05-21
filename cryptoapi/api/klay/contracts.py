from typing import Any, Dict, List, Optional, Union

error_static_type = Dict[str, Union[List[Dict[str, str]], int]]


class Contracts:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_contracts_logs(
        self,
        cursor: Optional[str] = None,
        reversed_fetch: Optional[bool] = None,
        from_block: Optional[int] = None,
        to_block: Optional[int] = None,
        addresses: Optional[List[str]] = None,
        topics: Optional[List[str]] = None
    ) -> Union[List[Dict[str,
                         Any]],
               error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str,
                     Union[int,
                           str,
                           bool,
                           List[str]]] = {}
        if cursor is not None:
            params.update({'cursor': cursor})

        if reversed_fetch is not None:
            params.update({'reversed_fetch': reversed_fetch})

        if from_block is not None:
            params.update({'from_block': from_block})

        if to_block is not None:
            params.update({'to_block': to_block})

        if addresses is not None:
            params.update({'addresses': addresses})

        if topics is not None:
            params.update({'topics': topics})

        self._utils.validate_data(self._validators.api.klay.requests.get_contracts_logs, params)

        if 'addresses' in params:
            params['addresses'] = ','.join(params['addresses'])

        if 'topics' in params:
            params['topics'] = ','.join(params['topics'])

        validators.update({200: self._validators.api.klay.responses.get_contracts_logs})

        params.update(api_key)

        return self._http.get(url='{}/contracts/logs'.format(self._coin_url), params=params, validators=validators)

    def contract_call(self,
                      address: str,
                      sender: str,
                      amount: int,
                      bytecode: str) -> Union[str,
                                              error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str,
                     str] = {
                         'address': address
                     }

        data: Dict[str,
                   Union[int,
                         str]] = {
                             'sender': sender,
                             'amount': amount,
                             'bytecode': bytecode
                         }

        self._utils.validate_data(self._validators.api.klay.requests.contract_call_params, params)
        self._utils.validate_data(self._validators.api.klay.requests.contract_call_body, data)

        validators.update({200: self._validators.api.klay.responses.contract_call})

        return self._http.post(
            url='{}/contracts/{}/call'.format(self._coin_url,
                                              params.pop('address')),
            data=data,
            params=api_key,
            validators=validators
        )

    def get_contract_general_information(self, address: str) -> Union[Dict[str, str], error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str,
                     str] = {
                         'address': address
                     }

        self._utils.validate_data(self._validators.api.klay.requests.get_contract_general_information, params)

        validators.update({200: self._validators.api.klay.responses.get_contract_general_information})

        return self._http.get(
            url='{}/contracts/{}'.format(self._coin_url,
                                         params.pop('address')),
            params=api_key,
            validators=validators
        )
