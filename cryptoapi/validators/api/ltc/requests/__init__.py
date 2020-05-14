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

    def __init__(self, validator):
        self.get_block = validator(get_block)
        self.get_blocks = validator(get_blocks)
        self.get_transaction_by_hash = validator(get_transaction_by_hash)
        self.get_transactions = validator(get_transactions)
        self.send_transaction = validator(send_transaction)
        self.decode_transaction = validator(decode_transaction)
        self.get_outputs_by_addresses = validator(get_outputs_by_addresses)
        self.get_utxo_coin_addresses_info = validator(get_utxo_coin_addresses_info)
        self.get_utxo_coin_addresses_history = validator(get_utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications_params = validator(subscribe_to_addresses_notifications_params)
        self.subscribe_to_addresses_notifications_body = validator(subscribe_to_addresses_notifications_body)
        self.unsubscribe_from_addresses_notifications = validator(unsubscribe_from_addresses_notifications)
