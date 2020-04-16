from .eth import Eth
from .klay import Klay
from .btc import Btc
from .bch import Bch


class Events:
    def __init__(
            self,
            ws_wrapper,
            config,
            debug,
            api_key
    ):
        self.eth = Eth(
            ws_wrapper,
            config,
            api_key,
            debug
        )
        self.klay = Klay(
            ws_wrapper,
            config,
            api_key,
            debug
        )
        self.btc = Btc(
            ws_wrapper,
            config,
            api_key,
            debug
        )
        self.bch = Bch(
            ws_wrapper,
            config,
            api_key,
            debug
        )
