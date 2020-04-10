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
            200: self._models.bch.responses.get_network_information
        })

        return self._http.get(
            url='/network',
            params=api_key,
            validators=validators
        )

    def get_estimate_fee(self):
        api_key, validators = api_method_preprocessing(self)

        validators.update({
            200: self._models.bch.responses.get_estimate_fee
        })

        return self._http.get(
            url='/estimate-fee',
            params=api_key,
            validators=validators
        )
