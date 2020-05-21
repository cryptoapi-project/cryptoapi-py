from typing import Any

from .testnet import Testnet


class Ltc(Testnet):

    def __init__(
        self,
        mainnet_http: Any,
        testnet_http: Any,
        validators: Any,
        utils: Any,
        debug: bool,
        api_key: str
    ) -> None:
        self._http: Any = mainnet_http
        self._coin_url: str = '/coins/ltc'
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

        self._init_modules()

        self.testnet: Testnet = Testnet(testnet_http, validators, utils, debug, api_key)
