from typing import Any, Callable

from .schemes import (
    contract_call,
    decode_transaction,
    estimate_gas,
    get_balances_by_addresses,
    get_block,
    get_blocks,
    get_contract_general_information,
    get_contracts_logs,
    get_general_information_by_addresses,
    get_network_info,
    get_token_balance_by_holders_and_token,
    get_token_contract,
    get_token_transfers_by_addresses,
    get_token_transfers_by_token_address,
    get_tokens,
    get_tokens_balances_by_holders,
    get_transaction_information,
    get_transaction_intersections_by_addresses,
    get_transaction_receipt,
    get_transactions,
    get_transactions_by_addresses,
    send_transaction,
    subscribe_to_addresses_notifications
)


class Responses:

    def __init__(self, validator: Callable, utils: Any) -> None:
        self.get_network_info: Any = validator(get_network_info)
        self.estimate_gas: Any = validator(estimate_gas)
        self.get_block: Any = validator(get_block)
        self.get_blocks: Any = validator(get_blocks)
        self.get_transactions_by_addresses: Any = validator(get_transactions_by_addresses)
        self.get_transaction_intersections_by_addresses: Any = validator(
            get_transaction_intersections_by_addresses
        )
        self.get_balances_by_addresses: Any = validator(get_balances_by_addresses, True)
        self.get_general_information_by_addresses: Any = validator(get_general_information_by_addresses, True)
        self.get_token_transfers_by_addresses: Any = validator(get_token_transfers_by_addresses)
        self.get_tokens_balances_by_holders: Any = validator(get_tokens_balances_by_holders)
        self.get_token_balance_by_holders_and_token: Any = validator(get_token_balance_by_holders_and_token)
        self.get_transactions: Any = validator(get_transactions)
        self.get_transaction_information: Any = validator(get_transaction_information)
        self.get_transaction_receipt: Any = validator(get_transaction_receipt)
        self.send_transaction: Any = validator(send_transaction)
        self.decode_transaction: Any = validator(decode_transaction)
        self.get_tokens: Any = validator(get_tokens)
        self.get_token_transfers_by_token_address: Any = validator(get_token_transfers_by_token_address)
        self.get_token_contract: Any = validator(get_token_contract)
        self.subscribe_to_addresses_notifications: Any = validator(subscribe_to_addresses_notifications)
        self.get_contracts_logs: Any = validator(get_contracts_logs, True)
        self.contract_call: Any = validator(
            utils.custom_validator(contract_call,
                                   'Contract call result must be a string')
        )
        self.get_contract_general_information: Any = validator(get_contract_general_information)
