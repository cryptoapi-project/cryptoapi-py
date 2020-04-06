from cryptoapi.utils.api import api_method_preprocessing, validate_data


class Blocks:
    def __init__(
        self,
        http,
        models,
        api_key
    ):
        self._http = http
        self._api_key = api_key
        self._models = models

    def get_block(self, block_height_or_hash):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'block_height_or_hash': block_height_or_hash
        }
        validate_data(
            self._models.btc.requests.get_block,
            params
        )

        validators.update({
            200: self._models.btc.responses.get_block
        })

        return self._http.get(
            url='/blocks/{}'.format(params['block_height_or_hash']),
            params=api_key,
            validators=validators
        )

    def get_blocks(self, skip=None, limit=None):
        api_key, validators = api_method_preprocessing(self)

        params = {}
        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        validate_data(
            self._models.btc.requests.get_blocks,
            params
        )

        validators.update({
            200: self._models.btc.responses.get_blocks
        })

        params.update(api_key)

        return self._http.get(
            url='/blocks',
            params=params,
            validators=validators
        )
