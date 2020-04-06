from cryptoapi.utils.api import api_method_preprocessing, validate_data


class Common:
    def __init__(
        self,
        http,
        models,
        api_key
    ):
        self._http = http
        self._api_key = api_key
        self._models = models

    def get_network_info(self):
        api_key, validators = api_method_preprocessing(self)

        validators.update({
            200: self._models.klay.responses.get_network_info
        })

        return self._http.get(
            url='/network',
            params=api_key,
            validators=validators
        )

    def estimate_gas(self, _from, to, data, value):
        api_key, validators = api_method_preprocessing(self)

        data = {
            'from': _from,
            'to': to,
            'data': data,
            'value': value
        }

        validate_data(
            self._models.klay.requests.estimate_gas,
            data
        )

        validators.update({
            200: self._models.klay.responses.estimate_gas
        })

        return self._http.post(
            url='/estimate-gas',
            data=data,
            params=api_key,
            validators=validators
        )
