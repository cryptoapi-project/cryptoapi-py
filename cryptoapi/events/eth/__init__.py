class Eth:

    def __init__(
        self,
        ws_wrapper,
        config,
        debug,
        api_key
    ):
        coin_prefix = 'eth'
        self._ws = ws_wrapper(
            url=config.events.WS_BASE_URL + coin_prefix,
            api_key=api_key,
            debug=debug
        )

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
        return self._ws.on_event(
            ['new_transaction', address, confirmations],
            callback
        )

    def on_address_balance(self, address, callback, confirmations=0):
        return self._ws.on_event(
            ['new_balance', address, confirmations],
            callback
        )

    def on_token_transfers(self, token, address, callback, confirmations=0):
        return self._ws.on_event(
            ['new_transfer', token, address, confirmations],
            callback
        )

    def on_token_balance(self, token, address, callback, confirmations=0):
        return self._ws.on_event(
            ['new_token_balance', token, address, confirmations],
            callback
        )

    def on_contract_log(self, address, callback, confirmations=0, _from=None, to=None, topics=None):
        return self._ws.on_event(
            ['new_contract_log', address, confirmations, _from, to, topics],
            callback
        )

    def on_transaction_confirmations(self, _hash, confirmations, callback):
        return self._ws.on_event(
            ['new_confirmation', _hash, confirmations],
            callback
        )

    def on_connected(self, callback):
        self._ws.on_connected_callbacks.append(callback)

    def on_disconnected(self, callback):
        self._ws.on_disconnected_callbacks.append(callback)

    def unsubscribe(self, subscription_id):
        return self._ws.unsubscribe(subscription_id)
