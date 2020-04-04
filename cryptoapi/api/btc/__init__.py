from .testnet import Testnet


class Btc(Testnet):

    def __init__(
        self,
        http_wrapper,
        models,
        config,
        debug,
        api_key
    ):
        self._http = http_wrapper(
            url=config.BASE_HTTP_URL + '/coins/btc',
            debug=debug
        )
        self._api_key = api_key
        self._models = models

        self._init_modules()

        self.testnet = Testnet(
            http_wrapper,
            models,
            config,
            debug,
            api_key
        )
