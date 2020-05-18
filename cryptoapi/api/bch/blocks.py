class Blocks:

    def __init__(self, http, coin_url, validators, utils, api_key):
        self._http = http
        self._coin_url = coin_url
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

    def get_block(self, block_height_or_hash):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'block_height_or_hash': block_height_or_hash
        }
        self._utils.validate_data(self._validators.api.bch.requests.get_block, params)

        validators.update({200: self._validators.api.bch.responses.get_block})

        return self._http.get(
            url='{}/blocks/{}'.format(self._coin_url,
                                      params['block_height_or_hash']),
            params=api_key,
            validators=validators
        )

    def get_blocks(self, skip=None, limit=None):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {}
        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(self._validators.api.bch.requests.get_blocks, params)

        validators.update({200: self._validators.api.bch.responses.get_blocks})

        params.update(api_key)

        return self._http.get(url='{}/blocks'.format(self._coin_url), params=params, validators=validators)
