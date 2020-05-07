from .rates import Rates
from .eth import Eth
from .btc import Btc
from .bch import Bch
from .ltc import Ltc
from .klay import Klay
from .whooks import Whooks


class Api:

    def __init__(self, model, utils):
        self.rates = Rates(model)
        self.eth = Eth(model, utils)
        self.btc = Btc(model, utils)
        self.bch = Bch(model, utils)
        self.ltc = Ltc(model, utils)
        self.klay = Klay(model, utils)
        self.whooks = Whooks(model)
