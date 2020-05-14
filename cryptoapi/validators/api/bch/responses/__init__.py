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

    def __init__(self, validator, utils):
        self.get_network_information = validator(get_network_information)
        self.get_estimate_fee = validator(utils.custom_validator(get_estimate_fee, 'Fee value must be a float'))
        self.get_block = validator(get_block)
        self.get_blocks = validator(get_blocks)
        self.get_transaction_by_hash = validator(get_transaction_by_hash)
        self.get_transactions = validator(get_transactions)
        self.send_transaction = validator(send_transaction)
        self.decode_transaction = validator(decode_transaction)
        self.get_outputs_by_addresses = validator(get_outputs_by_addresses, True)
        self.get_utxo_coin_addresses_info = validator(get_utxo_coin_addresses_info, True)
        self.get_utxo_coin_addresses_history = validator(get_utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications = validator(subscribe_to_addresses_notifications)
