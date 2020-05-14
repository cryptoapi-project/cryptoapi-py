from .bch import Bch
from .btc import Btc
from .eth import Eth
from .klay import Klay
from .ltc import Ltc
from .rates import Rates
from .whooks import Whooks


class Api:

    def __init__(self, validator, utils):
        self.rates = Rates(validator)
        self.eth = Eth(validator, utils)
        self.btc = Btc(validator, utils)
        self.bch = Bch(validator, utils)
        self.ltc = Ltc(validator, utils)
        self.klay = Klay(validator, utils)
        self.whooks = Whooks(validator)
