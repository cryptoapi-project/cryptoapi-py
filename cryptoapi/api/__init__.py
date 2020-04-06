# -*- coding: utf-8 -*-
from cryptoapi.configs.api import Config
from cryptoapi.utils.api import api_method_preprocessing
from .rates import Rates
from .eth import Eth
from .klay import Klay


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
        self.klay = Klay(
            http_wrapper,
            self._models,
            self._config,
            debug,
            api_key
        )

    def get_coins(self):
        api_key, validators = api_method_preprocessing(self)
        validators.update({
            200: self._models.get_coins
        })

        return self._http.get(
            url='/coins',
            params=api_key,
            validators=validators
        )
