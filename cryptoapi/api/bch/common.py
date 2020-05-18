class Common:

    def __init__(self, http, coin_url, validators, utils, api_key):
        self._http = http
        self._coin_url = coin_url
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

    def get_network_information(self):
        api_key, validators = self._utils.api_method_preprocessing(self)

        validators.update({200: self._validators.api.bch.responses.get_network_information})

        return self._http.get(url='{}/network'.format(self._coin_url), params=api_key, validators=validators)

    def get_estimate_fee(self):
        api_key, validators = self._utils.api_method_preprocessing(self)

        validators.update({200: self._validators.api.bch.responses.get_estimate_fee})

        return self._http.get(url='{}/estimate-fee'.format(self._coin_url), params=api_key, validators=validators)
