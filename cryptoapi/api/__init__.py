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
        self._config = config
        self._http = http_wrapper(self._config.api.BASE_HTTP_URL, debug)
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

        self.testnet = Testnet(http_wrapper, config, validators, utils, api_key, debug)

        self.rates = Rates(http_wrapper, self._validators, self._config, self._utils, debug, api_key)
        self.eth = Eth(http_wrapper, self._validators, self._config, self._utils, debug, api_key)
        self.btc = Btc(http_wrapper, self._validators, self._config, self._utils, debug, api_key)
        self.bch = Bch(http_wrapper, self._validators, self._config, self._utils, debug, api_key)
        self.ltc = Ltc(http_wrapper, self._validators, self._config, self._utils, debug, api_key)
        self.klay = Klay(http_wrapper, self._validators, self._config, self._utils, debug, api_key)
        self.whooks = Whooks(http_wrapper, self._validators, self._config, self._utils, debug, api_key)
