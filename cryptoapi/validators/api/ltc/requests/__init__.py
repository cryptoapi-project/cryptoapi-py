from typing import Any, Callable

from .schemes import (
    decode_transaction,
    get_block,
    get_blocks,
    get_outputs_by_addresses,
    get_transaction_by_hash,
    get_transactions,
    get_utxo_coin_addresses_history,
    get_utxo_coin_addresses_info,
    send_transaction,
    subscribe_to_addresses_notifications_body,
    subscribe_to_addresses_notifications_params,
    unsubscribe_from_addresses_notifications
)


class Requests:

    def __init__(self, validator: Callable) -> None:
        self.get_block: Any = validator(get_block)
        self.get_blocks: Any = validator(get_blocks)
        self.get_transaction_by_hash: Any = validator(get_transaction_by_hash)
        self.get_transactions: Any = validator(get_transactions)
        self.send_transaction: Any = validator(send_transaction)
        self.decode_transaction: Any = validator(decode_transaction)
        self.get_outputs_by_addresses: Any = validator(get_outputs_by_addresses)
        self.get_utxo_coin_addresses_info: Any = validator(get_utxo_coin_addresses_info)
        self.get_utxo_coin_addresses_history: Any = validator(get_utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications_params: Any = validator(
            subscribe_to_addresses_notifications_params
        )
        self.subscribe_to_addresses_notifications_body: Any = validator(subscribe_to_addresses_notifications_body)
        self.unsubscribe_from_addresses_notifications: Any = validator(unsubscribe_from_addresses_notifications)
