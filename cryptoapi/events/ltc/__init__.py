from .testnet import Testnet


class Ltc(Testnet):

    def __init__(
        self,
        ws_wrapper,
        config,
        models,
        api_key,
        debug
    ):
        coin_prefix = 'ltc'
        self._ws = ws_wrapper(
            url=config.events.WS_BASE_URL + coin_prefix,
            api_key=api_key,
            debug=debug
        )
        self._models = models
        self.testnet = Testnet(
            ws_wrapper,
            config,
            models,
            debug,
            api_key
        )
