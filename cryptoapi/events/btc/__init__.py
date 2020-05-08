from .testnet import Testnet


class Btc(Testnet):

    def __init__(self, ws_wrapper, config, models, utils, api_key, debug):
        coin_prefix = 'btc'
        self._ws = ws_wrapper(url=config.events.WS_BASE_URL + coin_prefix, api_key=api_key, debug=debug)
        self._models = models
        self._utils = utils

        self.testnet = Testnet(ws_wrapper, config, models, utils, debug, api_key)
