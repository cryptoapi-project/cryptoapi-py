class Blocks:
    def __init__(
        self,
        http,
        models,
        utils,
        api_key
    ):
        self._http = http
        self._api_key = api_key
        self._models = models
        self._utils = utils

    def get_block(self, block_number_or_hash):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'block_number_or_hash': block_number_or_hash
        }
        self._utils.validate_data(
            self._models.api.eth.requests.get_block,
            params
        )

        validators.update({
            200: self._models.api.eth.responses.get_block
        })

        return self._http.get(
            url='/blocks/{}'.format(params['block_number_or_hash']),
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

        self._utils.validate_data(
            self._models.api.eth.requests.get_blocks,
            params
        )

        validators.update({
            200: self._models.api.eth.responses.get_blocks
        })

        params.update(api_key)

        return self._http.get(
            url='/blocks',
            params=params,
            validators=validators
        )
