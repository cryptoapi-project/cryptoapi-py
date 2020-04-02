from cryptoapi.models.utils import regex_is_hex, hex_type, string_type, integer_type, required_string_type, boolean_type


# ETH.Common
estimate_gas = {
    'from': hex_type,
    'to': hex_type,
    'data': hex_type,
    'value': hex_type
}

# ETH.Blocks
get_block_information_by_block_number_or_hash = {
    'block_number_or_hash': {'type': ['string', 'integer']}
}

get_information_about_the_latest_blocks_with_pagination = {
    'skip': integer_type,
    'limit': integer_type
}

# ETH.Addresses
get_transactions_by_addresses = {
    'addresses': required_string_type,
    'skip': integer_type,
    'limit': integer_type,
    'positive': string_type
}

get_transaction_intersections_by_addresses = {
    'addresses': required_string_type,
    'skip': integer_type,
    'limit': integer_type
}

get_balances_by_addresses = {
    'addresses': required_string_type
}
get_general_information_by_addresses = {
    'addresses': required_string_type
}

get_token_transfers_by_addresses = {
    'skip': integer_type,
    'limit': integer_type,
    'addresses': {
        'required': True,
        'type': 'list',
        'schema': string_type},
    'token': required_string_type
}

get_tokens_balances_by_holders = {
    'addresses': required_string_type,
    'skip': integer_type,
    'limit': integer_type
}

get_token_balance_by_holders_and_token = {
    'skip': integer_type,
    'limit': integer_type,
    'addresses': {
        'required': True,
        'type': 'list',
        'schema': string_type},
    'token': required_string_type
}

# ETH.Transactions
get_transactions_with_pagination = {
    'from': string_type,
    'to': string_type,
    'skip': integer_type,
    'limit': integer_type,
    'block_number': integer_type
}

get_transaction_information = {
    'hash': required_string_type
}

get_transaction_receipt = {
    'hash': required_string_type
}

send_transaction = {
    'tx': required_string_type
}

decode_transaction = {
    'tx': required_string_type
}

# ETH.Tokens
get_tokens = {
    'query': string_type,
    'skip': integer_type,
    'limit': integer_type,
    'types': {
        'type': 'list',
        'schema': string_type
    }
}

get_token_transfers_by_token_address = {
    'skip': integer_type,
    'limit': integer_type,
    'addresses': {
        'type': 'list',
        'schema': string_type
    },
    'token': required_string_type
}

get_token_contract = {
    'address': required_string_type
}

# ETH.Push Notifications
subscribe_to_addresses_notifications_params = {
    'addresses': required_string_type
}

subscribe_to_addresses_notifications_body = {
    'firebase_token': required_string_type
}

unsubscribe_from_addresses_notifications = {
    'addresses': required_string_type,
    'firebase_token': required_string_type
}

# ETH.Contracts
get_contracts_logs = {
    'cursor': string_type,
    'reversed_fetch': boolean_type,
    'from_block': integer_type,
    'to_block': integer_type,
    'addresses': {
        'type': 'list',
        'schema': string_type
    },
    'topics': {
        'type': 'list',
        'schema': string_type
    }
}

contract_call_params = {
    'address': required_string_type
}

contract_call_body = {
    'sender': required_string_type,
    'amount': required_string_type,
    'bytecode': required_string_type
}

get_contract_general_information = {
    'address': required_string_type
}
