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

    def get_network_information(self):
        api_key, validators = api_method_preprocessing(self)

        validators.update({
            200: self._models.btc.responses.network_information
        })

        return self._http.get(
            url='/network',
            params=api_key,
            validators=validators
        )

    def get_estimate_fee(self, _from, to, data, value):
        api_key, validators = api_method_preprocessing(self)

        data = {
            'from': _from,
            'to': to,
            'data': data,
            'value': value
        }

        validate_data(
            self._models.btc.requests.estimate_fee,
            data
        )

        validators.update({
            200: self._models.btc.responses.estimate_fee
        })

        return self._http.post(
            url='/estimate-fee',
            data=data,
            params=api_key,
            validators=validators
        )
