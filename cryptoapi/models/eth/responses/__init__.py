from .schemes import get_network_information, estimate_gas, get_block_information_by_block_number_or_hash, \
    get_information_about_the_latest_blocks_with_pagination, get_transactions_by_addresses, \
    get_balances_by_addresses, get_transaction_intersections_by_addresses, get_general_information_by_addresses, \
    get_token_transfers_by_addresses, get_tokens_balances_by_holders, \
    get_token_balance_by_holders_and_token, get_transactions_with_pagination, \
    get_transaction_information, get_transaction_receipt, send_transaction, \
    decode_transaction, get_tokens, get_token_transfers_by_token_address, get_token_contract, \
    subscribe_to_addresses_notifications, unsubscribe_from_addresses_notifications, get_contracts_logs, \
    contract_call, get_contract_general_information


class Responses:

    def __init__(self, model_wrapper):
        self.get_network_information = model_wrapper(get_network_information)
        self.estimate_gas = model_wrapper(estimate_gas)
        self.get_block_information_by_block_number_or_hash = model_wrapper(
            get_block_information_by_block_number_or_hash)
        self.get_information_about_the_latest_blocks_with_pagination = model_wrapper(
            get_information_about_the_latest_blocks_with_pagination)
        self.get_transactions_by_addresses = model_wrapper(get_transactions_by_addresses)
        self.get_transaction_intersections_by_addresses = model_wrapper(get_transaction_intersections_by_addresses)
        self.get_balances_by_addresses = model_wrapper(get_balances_by_addresses)
        self.get_general_information_by_addresses = model_wrapper(get_general_information_by_addresses)
        self.get_token_transfers_by_addresses = model_wrapper(get_token_transfers_by_addresses)
        self.get_tokens_balances_by_holders = model_wrapper(get_tokens_balances_by_holders)
        self.get_token_balance_by_holders_and_token = model_wrapper(get_token_balance_by_holders_and_token)
        self.get_transactions_with_pagination = model_wrapper(get_transactions_with_pagination)
        self.get_transaction_information = model_wrapper(get_transaction_information)
        self.get_transaction_receipt = model_wrapper(get_transaction_receipt)
        self.send_transaction = model_wrapper(send_transaction)
        self.decode_transaction = model_wrapper(decode_transaction)
        self.get_tokens = model_wrapper(get_tokens)
        self.get_token_transfers_by_token_address = model_wrapper(get_token_transfers_by_token_address)
        self.get_token_contract = model_wrapper(get_token_contract)
        self.subscribe_to_addresses_notifications = model_wrapper(subscribe_to_addresses_notifications)
        self.unsubscribe_from_addresses_notifications = model_wrapper(unsubscribe_from_addresses_notifications)
        self.get_contracts_logs = model_wrapper(get_contracts_logs)
        self.contract_call = model_wrapper(contract_call)
        self.get_contract_general_information = model_wrapper(get_contract_general_information)
