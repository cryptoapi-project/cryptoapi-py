class Transactions:
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

    def get_transactions(self, block_height_or_hash=None, skip=None, limit=None, _from=None, to=None):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {}

        if _from is not None:
            params.update({'from': _from})

        if to is not None:
            params.update({'to': to})

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if block_height_or_hash is not None:
            params.update({'block_height_or_hash': block_height_or_hash})

        self._utils.validate_data(
            self._models.api.btc.requests.get_transactions,
            params
        )

        params.update(api_key)

        validators.update({
            200: self._models.api.btc.responses.get_transactions
        })

        return self._http.get(
            url='/transactions',
            params=params,
            validators=validators
        )

    def get_transaction_by_hash(self, _hash):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'hash': _hash
        }

        self._utils.validate_data(
            self._models.api.btc.requests.get_transaction_by_hash,
            params
        )

        validators.update({
            200: self._models.api.btc.responses.get_transaction_by_hash
        })

        return self._http.get(
            url='/transactions/{}'.format(params['hash']),
            params=api_key,
            validators=validators
        )

    def send_transaction(self, _hash):
        api_key, validators = self._utils.api_method_preprocessing(self)

        data = {
            'hash': _hash
        }

        self._utils.validate_data(
            self._models.api.btc.requests.send_transaction,
            data
        )

        validators.update({
            200: self._models.api.btc.responses.send_transaction
        })

        return self._http.post(
            url='/transactions/raw/send',
            data=data,
            params=api_key,
            validators=validators
        )

    def decode_transaction(self, _hash):
        api_key, validators = self._utils.api_method_preprocessing(self)

        data = {
            'hash': _hash
        }

        self._utils.validate_data(
            self._models.api.btc.requests.decode_transaction,
            data
        )

        validators.update({
            200: self._models.api.btc.responses.decode_transaction
        })

        return self._http.post(
            url='/transactions/raw/decode',
            data=data,
            params=api_key,
            validators=validators
        )
