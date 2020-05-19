from typing import Callable

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
        self.get_block: Callable = validator(get_block)
        self.get_blocks: Callable = validator(get_blocks)
        self.get_transaction_by_hash: Callable = validator(get_transaction_by_hash)
        self.get_transactions: Callable = validator(get_transactions)
        self.send_transaction: Callable = validator(send_transaction)
        self.decode_transaction: Callable = validator(decode_transaction)
        self.get_outputs_by_addresses: Callable = validator(get_outputs_by_addresses)
        self.get_utxo_coin_addresses_info: Callable = validator(get_utxo_coin_addresses_info)
        self.get_utxo_coin_addresses_history: Callable = validator(get_utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications_params: Callable = validator(
            subscribe_to_addresses_notifications_params
        )
        self.subscribe_to_addresses_notifications_body: Callable = validator(
            subscribe_to_addresses_notifications_body
        )
        self.unsubscribe_from_addresses_notifications: Callable = validator(
            unsubscribe_from_addresses_notifications
        )
