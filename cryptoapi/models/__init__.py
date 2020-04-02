from .model import Model
from .general import General
from .eth import Eth


class Models:

    def __init__(self):
        self.general = General(Model)

        self.eth = Eth(Model)
        self.btc = None
        self.bch = None
        self.klay = None
