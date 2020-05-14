class Common:

    def __init__(self, http, validators, utils, api_key):
        self._http = http
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

    def get_network_information(self):
        api_key, validators = self._utils.api_method_preprocessing(self)

        validators.update({200: self._validators.api.bch.responses.get_network_information})

        return self._http.get(url='/network', params=api_key, validators=validators)

    def get_estimate_fee(self):
        api_key, validators = self._utils.api_method_preprocessing(self)

        validators.update({200: self._validators.api.bch.responses.get_estimate_fee})

        return self._http.get(url='/estimate-fee', params=api_key, validators=validators)
