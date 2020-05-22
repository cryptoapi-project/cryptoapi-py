from typing import Any

from .schemes import (
    address_subscription, balance_notification, eth_block_notification, eth_contract_log_notification,
    eth_contract_log_subscription, eth_transaction_notification, klay_block_notification,
    klay_transaction_notification, token_balance_notification, token_subscription,
    transaction_confirmation_notification, transaction_confirmation_subscription, transfer_notification,
    utxo_block_notification, utxo_transaction_notification
)


class Notifications:

    def __init__(self, utils: Any) -> None:
        self.eth_block_notification: Any = utils.validator(eth_block_notification)
        self.klay_block_notification: Any = utils.validator(klay_block_notification)
        self.address_subscription: Any = utils.validator(address_subscription)
        self.balance_notification: Any = utils.validator(balance_notification)
        self.eth_transaction_notification: Any = utils.validator(eth_transaction_notification)
        self.klay_transaction_notification: Any = utils.validator(klay_transaction_notification)
        self.token_subscription: Any = utils.validator(token_subscription)
        self.transfer_notification: Any = utils.validator(transfer_notification)
        self.token_balance_notification: Any = utils.validator(token_balance_notification)
        self.eth_contract_log_subscription: Any = utils.validator(eth_contract_log_subscription)
        self.eth_contract_log_notification: Any = utils.validator(eth_contract_log_notification)
        self.transaction_confirmation_subscription: Any = utils.validator(transaction_confirmation_subscription)
        self.transaction_confirmation_notification: Any = utils.validator(transaction_confirmation_notification)
        self.utxo_block_notification: Any = utils.validator(utxo_block_notification)
        self.utxo_transaction_notification: Any = utils.validator(utxo_transaction_notification)
