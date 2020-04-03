class Blocks:
    def __init__(
        self,
        http,
        models,
        debug,
        api_key
    ):
        self._http = http
        self._api_key = api_key
        self._models = models

    def _prepare(self):
        if not self._api_key:
            raise Exception('api_key exception')

        validators = {
            401: self._models.error,
            422: self._models.error
        }

        return {'token': self._api_key}, validators

    def get_block(self, block_number_or_hash):
        api_key, validators = self._prepare()

        params = {
            'block_number_or_hash': block_number_or_hash
        }
        self._models.eth.requests.get_block.validate(params)

        validators.update({
            200: self._models.eth.responses.get_block
        })

        return self._http.get(
            url='/blocks/{}'.format(params['block_number_or_hash']),
            params=api_key,
            validators=validators
        )

    def get_blocks(self, skip=None, limit=None):
        api_key, validators = self._prepare()

        params = {}
        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._models.eth.requests.estimate_gas.validate(params)

        validators.update({
            200: self._models.eth.responses.estimate_gas
        })

        params.update(api_key)

        return self._http.get(
            url='/blocks',
            params=params,
            validators=validators
        )
