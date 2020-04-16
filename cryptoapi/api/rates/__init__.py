from cryptoapi.utils.api import api_method_preprocessing, validate_data


class Rates:

    def __init__(
        self,
        http_wrapper,
        models,
        config,
        debug,
        api_key
    ):
        self._http = http_wrapper(
            url=config.api.BASE_HTTP_URL + '/rates',
            debug=debug
        )
        self._api_key = api_key
        self._models = models

    def get_coins_rates(self, coins):
        api_key, validators = api_method_preprocessing(self)
        params = {'coins': ','.join(coins)}

        validate_data(
            self._models.rates.requests.get_coins_rates,
            params
        )

        validators.update({
            200: self._models.rates.responses.get_coins_rates
        })

        return self._http.get(
            url='/{}/'.format(params['coins']),
            params=api_key,
            validators=validators
        )

    def get_coins_history(self, coins):
        api_key, validators = api_method_preprocessing(self)
        params = {'coins': ','.join(coins)}

        validate_data(
            self._models.rates.requests.get_coins_history,
            params
        )

        validators.update({
            200: self._models.rates.responses.get_coins_history
        })

        return self._http.get(
            url='/{}/history'.format((params['coins'])),
            params=api_key,
            validators=validators
        )
