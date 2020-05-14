from .testnet import Testnet


class Klay(Testnet):

    def __init__(self, http_wrapper, validators, config, utils, debug, api_key):
        self._http = http_wrapper(url=config.api.BASE_HTTP_URL + '/coins/klay', debug=debug)
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

        self.testnet = Testnet(http_wrapper, validators, config, utils, debug, api_key)
