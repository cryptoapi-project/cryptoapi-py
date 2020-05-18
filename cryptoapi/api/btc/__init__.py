from .testnet import Testnet


class Btc(Testnet):

    def __init__(self, mainnet_http, testnet_http, validators, utils, debug, api_key):
        self._http = mainnet_http
        self._coin_url = '/coins/btc'
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

        self._init_modules()

        self.testnet = Testnet(testnet_http, validators, utils, debug, api_key)
