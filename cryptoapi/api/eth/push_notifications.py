from cryptoapi.utils.api import api_method_preprocessing, validate_data


class PushNotifications:
    def __init__(
        self,
        http,
        models,
        api_key
    ):
        self._http = http
        self._api_key = api_key
        self._models = models

    def subscribe_to_addresses_notifications(self, addresses, firebase_token):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'addresses': ','.join(addresses)
        }

        data = {
            'firebase_token': firebase_token
        }

        validate_data(
            self._models.eth.requests.subscribe_to_addresses_notifications_params,
            params
        )
        validate_data(
            self._models.eth.requests.subscribe_to_addresses_notifications_body,
            data
        )

        validators.update({
            200: self._models.eth.responses.subscribe_to_addresses_notifications
        })

        return self._http.post(
            url='/push-notifications/addresses/{}/balance'.format(params['addresses']),
            data=data,
            params=api_key,
            validators=validators
        )

    def unsubscribe_from_addresses_notifications(self, addresses, firebase_token):
        api_key, validators = api_method_preprocessing(self)

        params = {
            'addresses': ','.join(addresses),
            'firebase_token': firebase_token
        }

        validate_data(
            self._models.eth.requests.unsubscribe_from_addresses_notifications,
            params
        )

        params.update(api_key)

        return self._http.delete(
            url='/push-notifications/addresses/{}/balance'.format(params['addresses']),
            params=params,
            validators=validators
        )
