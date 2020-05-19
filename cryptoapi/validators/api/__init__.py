from typing import Any, Callable

from .bch import Bch
from .btc import Btc
from .eth import Eth
from .klay import Klay
from .ltc import Ltc
from .rates import Rates
from .whooks import Whooks


class Api:

    def __init__(self, validator: Callable, utils: Any) -> None:
        self.rates: Rates = Rates(validator)
        self.eth: Eth = Eth(validator, utils)
        self.btc: Btc = Btc(validator, utils)
        self.bch: Bch = Bch(validator, utils)
        self.ltc: Ltc = Ltc(validator, utils)
        self.klay: Klay = Klay(validator, utils)
        self.whooks: Whooks = Whooks(validator)
