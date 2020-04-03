class Addresses:
    def __init__(
        self,
        http,
        models,
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

    def get_transactions_by_addresses(self, addresses, skip=None, limit=None, positive=None):
        api_key, validators = self._prepare()

        params = {
            'addresses': ','.join(addresses)
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if positive is not None:
            params.update({'positive': positive})

        self._models.eth.requests.get_transactions_by_addresses.validate(params)

        params.update(api_key)

        validators.update({
            200: self._models.eth.responses.get_transactions_by_addresses
        })

        return self._http.get(
            url='/addresses/{}/transfers'.format(params['addresses']),
            params=params,
            validators=validators
        )

    def get_transaction_intersections_by_addresses(self, addresses, skip=None, limit=None):
        api_key, validators = self._prepare()

        params = {
            'addresses': ','.join(addresses)
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._models.eth.requests.get_transaction_intersections_by_addresses.validate(params)

        params.update(api_key)

        validators.update({
            200: self._models.eth.responses.get_transaction_intersections_by_addresses
        })

        return self._http.get(
            url='/addresses/{}/transactions'.format(params['addresses']),
            params=params,
            validators=validators
        )

    def get_balances_by_addresses(self, addresses):
        api_key, validators = self._prepare()

        params = {
            'addresses': ','.join(addresses)
        }

        self._models.eth.requests.get_balances_by_addresses.validate(params)

        validators.update({
            200: self._models.eth.responses.get_balances_by_addresses
        })

        return self._http.get(
            url='/addresses/{}/balance'.format(params['addresses']),
            params=api_key,
            validators=validators
        )

    def get_general_information_by_addresses(self, addresses):
        api_key, validators = self._prepare()

        params = {
            'addresses': ','.join(addresses)
        }

        self._models.eth.requests.get_general_information_by_addresses.validate(params)

        validators.update({
            200: self._models.eth.responses.get_general_information_by_addresses
        })

        return self._http.get(
            url='/addresses/{}'.format(params['addresses']),
            params=api_key,
            validators=validators
        )

    def get_token_transfers_by_addresses(self, addresses, token, skip=None, limit=None):
        api_key, validators = self._prepare()

        params = {
            'addresses': ','.join(addresses),
            'token': token
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._models.eth.requests.get_token_transfers_by_addresses.validate(params)

        params.update(api_key)

        validators.update({
            200: self._models.eth.responses.get_token_transfers_by_addresses
        })

        return self._http.get(
            url='/addresses/{}/transfers/tokens/{}'.format(
                params['addresses'],
                params['token']
            ),
            params=params,
            validators=validators
        )

    def get_tokens_balances_by_holders(self, addresses, skip=None, limit=None):
        api_key, validators = self._prepare()

        params = {
            'addresses': ','.join(addresses)
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._models.eth.requests.get_tokens_balances_by_holders.validate(params)

        params.update(api_key)

        validators.update({
            200: self._models.eth.responses.get_tokens_balances_by_holders
        })

        return self._http.get(
            url='/addresses/{}/balance/tokens'.format(params['addresses']),
            params=params,
            validators=validators
        )

    def get_token_balance_by_holders_and_token(self, addresses, token, skip=None, limit=None):
        api_key, validators = self._prepare()

        params = {
            'addresses': ','.join(addresses),
            'token': token
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._models.eth.requests.get_token_balance_by_holders_and_token.validate(params)

        params.update(api_key)

        validators.update({
            200: self._models.eth.responses.get_token_balance_by_holders_and_token
        })

        return self._http.get(
            url='/addresses/{}/balance/tokens/{}'.format(
                params['addresses'],
                params['token']
            ),
            params=params,
            validators=validators
        )
