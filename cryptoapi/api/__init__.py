from .bch import Bch
from .btc import Btc
from .eth import Eth
from .klay import Klay
from .ltc import Ltc
from .rates import Rates
from .testnet import Testnet
from .whooks import Whooks

from typing import Any, Callalbe


class Api(Testnet):

    def __init__(self, http_wrapper: Callable, config: Any, validators: Any, utils: Any, api_key: str, debug: bool) -> None:
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

        mainnet_http: Any = http_wrapper(url=config.api.BASE_HTTP_URL, debug=debug)
        testnet_http: Any = http_wrapper(url=config.api.BASE_TESTNET_HTTP_URL, debug=debug)
        whooks_http: Any = http_wrapper(url=config.api.BASE_WEB_HOOKS_URL, debug=debug)
        self._http: Any = mainnet_http

        self.testnet: Testnet = Testnet(testnet_http, validators, utils, api_key, debug)

        self.rates: Rates = Rates(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.eth: Eth = Eth(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.btc: Btc = Btc(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.bch: Bch = Bch(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.ltc: Ltc = Ltc(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.klay: Klay = Klay(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.whooks: Whooks = Whooks(whooks_http, self._validators, self._utils, debug, api_key)
