from cryptoapi.utils.api import api_method_preprocessing, validate_data


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

    def get_outputs_by_addresses(self, addresses, status, skip=None, limit=None):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'addresses': addresses,
            'status': status
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        validate_data(
            self._models.ltc.requests.get_outputs_by_addresses,
            params
        )

        params.update(api_key)

        validators.update({
            200: self._models.ltc.responses.get_outputs_by_addresses
        })

        return self._http.get(
            url='/addresses/{}/outputs'.format(
                ','.join(params.pop('addresses'))
            ),
            params=params,
            validators=validators
        )

    def get_utxo_coin_addresses_info(self, addresses):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'addresses': addresses
        }

        validate_data(
            self._models.ltc.requests.get_utxo_coin_addresses_info,
            params
        )

        validators.update({
            200: self._models.ltc.responses.get_utxo_coin_addresses_info
        })

        return self._http.get(
            url='/addresses/{}'.format(
                ','.join(params.pop('addresses'))
            ),
            params=api_key,
            validators=validators
        )

    def get_utxo_coin_addresses_history(self, addresses, skip=None, limit=None):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'addresses': addresses
        }

        if skip is not None:
            params.update({'skip': skip})

        if limit is not None:
            params.update({'limit': limit})

        validate_data(
            self._models.ltc.requests.get_utxo_coin_addresses_history,
            params
        )

        params.update(api_key)

        validators.update({
            200: self._models.ltc.responses.get_utxo_coin_addresses_history
        })

        return self._http.get(
            url='/addresses/{}/transactions'.format(
                ','.join(params.pop('addresses'))
            ),
            params=params,
            validators=validators
        )
