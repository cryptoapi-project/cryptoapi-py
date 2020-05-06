from cryptoapi.utils.api import api_method_preprocessing, validate_data


class Transactions:
    def __init__(
        self,
        http,
        models,
        api_key
    ):
        self._http = http
        self._api_key = api_key
        self._models = models

    def get_transactions(self, _from=None, to=None, skip=None, limit=None, block_number=None):
        api_key, validators = api_method_preprocessing(self)

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

        validate_data(
            self._models.api.eth.requests.get_transactions,
            params
        )

        params.update(api_key)

        validators.update({
            200: self._models.api.eth.responses.get_transactions
        })

        return self._http.get(
            url='/transactions',
            params=params,
            validators=validators
        )

    def get_transaction_information(self, _hash):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'hash': _hash
        }

        validate_data(
            self._models.api.eth.requests.get_transaction_information,
            params
        )

        validators.update({
            200: self._models.api.eth.responses.get_transaction_information
        })

        return self._http.get(
            url='/transactions/{}'.format(params['hash']),
            params=api_key,
            validators=validators
        )

    def get_transaction_receipt(self, _hash):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'hash': _hash
        }

        validate_data(
            self._models.api.eth.requests.get_transaction_receipt,
            params
        )

        validators.update({
            200: self._models.api.eth.responses.get_transaction_receipt
        })

        return self._http.get(
            url='/transactions/{}/receipt'.format(params['hash']),
            params=api_key,
            validators=validators
        )

    def send_transaction(self, tx):
        api_key, validators = api_method_preprocessing(self)

        data = {
            'tx': tx
        }

        validate_data(
            self._models.api.eth.requests.send_transaction,
            data
        )

        validators.update({
            200: self._models.api.eth.responses.send_transaction
        })

        return self._http.post(
            url='/transactions/raw/send',
            data=data,
            params=api_key,
            validators=validators
        )

    def decode_transaction(self, tx):
        api_key, validators = api_method_preprocessing(self)

        data = {
            'tx': tx
        }

        validate_data(
            self._models.api.eth.requests.decode_transaction,
            data
        )

        validators.update({
            200: self._models.api.eth.responses.decode_transaction
        })

        return self._http.post(
            url='/transactions/raw/decode',
            data=data,
            params=api_key,
            validators=validators
        )
