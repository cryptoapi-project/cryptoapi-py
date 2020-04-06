from .schemes import get_block, get_blocks, get_transaction_by_hash, get_transactions, send_transaction, \
    decode_transaction, get_outputs_by_addresses, get_utxo_coin_addresses_info, get_utxo_coin_addresses_history, \
    subscribe_to_addresses_notifications_params, subscribe_to_addresses_notifications_body, \
    unsubscribe_from_addresses_notifications


class Requests:

    def __init__(self, model_wrapper):
        self.get_block = model_wrapper(get_block)
        self.get_blocks = model_wrapper(get_blocks)
        self.get_transaction_by_hash = model_wrapper(get_transaction_by_hash)
        self.get_transactions = model_wrapper(get_transactions)
        self.send_transaction = model_wrapper(send_transaction)
        self.decode_transaction = model_wrapper(decode_transaction)
        self.get_outputs_by_addresses = model_wrapper(get_outputs_by_addresses)
        self.get_utxo_coin_addresses_info = model_wrapper(get_utxo_coin_addresses_info)
        self.get_utxo_coin_addresses_history = model_wrapper(get_utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications_params = model_wrapper(
            subscribe_to_addresses_notifications_params)
        self.subscribe_to_addresses_notifications_body = model_wrapper(subscribe_to_addresses_notifications_body)
        self.unsubscribe_from_addresses_notifications = model_wrapper(unsubscribe_from_addresses_notifications)
