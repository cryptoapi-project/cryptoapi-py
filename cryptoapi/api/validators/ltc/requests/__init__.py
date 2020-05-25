from typing import Any

from .schemes import (
    decode_transaction, get_block, get_blocks, get_outputs_by_addresses, get_transaction_by_hash, get_transactions,
    get_utxo_coin_addresses_history, get_utxo_coin_addresses_info, send_transaction,
    subscribe_to_addresses_notifications_body, subscribe_to_addresses_notifications_params,
    unsubscribe_from_addresses_notifications
)


class Requests:

    def __init__(self, utils: Any) -> None:
        self.get_block: Any = utils.validator(get_block)
        self.get_blocks: Any = utils.validator(get_blocks)
        self.get_transaction_by_hash: Any = utils.validator(get_transaction_by_hash)
        self.get_transactions: Any = utils.validator(get_transactions)
        self.send_transaction: Any = utils.validator(send_transaction)
        self.decode_transaction: Any = utils.validator(decode_transaction)
        self.get_outputs_by_addresses: Any = utils.validator(get_outputs_by_addresses)
        self.get_utxo_coin_addresses_info: Any = utils.validator(get_utxo_coin_addresses_info)
        self.get_utxo_coin_addresses_history: Any = utils.validator(get_utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications_params: Any = utils.validator(
            subscribe_to_addresses_notifications_params
        )
        self.subscribe_to_addresses_notifications_body: Any = utils.validator(
            subscribe_to_addresses_notifications_body
        )
        self.unsubscribe_from_addresses_notifications: Any = utils.validator(
            unsubscribe_from_addresses_notifications
        )
