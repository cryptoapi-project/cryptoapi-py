from .testnet import Testnet


class Ltc(Testnet):

    def __init__(self, http_wrapper, models, config, utils, debug, api_key):
        coin_url = '/coins/ltc'
        self._http = http_wrapper(url=config.api.BASE_HTTP_URL + coin_url, debug=debug)
        self._api_key = api_key
        self._models = models
        self._utils = utils

        self.testnet = Testnet(http_wrapper, coin_url, models, config, utils, debug, api_key)
