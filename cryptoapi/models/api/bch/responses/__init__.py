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

    def __init__(self, model_wrapper, utils):
        self.get_network_information = model_wrapper(get_network_information)
        self.get_estimate_fee = model_wrapper(
            utils.custom_validator(get_estimate_fee,
                                   'Fee value must be a float')
        )
        self.get_block = model_wrapper(get_block)
        self.get_blocks = model_wrapper(get_blocks)
        self.get_transaction_by_hash = model_wrapper(get_transaction_by_hash)
        self.get_transactions = model_wrapper(get_transactions)
        self.send_transaction = model_wrapper(send_transaction)
        self.decode_transaction = model_wrapper(decode_transaction)
        self.get_outputs_by_addresses = model_wrapper(get_outputs_by_addresses, True)
        self.get_utxo_coin_addresses_info = model_wrapper(get_utxo_coin_addresses_info, True)
        self.get_utxo_coin_addresses_history = model_wrapper(get_utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications = model_wrapper(subscribe_to_addresses_notifications)
