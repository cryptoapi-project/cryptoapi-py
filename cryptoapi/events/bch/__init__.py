from .testnet import Testnet


class Bch(Testnet):

    def __init__(
        self,
        ws_wrapper,
        config,
        debug,
        api_key
    ):
        coin_prefix = 'bch'
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
