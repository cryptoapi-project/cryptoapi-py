class Tokens:

    def __init__(self, http, models, utils, api_key):
        self._http = http
        self._api_key = api_key
        self._models = models
        self._utils = utils

    def get_tokens(self, query=None, skip=None, limit=None, types=None):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {}

        if query is not None:
            params.update({'query': query})

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if types is not None:
            params.update({'types': ','.join(types)})

        self._utils.validate_data(self._models.api.klay.requests.get_tokens, params)

        params.update(api_key)

        validators.update({200: self._models.api.klay.responses.get_tokens})

        return self._http.get(url='/tokens/search', params=params, validators=validators)

    def get_token_transfers_by_token_address(self, token, skip=None, limit=None, addresses=None):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'token': token
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if addresses is not None:
            params.update({'addresses': ','.join(addresses)})

        self._utils.validate_data(self._models.api.klay.requests.get_token_transfers_by_token_address, params)
        token = params.pop('token')
        params.update(api_key)

        validators.update({200: self._models.api.klay.responses.get_token_transfers_by_token_address})

        return self._http.get(url='/tokens/{}/transfers'.format(token), params=params, validators=validators)

    def get_token_contract(self, address):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'address': address
        }

        self._utils.validate_data(self._models.api.klay.requests.get_token_contract, params)

        validators.update({200: self._models.api.klay.responses.get_token_contract})

        return self._http.get(
            url='/tokens/{}'.format(params.pop('address')),
            params=api_key,
            validators=validators
        )
