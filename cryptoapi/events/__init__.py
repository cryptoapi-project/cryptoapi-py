from .eth import Eth


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
