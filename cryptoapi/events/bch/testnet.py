from typing import Any, Callable


class Testnet:

    def __init__(
        self, ws_wrapper: Callable, config: Any, validators: Any, utils: Any, api_key: str, debug: bool
    ) -> None:
        coin_prefix: str = 'bch'
        self._ws: Any = ws_wrapper(url=config.WS_TESTNET_URL + coin_prefix, api_key=api_key, debug=debug)
        self._validators: Any = validators
        self._utils: Any = utils

    @property
    def connected(self) -> bool:
        return self._ws._connected

    def connect(self) -> None:
        self._ws.connect()

    def disconnect(self) -> None:
        self._ws.disconnect()

    def on_block(self, callback: Callable, confirmations: int = 0) -> int:
        self._utils.validate_data(self._validators.confirmations, confirmations)
        return self._ws.on_event(['new_block', confirmations], callback,
                                 self._validators.notifications.utxo_transaction_notification)

    def on_address_transactions(self, address: str, callback: Callable, confirmations: int = 0) -> int:
        self._utils.validate_data(self._validators.address, address)
        self._utils.validate_data(self._validators.confirmations, confirmations)
        return self._ws.on_event(['new_transaction', address, confirmations], callback,
                                 self._validators.notifications.utxo_transaction_notification)

    def on_address_balance(self, address: str, callback: Callable, confirmations: int = 0) -> int:
        self._utils.validate_data(self._validators.address, address)
        self._utils.validate_data(self._validators.confirmations, confirmations)
        return self._ws.on_event(['new_balance', address, confirmations], callback,
                                 self._validators.notifications.balance_notification)

    def on_transaction_confirmations(self, _hash: str, callback: Callable, confirmations: int = 0) -> int:
        self._utils.validate_data(self._validators.hash, _hash)
        self._utils.validate_data(self._validators.confirmations, confirmations)
        return self._ws.on_event(['new_confirmation', _hash, confirmations], callback,
                                 self._validators.notifications.transaction_confirmation_notification)

    def on_connected(self, callback: Callable) -> None:
        if not callable(callback):
            raise Exception('Callback must be callable object')
        self._ws.on_connected_callbacks.append(callback)

    def on_disconnected(self, callback: Callable) -> None:
        if not callable(callback):
            raise Exception('Callback must be callable object')
        self._ws.on_disconnected_callbacks.append(callback)

    def unsubscribe(self, subscription_id: int) -> bool:
        self._utils.validate_data(self._validators.subscription_id, subscription_id)
        return self._ws.unsubscribe(subscription_id)
