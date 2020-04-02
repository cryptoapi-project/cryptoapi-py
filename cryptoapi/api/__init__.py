# -*- coding: utf-8 -*-
from .config import Config
from .rates import Rates


class Api:

    def __init__(
        self,
        http_wrapper,
        models,
        api_key,
        debug=False
    ):
        self._config = Config()
        self._http = http_wrapper(
            self._config.BASE_HTTP_URL,
            debug
        )
        self._api_key = api_key
        self.models = models

        self.rates = Rates(
            http_wrapper,
            self.models,
            self._config,
            debug,
            api_key
        )
        self.eth = None
        self.btc = None
        self.bch = None
        self.klay = None

    def _prepare(self):
        if not self._api_key:
            raise Exception('api_key exception')

        validators = {
            401: self.models.error,
            422: self.models.error
        }

        return {'token': self._api_key}, validators

    def get_coins(self, *args, **kwargs):
        api_key, validators = self._prepare()
        validators.update({
            200: self.models.get_coins
        })

        response = self._http.get(
            url='/coins',
            params=api_key,
            validators=validators
        )
        return response
