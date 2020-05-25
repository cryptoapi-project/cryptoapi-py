from typing import Any

from ..utils import Utils
from .bch import Bch
from .btc import Btc
from .config import Config
from .eth import Eth
from .klay import Klay
from .ltc import Ltc
from .rates import Rates
from .rpc import HTTP
from .testnet import Testnet
from .validators import Validators
from .whooks import Whooks


class Api(Testnet):

    def __init__(self, api_key: str, debug: bool = False, utils: Any = Utils()) -> None:
        self._api_key: str = api_key
        self._utils: Utils = utils
        self._validators: Validators = Validators(self._utils)
        self._config: Config = Config()

        mainnet_http: HTTP = HTTP(url=self._config.BASE_HTTP_URL, debug=debug)
        testnet_http: HTTP = HTTP(url=self._config.BASE_TESTNET_HTTP_URL, debug=debug)
        whooks_http: HTTP = HTTP(url=self._config.BASE_WEB_HOOKS_URL, debug=debug)
        self._http: Any = mainnet_http

        self.testnet: Testnet = Testnet(testnet_http, utils, self._api_key)

        self.rates: Rates = Rates(mainnet_http, testnet_http, self._validators, self._utils, self._api_key)
        self.eth: Eth = Eth(mainnet_http, testnet_http, self._validators, self._utils, self._api_key)
        self.btc: Btc = Btc(mainnet_http, testnet_http, self._validators, self._utils, self._api_key)
        self.bch: Bch = Bch(mainnet_http, testnet_http, self._validators, self._utils, self._api_key)
        self.ltc: Ltc = Ltc(mainnet_http, testnet_http, self._validators, self._utils, self._api_key)
        self.klay: Klay = Klay(mainnet_http, testnet_http, self._validators, self._utils, self._api_key)
        self.whooks: Whooks = Whooks(whooks_http, self._validators, self._utils, self._api_key)
