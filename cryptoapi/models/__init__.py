from .model import Model
from .general import General
from .eth import Eth
from .klay import Klay

class Models:

    def __init__(self):
        self.general = General(Model)

        self.eth = Eth(Model)
        self.btc = None
        self.bch = None
        self.klay = Klay(Model)
