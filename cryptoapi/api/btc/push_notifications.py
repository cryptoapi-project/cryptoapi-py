from typing import Any, Dict, List, Optional, Union

error_static_type = Dict[str, Union[List[Dict[str, str]], int]]


class PushNotifications:

    def __init__(self, http: Any, coin_url: str, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._coin_url: str = coin_url
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def subscribe_to_addresses_notifications(self, addresses: str, firebase_token: str) -> Dict[str, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, str] = {
            'addresses': addresses
        }

        data: Dict[str, str] = {
            'firebase_token': firebase_token
        }

        self._utils.validate_data(
            self._validators.btc.requests.subscribe_to_addresses_notifications_params, params
        )
        self._utils.validate_data(self._validators.btc.requests.subscribe_to_addresses_notifications_body, data)

        validators.update({200: self._validators.btc.responses.subscribe_to_addresses_notifications})

        return self._http.post(
            url='{}/push-notifications/addresses/{}/balance'.format(
                self._coin_url, ','.join(params.pop('addresses'))
            ),
            data=data,
            params=api_key,
            validators=validators
        )

    def unsubscribe_from_addresses_notifications(self, addresses: str,
                                                 firebase_token: str) -> Optional[error_static_type]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, str] = {
            'addresses': addresses,
            'firebase_token': firebase_token
        }

        self._utils.validate_data(self._validators.btc.requests.unsubscribe_from_addresses_notifications, params)

        params.update(api_key)

        return self._http.delete(
            url='{}/push-notifications/addresses/{}/balance'.format(
                self._coin_url, ','.join(params.pop('addresses'))
            ),
            params=params,
            validators=validators
        )
