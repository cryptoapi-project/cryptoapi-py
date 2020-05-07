class Whooks:

    def __init__(
        self,
        http_wrapper,
        models,
        config,
        utils,
        debug,
        api_key
    ):
        self._http = http_wrapper(
            url=config.api.BASE_WEB_HOOKS_URL,
            debug=debug
        )
        self._api_key = api_key
        self._models = models
        self._utils = utils

    def get_hook_events(self, hook_id, start_id=None, end_id=None,
                        only_failed=None, skip=None, limit=None, _type=None):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'hook_id': hook_id
        }

        if start_id is not None:
            params.update({'start_id': start_id})

        if end_id is not None:
            params.update({'end_id': end_id})

        if only_failed is not None:
            params.update({'only_failed': only_failed})

        if limit is not None:
            params.update({'limit': limit})

        if skip is not None:
            params.update({'skip': skip})

        if _type is not None:
            params.update({'type': _type})

        self._utils.validate_data(
            self._models.api.whooks.requests.get_hook_events,
            params
        )

        validators.update({
            200: self._models.api.whooks.responses.get_hook_events
        })

        params.update(api_key)

        return self._http.get(
            url='/web-hooks/{}/events'.format(params.pop('hook_id')),
            params=params,
            validators=validators
        )
