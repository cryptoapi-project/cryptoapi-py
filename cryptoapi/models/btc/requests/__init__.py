from .schemes import block_by_height_or_hash, blocks, transaction_by_hash, transactions, send_transaction, \
    decode_transaction, outputs_by_addresses, utxo_coin_addresses_info, utxo_coin_addresses_history, \
    subscribe_to_addresses_notifications_params, subscribe_to_addresses_notifications_body, \
    unsubscribe_from_addresses_notifications


class Requests:

    def __init__(self, model_wrapper):
        self.block_by_height_or_hash = model_wrapper(block_by_height_or_hash)
        self.blocks = model_wrapper(blocks)
        self.transaction_by_hash = model_wrapper(transaction_by_hash)
        self.transactions = model_wrapper(transactions)
        self.send_transaction = model_wrapper(send_transaction)
        self.decode_transaction = model_wrapper(decode_transaction)
        self.outputs_by_addresses = model_wrapper(outputs_by_addresses)
        self.utxo_coin_addresses_info = model_wrapper(utxo_coin_addresses_info)
        self.utxo_coin_addresses_history = model_wrapper(utxo_coin_addresses_history)
        self.subscribe_to_addresses_notifications_params = model_wrapper(
            subscribe_to_addresses_notifications_params)
        self.subscribe_to_addresses_notifications_body = model_wrapper(subscribe_to_addresses_notifications_body)
        self.unsubscribe_from_addresses_notifications = model_wrapper(unsubscribe_from_addresses_notifications)
