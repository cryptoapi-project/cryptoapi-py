from cryptoapi.utils.api import validate_data


class Testnet:

    def __init__(
        self,
        ws_wrapper,
        config,
        models,
        api_key,
        debug
    ):
        coin_prefix = 'btc'
        self._ws = ws_wrapper(
            url=config.events.WS_TESTNET_URL + coin_prefix,
            api_key=api_key,
            debug=debug
        )
        self._models = models

    @property
    def connected(self):
        return self._ws._connected

    def connect(self):
        self._ws.connect()

    def disconnect(self):
        self._ws.disconnect()

    def on_block(self, callback, confirmations=0):
        return self._ws.on_event(
            ['new_block', confirmations],
            callback
        )

    def on_address_transactions(self, address, callback, confirmations=0):
        validate_data(
            self._models.is_integer,
            confirmations
        )
        validate_data(
            self._models.is_string,
            address
        )
        return self._ws.on_event(
            ['new_transaction', address, confirmations],
            callback
        )

    def on_address_balance(self, address, callback, confirmations=0):
        validate_data(
            self._models.is_integer,
            confirmations
        )
        validate_data(
            self._models.is_string,
            address
        )
        return self._ws.on_event(
            ['new_balance', address, confirmations],
            callback
        )

    def on_transaction_confirmations(self, _hash, confirmations, callback):
        validate_data(
            self._models.is_integer,
            confirmations
        )
        validate_data(
            self._models.is_string,
            _hash
        )
        return self._ws.on_event(
            ['new_confirmation', _hash, confirmations],
            callback
        )

    def on_connected(self, callback):
        if not callable(callback):
            raise Exception('Callback must be callable object')
        self._ws.on_connected_callbacks.append(callback)

    def on_disconnected(self, callback):
        if not callable(callback):
            raise Exception('Callback must be callable object')
        self._ws.on_disconnected_callbacks.append(callback)

    def unsubscribe(self, subscription_id):
        validate_data(
            self._models.is_integer,
            subscription_id
        )
        return self._ws.unsubscribe(subscription_id)
