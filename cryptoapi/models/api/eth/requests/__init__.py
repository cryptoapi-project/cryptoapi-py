from .schemes import (
    contract_call_body,
    contract_call_params,
    decode_transaction,
    estimate_gas,
    get_balances_by_addresses,
    get_block,
    get_blocks,
    get_contract_general_information,
    get_contracts_logs,
    get_general_information_by_addresses,
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
    subscribe_to_addresses_notifications_body,
    subscribe_to_addresses_notifications_params,
    unsubscribe_from_addresses_notifications
)


class Requests:

    def __init__(self, model_wrapper):
        self.estimate_gas = model_wrapper(estimate_gas)
        self.get_block = model_wrapper(get_block)
        self.get_blocks = model_wrapper(get_blocks)
        self.get_transactions_by_addresses = model_wrapper(get_transactions_by_addresses)
        self.get_transaction_intersections_by_addresses = model_wrapper(get_transaction_intersections_by_addresses)
        self.get_balances_by_addresses = model_wrapper(get_balances_by_addresses)
        self.get_general_information_by_addresses = model_wrapper(get_general_information_by_addresses)
        self.get_token_transfers_by_addresses = model_wrapper(get_token_transfers_by_addresses)
        self.get_tokens_balances_by_holders = model_wrapper(get_tokens_balances_by_holders)
        self.get_token_balance_by_holders_and_token = model_wrapper(get_token_balance_by_holders_and_token)
        self.get_transactions = model_wrapper(get_transactions)
        self.get_transaction_information = model_wrapper(get_transaction_information)
        self.get_transaction_receipt = model_wrapper(get_transaction_receipt)
        self.send_transaction = model_wrapper(send_transaction)
        self.decode_transaction = model_wrapper(decode_transaction)
        self.get_tokens = model_wrapper(get_tokens)
        self.get_token_transfers_by_token_address = model_wrapper(get_token_transfers_by_token_address)
        self.get_token_contract = model_wrapper(get_token_contract)
        self.subscribe_to_addresses_notifications_params = model_wrapper(
            subscribe_to_addresses_notifications_params
        )
        self.subscribe_to_addresses_notifications_body = model_wrapper(subscribe_to_addresses_notifications_body)
        self.unsubscribe_from_addresses_notifications = model_wrapper(unsubscribe_from_addresses_notifications)
        self.get_contracts_logs = model_wrapper(get_contracts_logs)
        self.contract_call_params = model_wrapper(contract_call_params)
        self.contract_call_body = model_wrapper(contract_call_body)
        self.get_contract_general_information = model_wrapper(get_contract_general_information)
