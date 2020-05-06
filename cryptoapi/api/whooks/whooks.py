from cryptoapi.utils.api import api_method_preprocessing, validate_data


class Whooks:
    def __init__(
        self,
        http,
        models,
        api_key
    ):
        self._http = http
        self._api_key = api_key
        self._models = models

    def create_webhook(self, project_id, url, coin, is_subscribe_block, is_subscribe_transfer,
                       is_subscribe_transaction, transaction_addresses, transfer_triggers):
        api_key, validators = api_method_preprocessing(self)

        data = {
            'project_id': project_id,
            'url': url,
            'coin': coin,
            'is_subscribe_block': is_subscribe_block,
            'is_subscribe_transfer': is_subscribe_transfer,
            'is_subscribe_transaction': is_subscribe_transaction,
            'transaction_addresses': transaction_addresses,
            'transfer_triggers': transfer_triggers
        }

        validate_data(
            self._models.api.whooks.requests.create_webhook,
            data
        )

        validators.update({
            200: self._models.api.whooks.responses.create_webhook
        })

        return self._http.post(
            url='/web-hooks/create',
            data=data,
            params=api_key,
            validators=validators
        )

    def get_webhook(self, project_id):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'project_id': project_id
        }

        validate_data(
            self._models.api.whooks.requests.get_webhook,
            params
        )

        validators.update({
            200: self._models.api.whooks.responses.get_webhook
        })

        params.update(api_key)

        return self._http.get(
            url='/web-hooks/{}'.format(params['project_id']),
            params=params,
            validators=validators
        )

    def delete_webhook(self, _id):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'id': _id
        }

        validate_data(
            self._models.api.whooks.requests.delete_webhook,
            params
        )

        validators.update({
            200: self._models.api.whooks.responses.delete_webhook
        })

        params.update(api_key)

        return self._http.delete(
            url='/web-hooks/{}'.format(params['_id']),
            params=params,
            validators=validators
        )

    def change_webhook(self, project_id, url, coin, is_subscribe_block, is_subscribe_transfer,
                       is_subscribe_transaction, transaction_addresses, transfer_triggers, _id):
        api_key, validators = api_method_preprocessing(self)

        data = {
            'project_id': project_id,
            'url': url,
            'coin': coin,
            'is_subscribe_block': is_subscribe_block,
            'is_subscribe_transfer': is_subscribe_transfer,
            'is_subscribe_transaction': is_subscribe_transaction,
            'transaction_addresses': transaction_addresses,
            'transfer_triggers': transfer_triggers,
            'id': _id
        }

        validate_data(
            self._models.api.whooks.requests.change_webhook,
            data
        )

        validators.update({
            200: self._models.api.whooks.responses.change_webhook
        })

        return self._http.post(
            url='/web-hooks/change',
            data=data,
            params=api_key,
            validators=validators
        )

    def get_events(self, hook_id, start_id=None, end_id=None, only_failed=None, skip=None, limit=None, _type=None):
        api_key, validators = api_method_preprocessing(self)

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

        validate_data(
            self._models.api.whooks.requests.get_events,
            params
        )

        validators.update({
            200: self._models.api.whooks.responses.get_events
        })

        params.update(api_key)

        return self._http.get(
            url='/web-hooks/{}/events'.format(params['hook_id']),
            params=params,
            validators=validators
        )
