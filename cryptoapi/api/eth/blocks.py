from typing import Any, Dict, Optional, Union


class Blocks:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_block(self, block_number_or_hash: Union[int, str]) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[int, str]] = {
            'block_number_or_hash': block_number_or_hash
        }
        self._utils.validate_data(self._validators.eth.requests.get_block, params)

        validators.update({200: self._validators.eth.responses.get_block})

        return self._http.get(
            url='{}/blocks/{}'.format(self._coin_url, params['block_number_or_hash']),
            params=api_key,
            validators=validators
        )

    def get_blocks(self, skip: Optional[int] = None, limit: Optional[int] = None) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[str, int]] = {}
        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(self._validators.eth.requests.get_blocks, params)

        validators.update({200: self._validators.eth.responses.get_blocks})

        params.update(api_key)

        return self._http.get(url='{}/blocks'.format(self._coin_url), params=params, validators=validators)
