from typing import Any, Dict, List, Optional, Union


class Tokens:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_tokens(
        self,
        query: Optional[str] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        types: Optional[List[str]] = None
    ) -> Dict[str,
              Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str,
                     Union[str,
                           int,
                           List[str]]] = {}

        if query is not None:
            params.update({'query': query})

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if types is not None:
            params.update({'types': types})

        self._utils.validate_data(self._validators.api.klay.requests.get_tokens, params)

        if 'types' in params:
            params['types'] = ','.join(params['types'])

        params.update(api_key)

        validators.update({200: self._validators.api.klay.responses.get_tokens})

        return self._http.get(url='{}/tokens/search'.format(self._coin_url), params=params, validators=validators)

    def get_token_transfers_by_token_address(
        self,
        token: str,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        addresses: List[str] = None
    ) -> Dict[str,
              Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str,
                     Union[str,
                           int,
                           List[str]]] = {
                               'token': token
                           }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if addresses is not None:
            params.update({'addresses': addresses})

        self._utils.validate_data(self._validators.api.klay.requests.get_token_transfers_by_token_address, params)

        if 'addresses' in params:
            params['addresses'] = ','.join(params['addresses'])

        token = params.pop('token')

        params.update(api_key)

        validators.update({200: self._validators.api.klay.responses.get_token_transfers_by_token_address})

        return self._http.get(
            url='{}/tokens/{}/transfers'.format(self._coin_url,
                                                token),
            params=params,
            validators=validators
        )

    def get_token_contract(self, address: str) -> Dict[str, Any]:
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str,
                     str] = {
                         'address': address
                     }

        self._utils.validate_data(self._validators.api.klay.requests.get_token_contract, params)

        validators.update({200: self._validators.api.klay.responses.get_token_contract})

        return self._http.get(
            url='{}/tokens/{}'.format(self._coin_url,
                                      params['address']),
            params=api_key,
            validators=validators
        )
