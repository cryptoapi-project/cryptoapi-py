from typing import Callable

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

    def __init__(self, validator: Callable) -> None:
        self.eth_block_notification: Callable = validator(eth_block_notification)
        self.klay_block_notification: Callable = validator(klay_block_notification)
        self.address_subscription: Callable = validator(address_subscription)
        self.balance_notification: Callable = validator(balance_notification)
        self.eth_transaction_notification: Callable = validator(eth_transaction_notification)
        self.klay_transaction_notification: Callable = validator(klay_transaction_notification)
        self.token_subscription: Callable = validator(token_subscription)
        self.transfer_notification: Callable = validator(transfer_notification)
        self.token_balance_notification: Callable = validator(token_balance_notification)
        self.eth_contract_log_subscription: Callable = validator(eth_contract_log_subscription)
        self.eth_contract_log_notification: Callable = validator(eth_contract_log_notification)
        self.transaction_confirmation_subscription: Callable = validator(transaction_confirmation_subscription)
        self.transaction_confirmation_notification: Callable = validator(transaction_confirmation_notification)
        self.utxo_block_notification: Callable = validator(utxo_block_notification)
        self.utxo_transaction_notification: Callable = validator(utxo_transaction_notification)
