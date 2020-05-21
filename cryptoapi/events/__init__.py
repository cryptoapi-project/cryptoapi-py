from typing import Any

from ..utils import Utils
from .bch import Bch
from .btc import Btc
from .config import Config
from .eth import Eth
from .klay import Klay
from .ltc import Ltc
from .rpc import WS
from .validators import Validators


class Events:

    def __init__(self, api_key: str, debug: bool = False, utils: Any = Utils()) -> None:
        self._utils: Utils = utils
        self._validators: Validators = Validators(self._utils)
        self._config: Config = Config()

        self.eth: Eth = Eth(WS, self._config, self._validators, self._utils, api_key, debug)
        self.klay: Klay = Klay(WS, self._config, self._validators, self._utils, api_key, debug)
        self.btc: Btc = Btc(WS, self._config, self._validators, self._utils, api_key, debug)
        self.bch: Bch = Bch(WS, self._config, self._validators, self._utils, api_key, debug)
        self.ltc: Ltc = Ltc(WS, self._config, self._validators, self._utils, api_key, debug)
