from .testnet import Testnet


class Eth(Testnet):

    def __init__(
        self,
        ws_wrapper,
        config,
        api_key,
        debug
    ):
        coin_prefix = 'eth'
        self._ws = ws_wrapper(
            url=config.events.WS_BASE_URL + coin_prefix,
            api_key=api_key,
            debug=debug
        )

        self.testnet = Testnet(
            ws_wrapper,
            config,
            debug,
            api_key
        )
