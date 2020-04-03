# -*- coding: utf-8 -*-
from .config import Config
from .rates import Rates
from .eth import Eth


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
        self._models = models

        self.rates = Rates(
            http_wrapper,
            self._models,
            self._config,
            debug,
            api_key
        )
        self.eth = Eth(
            http_wrapper,
            self._models,
            self._config,
            debug,
            api_key
        )
        self.btc = None
        self.bch = None
        self.klay = None

    def _prepare(self):
        if not self._api_key:
            raise Exception('api_key exception')

        validators = {
            401: self._models.error,
            422: self._models.error
        }

        return {'token': self._api_key}, validators

    def get_coins(self):
        api_key, validators = self._prepare()
        validators.update({
            200: self._models.get_coins
        })

        return self._http.get(
            url='/coins',
            params=api_key,
            validators=validators
        )
