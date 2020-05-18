class PushNotifications:

    def __init__(self, http, coin_url, validators, utils, api_key):
        self._http = http
        self._coin_url = coin_url
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

    def subscribe_to_addresses_notifications(self, addresses, firebase_token):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'addresses': addresses
        }

        data = {
            'firebase_token': firebase_token
        }

        self._utils.validate_data(
            self._validators.api.btc.requests.subscribe_to_addresses_notifications_params,
            params
        )
        self._utils.validate_data(
            self._validators.api.btc.requests.subscribe_to_addresses_notifications_body,
            data
        )

        validators.update({200: self._validators.api.btc.responses.subscribe_to_addresses_notifications})

        return self._http.post(
            url='{}/push-notifications/addresses/{}/balance'.format(
                self._coin_url,
                ','.join(params.pop('addresses'))
            ),
            data=data,
            params=api_key,
            validators=validators
        )

    def unsubscribe_from_addresses_notifications(self, addresses, firebase_token):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'addresses': addresses,
            'firebase_token': firebase_token
        }

        self._utils.validate_data(
            self._validators.api.btc.requests.unsubscribe_from_addresses_notifications,
            params
        )

        params.update(api_key)

        return self._http.delete(
            url='{}/push-notifications/addresses/{}/balance'.format(
                self._coin_url,
                ','.join(params.pop('addresses'))
            ),
            params=params,
            validators=validators
        )
