class Transactions:
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

    def get_transactions(self, _from=None, to=None, skip=None, limit=None, block_number=None):
        api_key, validators = self._prepare()

        params = {
        }

        if _from is not None:
            params.update({'from': _from})

        if to is not None:
            params.update({'to': to})

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        if block_number is not None:
            params.update({'block_number': block_number})

        self._models.eth.requests.get_transactions.validate(params)

        params.update(api_key)

        validators.update({
            200: self._models.eth.responses.get_transactions
        })

        return self._http.get(
            url='/transactions',
            params=params,
            validators=validators
        )

    def get_transaction_information(self, _hash):
        api_key, validators = self._prepare()

        params = {
            'hash': _hash
        }

        self._models.eth.requests.get_transaction_information.validate(params)

        validators.update({
            200: self._models.eth.responses.get_transaction_information
        })

        return self._http.get(
            url='/transactions/{}'.format(params['hash']),
            params=api_key,
            validators=validators
        )

    def get_transaction_receipt(self, _hash):
        api_key, validators = self._prepare()

        params = {
            'hash': _hash
        }

        self._models.eth.requests.get_transaction_receipt.validate(params)

        validators.update({
            200: self._models.eth.responses.get_transaction_receipt
        })

        return self._http.get(
            url='/transactions/{}/receipt'.format(params['hash']),
            params=api_key,
            validators=validators
        )

    def send_transaction(self, tx):
        api_key, validators = self._prepare()

        data = {
            'tx': tx
        }
        self._models.eth.requests.send_transaction.validate(data)

        validators.update({
            200: self._models.eth.responses.send_transaction
        })

        return self._http.post(
            url='/transactions/raw/send',
            data=data,
            params=api_key,
            validators=validators
        )

    def decode_transaction(self, tx):
        api_key, validators = self._prepare()

        data = {
            'tx': tx
        }
        self._models.eth.requests.decode_transaction.validate(data)

        validators.update({
            200: self._models.eth.responses.decode_transaction
        })

        return self._http.post(
            url='/transactions/raw/decode',
            data=data,
            params=api_key,
            validators=validators
        )
