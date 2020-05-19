from typing import Any, Callable

from .testnet import Testnet


class Btc(Testnet):

    def __init__(
        self,
        ws_wrapper: Callable,
        config: Any,
        validators: Any,
        utils: Any,
        api_key: str,
        debug: bool
    ) -> None:
        coin_prefix: str = 'btc'
        self._ws: Any = ws_wrapper(url=config.events.WS_BASE_URL + coin_prefix, api_key=api_key, debug=debug)
        self._validators: Any = validators
        self._utils: Any = utils

        self.testnet: Testnet = Testnet(ws_wrapper, config, validators, utils, api_key, debug)
