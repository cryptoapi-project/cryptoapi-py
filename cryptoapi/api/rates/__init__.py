from .testnet import Testnet

from typing import Any


class Rates(Testnet):

    def __init__(self, mainnet_http: Any, testnet_http: Any, validators: Any, utils: Any, debug: bool, api_key: str):
        self._http: Any = mainnet_http
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

        self.testnet: Testnet = Testnet(testnet_http, validators, utils, debug, api_key)
