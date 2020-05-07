class Common:
    def __init__(
        self,
        http,
        models,
        utils,
        api_key
    ):
        self._http = http
        self._api_key = api_key
        self._models = models
        self._utils = utils

    def get_network_info(self):
        api_key, validators = self._utils.api_method_preprocessing(self)

        validators.update({
            200: self._models.api.klay.responses.get_network_info
        })

        return self._http.get(
            url='/network',
            params=api_key,
            validators=validators
        )

    def estimate_gas(self, _from, to, data, value):
        api_key, validators = self._utils.api_method_preprocessing(self)

        data = {
            'from': _from,
            'to': to,
            'data': data,
            'value': value
        }

        self._utils.validate_data(
            self._models.api.klay.requests.estimate_gas,
            data
        )

        validators.update({
            200: self._models.api.klay.responses.estimate_gas
        })

        return self._http.post(
            url='/estimate-gas',
            data=data,
            params=api_key,
            validators=validators
        )
