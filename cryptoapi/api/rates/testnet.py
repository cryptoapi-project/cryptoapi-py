class Testnet:

    def __init__(self, http, validators, utils, debug, api_key):
        self._http = http
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

    def get_coins_rates(self, coins):
        api_key, validators = self._utils.api_method_preprocessing(self)
        params = {
            'coins': coins
        }

        self._utils.validate_data(self._validators.api.rates.requests.get_coins_rates, params)

        validators.update({200: self._validators.api.rates.responses.get_coins_rates})

        return self._http.get(
            url='/rates/{}/'.format(','.join(params['coins'])),
            params=api_key,
            validators=validators
        )

    def get_coins_history(self, coins):
        api_key, validators = self._utils.api_method_preprocessing(self)
        params = {
            'coins': coins
        }

        self._utils.validate_data(self._validators.api.rates.requests.get_coins_history, params)

        validators.update({200: self._validators.api.rates.responses.get_coins_history})

        return self._http.get(
            url='/rates/{}/history'.format(','.join((params['coins']))),
            params=api_key,
            validators=validators
        )
