from typing import Any, Callable

from .bch import Bch
from .btc import Btc
from .eth import Eth
from .klay import Klay
from .ltc import Ltc


class Events:

    def __init__(
        self,
        ws_wrapper: Callable,
        config: Any,
        validators: Any,
        utils: Any,
        api_key: str,
        debug: bool
    ) -> None:
        self.eth: Eth = Eth(ws_wrapper, config, validators, utils, api_key, debug)
        self.klay: Klay = Klay(ws_wrapper, config, validators, utils, api_key, debug)
        self.btc: Btc = Btc(ws_wrapper, config, validators, utils, api_key, debug)
        self.bch: Bch = Bch(ws_wrapper, config, validators, utils, api_key, debug)
        self.ltc: Ltc = Ltc(ws_wrapper, config, validators, utils, api_key, debug)
