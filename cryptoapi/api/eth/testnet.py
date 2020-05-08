from .addresses import Addresses
from .blocks import Blocks
from .common import Common
from .contracts import Contracts
from .push_notifications import PushNotifications
from .tokens import Tokens
from .transactions import Transactions


class Testnet:

    def __init__(self, http_wrapper, models, config, utils, debug, api_key):
        self._http = http_wrapper(url=config.api.BASE_TESTNET_HTTP_URL + '/coins/eth', debug=debug)
        self._api_key = api_key
        self._models = models
        self._utils = utils

        self._init_modules()

    def _init_modules(self):
        self.addresses = Addresses(self._http, self._models, self._utils, self._api_key)

        self.blocks = Blocks(self._http, self._models, self._utils, self._api_key)

        self.common = Common(self._http, self._models, self._utils, self._api_key)

        self.contracts = Contracts(self._http, self._models, self._utils, self._api_key)

        self.push_notifications = PushNotifications(self._http, self._models, self._utils, self._api_key)

        self.tokens = Tokens(self._http, self._models, self._utils, self._api_key)

        self.transactions = Transactions(self._http, self._models, self._utils, self._api_key)
