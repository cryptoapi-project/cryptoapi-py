class Testnet:

    def __init__(self, http_wrapper, models, config, utils, debug, api_key):
        self._http = http_wrapper(url=config.api.BASE_TESTNET_HTTP_URL + '/rates', debug=debug)
        self._api_key = api_key
        self._models = models
        self._utils = utils

    def get_coins_rates(self, coins):
        api_key, validators = self._utils.api_method_preprocessing(self)
        params = {
            'coins': coins
        }

        self._utils.validate_data(self._models.api.rates.requests.get_coins_rates, params)

        validators.update({200: self._models.api.rates.responses.get_coins_rates})

        return self._http.get(url='/{}/'.format(','.join(params['coins'])), params=api_key, validators=validators)

    def get_coins_history(self, coins):
        api_key, validators = self._utils.api_method_preprocessing(self)
        params = {
            'coins': coins
        }

        self._utils.validate_data(self._models.api.rates.requests.get_coins_history, params)

        validators.update({200: self._models.api.rates.responses.get_coins_history})

        return self._http.get(
            url='/{}/history'.format(','.join((params['coins']))),
            params=api_key,
            validators=validators
        )
