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

    def _prepare(self):
        if not self._api_key:
            raise Exception('api_key exception')

        validators = {
            401: self._models.error,
            422: self._models.error
        }

        return {'token': self._api_key}, validators

    def get_network_info(self):
        api_key, validators = self._prepare()

        validators.update({
            200: self._models.eth.responses.get_network_info
        })

        return self._http.get(
            url='/network',
            params=api_key,
            validators=validators
        )

    def estimate_gas(self, _from, to, data, value):
        api_key, validators = self._prepare()

        data = {
            'from': _from,
            'to': to,
            'data': data,
            'value': value
        }
        self._models.eth.requests.estimate_gas.validate(data)

        validators.update({
            200: self._models.eth.responses.estimate_gas
        })

        return self._http.post(
            url='/estimate-gas',
            data=data,
            params=api_key,
            validators=validators
        )
