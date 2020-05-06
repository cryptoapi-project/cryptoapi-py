from .testnet import Testnet


class Klay(Testnet):

    def __init__(
        self,
        http_wrapper,
        models,
        config,
        debug,
        api_key
    ):
        self._http = http_wrapper(
            url=config.api.BASE_HTTP_URL + '/coins/klay',
            debug=debug
        )
        self._api_key = api_key
        self._models = models

        self.testnet = Testnet(
            http_wrapper,
            models,
            config,
            debug,
            api_key
        )
