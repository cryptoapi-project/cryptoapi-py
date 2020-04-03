from cryptoapi.utils.models import hex_type_not_required, string_type_not_required, integer_type_not_required,\
    required_string_type, boolean_type_not_required


# ETH.Common
estimate_gas = {
    'from': hex_type_not_required,
    'to': hex_type_not_required,
    'data': hex_type_not_required,
    'value': hex_type_not_required
}

# ETH.Blocks
get_block = {
    'block_number_or_hash': {
        'type': ['string', 'integer'],
        'required': True
    }
}

get_blocks = {
    'skip': integer_type_not_required,
    'limit': integer_type_not_required
}

# ETH.Addresses
get_transactions_by_addresses = {
    'addresses': required_string_type,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
    'positive': string_type_not_required
}

get_transaction_intersections_by_addresses = {
    'addresses': required_string_type,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required
}

get_balances_by_addresses = {
    'addresses': required_string_type
}
get_general_information_by_addresses = {
    'addresses': required_string_type
}

get_token_transfers_by_addresses = {
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
    'addresses': {
        'required': True,
        'type': 'list',
        'schema': required_string_type
    },
    'token': required_string_type
}

get_tokens_balances_by_holders = {
    'addresses': required_string_type,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required
}

get_token_balance_by_holders_and_token = {
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
    'addresses': {
        'required': True,
        'type': 'list',
        'schema': required_string_type
    },
    'token': required_string_type
}

# ETH.Transactions
get_transactions = {
    'from': hex_type_not_required,
    'to': hex_type_not_required,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
    'block_number': integer_type_not_required
}

get_transaction_information = {
    'hash': hex_type_not_required
}

get_transaction_receipt = {
    'hash': hex_type_not_required
}

send_transaction = {
    'tx': hex_type_not_required
}

decode_transaction = {
    'tx': hex_type_not_required
}

# ETH.Tokens
get_tokens = {
    'query': string_type_not_required,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
    'types': {
        'type': 'list',
        'schema': string_type_not_required
    }
}

get_token_transfers_by_token_address = {
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
    'addresses': {
        'type': 'list',
        'schema': string_type_not_required
    },
    'token': required_string_type
}

get_token_contract = {
    'address': {
        'required': True,
        'type': 'list',
        'schema': required_string_type
    },
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
    'cursor': string_type_not_required,
    'reversed_fetch': boolean_type_not_required,
    'from_block': integer_type_not_required,
    'to_block': integer_type_not_required,
    'addresses': {
        'type': 'list',
        'schema': string_type_not_required
    },
    'topics': {
        'type': 'list',
        'schema': string_type_not_required
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
