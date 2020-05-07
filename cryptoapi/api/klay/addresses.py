class Addresses:
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

    def get_transactions_by_addresses(self, addresses, skip=None, limit=None, positive=None):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'addresses': addresses
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if positive is not None:
            params.update({'positive': positive})

        self._utils.validate_data(
            self._models.api.klay.requests.get_transactions_by_addresses,
            params
        )

        params.update(api_key)

        validators.update({
            200: self._models.api.klay.responses.get_transactions_by_addresses
        })

        return self._http.get(
            url='/addresses/{}/transfers'.format(
                ','.join(params.pop('addresses'))
            ),
            params=params,
            validators=validators
        )

    def get_transaction_intersections_by_addresses(self, addresses, skip=None, limit=None):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'addresses': addresses
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(
            self._models.api.klay.requests.get_transaction_intersections_by_addresses,
            params
        )

        params.update(api_key)

        validators.update({
            200: self._models.api.klay.responses.get_transaction_intersections_by_addresses
        })

        return self._http.get(
            url='/addresses/{}/transactions'.format(
                ','.join(params.pop('addresses'))
            ),
            params=params,
            validators=validators
        )

    def get_balances_by_addresses(self, addresses):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'addresses': addresses
        }

        self._utils.validate_data(
            self._models.api.klay.requests.get_balances_by_addresses,
            params
        )

        validators.update({
            200: self._models.api.klay.responses.get_balances_by_addresses
        })

        return self._http.get(
            url='/addresses/{}/balance'.format(
                ','.join(params.pop('addresses'))
            ),
            params=api_key,
            validators=validators
        )

    def get_general_information_by_addresses(self, addresses):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'addresses': addresses
        }

        self._utils.validate_data(
            self._models.api.klay.requests.get_general_information_by_addresses,
            params
        )

        validators.update({
            200: self._models.api.klay.responses.get_general_information_by_addresses
        })

        return self._http.get(
            url='/addresses/{}'.format(
                ','.join(params.pop('addresses'))
            ),
            params=api_key,
            validators=validators
        )

    def get_token_transfers_by_addresses(self, addresses, token, skip=None, limit=None):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'addresses': addresses,
            'token': token
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(
            self._models.api.klay.requests.get_token_transfers_by_addresses,
            params
        )
        token = params.pop('token')
        addresses = ','.join(params.pop('addresses'))
        params.update(api_key)

        validators.update({
            200: self._models.api.klay.responses.get_token_transfers_by_addresses
        })

        return self._http.get(
            url='/addresses/{}/transfers/tokens/{}'.format(
                addresses,
                token
            ),
            params=params,
            validators=validators
        )

    def get_tokens_balances_by_holders(self, addresses, skip=None, limit=None):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'addresses': addresses
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(
            self._models.api.klay.requests.get_tokens_balances_by_holders,
            params
        )

        params.update(api_key)

        validators.update({
            200: self._models.api.klay.responses.get_tokens_balances_by_holders
        })

        return self._http.get(
            url='/addresses/{}/balance/tokens'.format(
                ','.join(params.pop('addresses'))
            ),
            params=params,
            validators=validators
        )

    def get_token_balance_by_holders_and_token(self, addresses, token, skip=None, limit=12):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'addresses': addresses,
            'token': token
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        self._utils.validate_data(
            self._models.api.klay.requests.get_token_balance_by_holders_and_token,
            params
        )
        token = params.pop('token')
        addresses = ','.join(params.pop('addresses'))
        params.update(api_key)

        validators.update({
            200: self._models.api.klay.responses.get_token_balance_by_holders_and_token
        })

        return self._http.get(
            url='/addresses/{}/balance/tokens/{}'.format(
                addresses,
                token
            ),
            params=params,
            validators=validators
        )
