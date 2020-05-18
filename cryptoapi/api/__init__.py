from .bch import Bch
from .btc import Btc
from .eth import Eth
from .klay import Klay
from .ltc import Ltc
from .rates import Rates
from .testnet import Testnet
from .whooks import Whooks


class Api(Testnet):

    def __init__(self, http_wrapper, config, validators, utils, api_key, debug):
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

        mainnet_http = http_wrapper(url=config.api.BASE_HTTP_URL, debug=debug)
        testnet_http = http_wrapper(url=config.api.BASE_TESTNET_HTTP_URL, debug=debug)
        whooks_http = http_wrapper(url=config.api.BASE_WEB_HOOKS_URL, debug=debug)
        self._http = mainnet_http

        self.testnet = Testnet(testnet_http, validators, utils, api_key, debug)

        self.rates = Rates(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.eth = Eth(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.btc = Btc(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.bch = Bch(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.ltc = Ltc(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.klay = Klay(mainnet_http, testnet_http, self._validators, self._utils, debug, api_key)
        self.whooks = Whooks(whooks_http, self._validators, self._utils, debug, api_key)
