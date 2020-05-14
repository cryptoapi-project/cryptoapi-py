from .testnet import Testnet


class Ltc(Testnet):

    def __init__(self, ws_wrapper, config, validators, utils, api_key, debug):
        coin_prefix = 'ltc'
        self._ws = ws_wrapper(url=config.events.WS_BASE_URL + coin_prefix, api_key=api_key, debug=debug)
        self._validators = validators
        self._utils = utils

        self.testnet = Testnet(ws_wrapper, config, validators, utils, debug, api_key)
