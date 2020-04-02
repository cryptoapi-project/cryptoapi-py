from .model import Model
from .general import General


class Models:

    def __init__(self):
        self.general = General(Model)

        self.eth = None
        self.btc = None
        self.bch = None
        self.klay = None
