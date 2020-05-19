from typing import Any, Callable

from .schemes import (
    decode_transaction,
    get_block,
    get_blocks,
    get_estimate_fee,
    get_network_information,
    get_outputs_by_addresses,
    get_transaction_by_hash,
    get_transactions,
    get_utxo_coin_addresses_history,
    get_utxo_coin_addresses_info,
    send_transaction,
    subscribe_to_addresses_notifications
)


class Responses:

    def __init__(self, validator: Callable, utils: Any) -> None:
        self.get_network_information: Callable = validator(get_network_information)
        self.get_estimate_fee: Callable = validator(
            utils.custom_validator(get_estimate_fee,
                                   'Fee value must be a float')
        )
        self.get_block: Callable = validator(get_block)
        self.get_blocks: Callable = validator(get_blocks)
        self.get_transaction_by_hash: Callable = validator(get_transaction_by_hash)
        self.get_transactions: Callable = validator(get_transactions)
        self.send_transaction: Callable = validator(send_transaction)
        self.decode_transaction: Callable = validator(decode_transaction)
        self.get_outputs_by_addresses: Callable = validator(get_outputs_by_addresses, True)
        self.get_utxo_coin_addresses_info: Callable = validator(get_utxo_coin_addresses_info, True)
        self.get_utxo_coin_addresses_history: Callable = validator(get_utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications: Callable = validator(subscribe_to_addresses_notifications)
