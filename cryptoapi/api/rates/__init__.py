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
            url=config.BASE_HTTP_URL + '/rates',
            debug=debug
        )
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

    def get_coins_rates(self, coins):
        api_key, validators = self._prepare()
        params = {'coins': ','.join(coins)}
        self._models.rates.requests.get_coins_rates.validate(params)

        validators.update({
            200: self._models.rates.responses.get_coins_rates
        })

        return self._http.get(
            url='/{}/'.format(params['coins']),
            params=api_key,
            validators=validators
        )

    def get_coins_history(self, coins):
        api_key, validators = self._prepare()
        params = {'coins': ','.join(coins)}
        self.models.rates.requests.get_coins_history.validate(params)

        validators.update({
            200: self._models.rates.responses.get_coins_history
        })

        return self._http.get(
            url='/{}/history'.format((params['coins'])),
            params=api_key,
            validators=validators
        )
