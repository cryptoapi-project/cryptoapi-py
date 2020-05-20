from typing import Any, Dict

from .addresses import Addresses
from .blocks import Blocks
from .common import Common
from .push_notifications import PushNotifications
from .transactions import Transactions


class Testnet:

    def __init__(self, http: Any, validators: Any, utils: Any, debug: bool, api_key: str):
        self._http: Any = http
        self._coin_url: str = '/coins/bch'
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

        self._init_modules()

    def _init_modules(self):
        self.addresses: Addresses = Addresses(
            self._http,
            self._coin_url,
            self._validators,
            self._utils,
            self._api_key
        )

        self.blocks: Blocks = Blocks(self._http, self._coin_url, self._validators, self._utils, self._api_key)

        self.common: Common = Common(self._http, self._coin_url, self._validators, self._utils, self._api_key)

        self.push_notifications: PushNotifications = PushNotifications(
            self._http,
            self._coin_url,
            self._validators,
            self._utils,
            self._api_key
        )

        self.transactions: Transactions = Transactions(
            self._http,
            self._coin_url,
            self._validators,
            self._utils,
            self._api_key
        )
