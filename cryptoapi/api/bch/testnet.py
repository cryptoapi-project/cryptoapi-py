from .addresses import Addresses
from .blocks import Blocks
from .common import Common
from .push_notifications import PushNotifications
from .transactions import Transactions


class Testnet:

    def __init__(self, http, validators, utils, debug, api_key):
        self._http = http
        self._coin_url = '/coins/bch'
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

        self._init_modules()

    def _init_modules(self):
        self.addresses = Addresses(self._http, self._coin_url, self._validators, self._utils, self._api_key)

        self.blocks = Blocks(self._http, self._coin_url, self._validators, self._utils, self._api_key)

        self.common = Common(self._http, self._coin_url, self._validators, self._utils, self._api_key)

        self.push_notifications = PushNotifications(
            self._http,
            self._coin_url,
            self._validators,
            self._utils,
            self._api_key
        )

        self.transactions = Transactions(self._http, self._coin_url, self._validators, self._utils, self._api_key)
