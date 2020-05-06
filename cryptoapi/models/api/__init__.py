from .rates import Rates
from .eth import Eth
from .btc import Btc
from .bch import Bch
from .ltc import Ltc
from .klay import Klay
from .whooks import Whooks


class Api:

    def __init__(self, model):
        self.rates = Rates(model)
        self.eth = Eth(model)
        self.btc = Btc(model)
        self.bch = Bch(model)
        self.ltc = Ltc(model)
        self.klay = Klay(model)
        self.whooks = Whooks(model)
