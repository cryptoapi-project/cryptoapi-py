class PushNotifications:
    def __init__(
        self,
        http,
        models,
        debug,
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

    # def get_tokens(self, query=None, skip=None, limit=None, types=None):
    #     api_key, validators = self._prepare()

    #     params = {
    #     }

    #     if query is not None:
    #         params.update({'query': query})

    #     if skip is not None:
    #         params.update({'skip': skip})

    #     if limit is not None:
    #         params.update({'limit': limit})

    #     if types is not None:
    #         params.update({'types': ','.join(types)})

    #     self._models.eth.requests.get_tokens.validate(params)

    #     params.update(api_key)

    #     validators.update({
    #         200: self._models.eth.responses.get_tokens
    #     })

    #     return self._http.get(
    #         url='/tokens/search',
    #         params=params,
    #         validators=validators
    #     )