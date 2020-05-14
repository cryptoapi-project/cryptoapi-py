class Testnet:

    def __init__(self, http_wrapper, config, validators, utils, api_key, debug):
        self._config = config
        self._http = http_wrapper(self._config.api.BASE_TESTNET_HTTP_URL, debug)
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

    def get_coins(self):
        api_key, validators = self._utils.api_method_preprocessing(self)
        validators.update({200: self._validators.get_coins})

        return self._http.get(url='/coins', params=api_key, validators=validators)
