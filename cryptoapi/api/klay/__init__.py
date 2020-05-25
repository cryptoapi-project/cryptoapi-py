from typing import Any

from .testnet import Testnet


class Klay(Testnet):

    def __init__(self, mainnet_http: Any, testnet_http: Any, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = mainnet_http
        self._coin_url: str = '/coins/Klay'
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

        self._init_modules()

        self.testnet: Testnet = Testnet(testnet_http, validators, utils, api_key)
