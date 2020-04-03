from .model import Model
from .general import General
from .eth import Eth
from .klay import Klay
from .btc import BTC


class Models:

    def __init__(self):
        self.general = General(Model)

        self.eth = Eth(Model)
        self.btc = BTC(Model)
        self.bch = BTC(Model)
        self.klay = Klay(Model)
