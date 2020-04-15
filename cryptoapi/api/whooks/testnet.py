from .whooks import Whooks


class Testnet:

    def __init__(
        self,
        http_wrapper,
        models,
        config,
        debug,
        api_key
    ):
        self._http = http_wrapper(
            url=config.api.BASE_WEB_HOOKS_URL,
            debug=debug
        )
        self._api_key = api_key
        self._models = models

        self._init_modules()

    def _init_modules(self):
        self.whooks = Whooks(
            self._http,
            self._models,
            self._api_key
        )
