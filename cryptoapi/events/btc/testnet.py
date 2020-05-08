class Testnet:

    def __init__(self, ws_wrapper, config, models, utils, api_key, debug):
        coin_prefix = 'btc'
        self._ws = ws_wrapper(url=config.events.WS_TESTNET_URL + coin_prefix, api_key=api_key, debug=debug)
        self._models = models
        self._utils = utils

    @property
    def connected(self):
        return self._ws._connected

    def connect(self):
        self._ws.connect()

    def disconnect(self):
        self._ws.disconnect()

    def on_block(self, callback, confirmations=0):
        self._utils.validate_data(self._models.events.confirmations, confirmations)
        return self._ws.on_event(['new_block',
                                  confirmations],
                                 callback,
                                 self._models.events.notifications.utxo_transaction_notification)

    def on_address_transactions(self, address, callback, confirmations=0):
        self._utils.validate_data(self._models.events.address, address)
        self._utils.validate_data(self._models.events.confirmations, confirmations)
        return self._ws.on_event(['new_transaction',
                                  address,
                                  confirmations],
                                 callback,
                                 self._models.events.notifications.utxo_transaction_notification)

    def on_address_balance(self, address, callback, confirmations=0):
        self._utils.validate_data(self._models.events.address, address)
        self._utils.validate_data(self._models.events.confirmations, confirmations)
        return self._ws.on_event(['new_balance',
                                  address,
                                  confirmations],
                                 callback,
                                 self._models.events.notifications.balance_notification)

    def on_transaction_confirmations(self, _hash, callback, confirmations=0):
        self._utils.validate_data(self._models.events.hash, _hash)
        self._utils.validate_data(self._models.events.confirmations, confirmations)
        return self._ws.on_event(['new_confirmation',
                                  _hash,
                                  confirmations],
                                 callback,
                                 self._models.events.notifications.transaction_confirmation_notification)

    def on_connected(self, callback):
        if not callable(callback):
            raise Exception('Callback must be callable object')
        self._ws.on_connected_callbacks.append(callback)

    def on_disconnected(self, callback):
        if not callable(callback):
            raise Exception('Callback must be callable object')
        self._ws.on_disconnected_callbacks.append(callback)

    def unsubscribe(self, subscription_id):
        self._utils.validate_data(self._models.events.subscription_id, subscription_id)
        return self._ws.unsubscribe(subscription_id)
