from .testnet import Testnet


class Bch(Testnet):

    def __init__(
        self,
        http_wrapper,
        models,
        config,
        debug,
        api_key
    ):
        coin_url = '/coins/bch'
        self._http = http_wrapper(
            url=config.api.BASE_HTTP_URL + coin_url,
            debug=debug
        )
        self._api_key = api_key
        self._models = models

        self._init_modules()

        self.testnet = Testnet(
            http_wrapper,
            coin_url,
            models,
            config,
            debug,
            api_key
        )
