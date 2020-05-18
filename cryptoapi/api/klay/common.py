class Common:

    def __init__(self, http, coin_url, validators, utils, api_key):
        self._http = http
        self._coin_url = coin_url
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

    def get_network_info(self):
        api_key, validators = self._utils.api_method_preprocessing(self)

        validators.update({200: self._validators.api.klay.responses.get_network_info})

        return self._http.get(url='{}/network'.format(self._coin_url), params=api_key, validators=validators)

    def estimate_gas(self, _from, to, data, value):
        api_key, validators = self._utils.api_method_preprocessing(self)

        data = {
            'from': _from,
            'to': to,
            'data': data,
            'value': value
        }

        self._utils.validate_data(self._validators.api.klay.requests.estimate_gas, data)

        validators.update({200: self._validators.api.klay.responses.estimate_gas})

        return self._http.post(
            url='{}/estimate-gas'.format(self._coin_url),
            data=data,
            params=api_key,
            validators=validators
        )
