from .bch import Bch
from .btc import Btc
from .eth import Eth
from .klay import Klay
from .ltc import Ltc


class Events:

    def __init__(self, ws_wrapper, config, models, utils, api_key, debug):
        self.eth = Eth(ws_wrapper, config, models, utils, api_key, debug)
        self.klay = Klay(ws_wrapper, config, models, utils, api_key, debug)
        self.btc = Btc(ws_wrapper, config, models, utils, api_key, debug)
        self.bch = Bch(ws_wrapper, config, models, utils, api_key, debug)
        self.ltc = Ltc(ws_wrapper, config, models, utils, api_key, debug)
