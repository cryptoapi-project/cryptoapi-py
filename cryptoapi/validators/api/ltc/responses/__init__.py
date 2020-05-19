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
        self.get_network_information: Any = validator(get_network_information)
        self.get_estimate_fee: Any = validator(
            utils.custom_validator(get_estimate_fee,
                                   'Fee value must be a float')
        )
        self.get_block: Any = validator(get_block)
        self.get_blocks: Any = validator(get_blocks)
        self.get_transaction_by_hash: Any = validator(get_transaction_by_hash)
        self.get_transactions: Any = validator(get_transactions)
        self.send_transaction: Any = validator(send_transaction)
        self.decode_transaction: Any = validator(decode_transaction)
        self.get_outputs_by_addresses: Any = validator(get_outputs_by_addresses, True)
        self.get_utxo_coin_addresses_info: Any = validator(get_utxo_coin_addresses_info, True)
        self.get_utxo_coin_addresses_history: Any = validator(get_utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications: Any = validator(subscribe_to_addresses_notifications)
