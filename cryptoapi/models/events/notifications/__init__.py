from .schemes import (
    address_subscription,
    balance_notification,
    eth_block_notification,
    eth_contract_log_notification,
    eth_contract_log_subscription,
    eth_transaction_notification,
    klay_block_notification,
    klay_transaction_notification,
    token_balance_notification,
    token_subscription,
    transaction_confirmation_notification,
    transaction_confirmation_subscription,
    transfer_notification,
    utxo_block_notification,
    utxo_transaction_notification
)


class Notifications:

    def __init__(self, model_wrapper):
        self.eth_block_notification = model_wrapper(eth_block_notification)
        self.klay_block_notification = model_wrapper(klay_block_notification)
        self.address_subscription = model_wrapper(address_subscription)
        self.balance_notification = model_wrapper(balance_notification)
        self.eth_transaction_notification = model_wrapper(eth_transaction_notification)
        self.klay_transaction_notification = model_wrapper(klay_transaction_notification)
        self.token_subscription = model_wrapper(token_subscription)
        self.transfer_notification = model_wrapper(transfer_notification)
        self.token_balance_notification = model_wrapper(token_balance_notification)
        self.eth_contract_log_subscription = model_wrapper(eth_contract_log_subscription)
        self.eth_contract_log_notification = model_wrapper(eth_contract_log_notification)
        self.transaction_confirmation_subscription = model_wrapper(transaction_confirmation_subscription)
        self.transaction_confirmation_notification = model_wrapper(transaction_confirmation_notification)
        self.utxo_block_notification = model_wrapper(utxo_block_notification)
        self.utxo_transaction_notification = model_wrapper(utxo_transaction_notification)
