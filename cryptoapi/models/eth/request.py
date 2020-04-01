regex_is_hex = "^[0-9a-fA-F]+"


schema_ETH_common_gas_request = {
    'from': {'type': 'string', 'regex': regex_is_hex},
    'to': {'type': 'string', 'regex': regex_is_hex},
    'data': {'type': 'string', 'regex': regex_is_hex},
    'value': {'type': 'string', 'regex': regex_is_hex}
}

get_block_information_by_block_number_or_hash = {
    'block_number_or_hash': {'type': ['string', 'integer']}
}

get_information_about_the_latest_blocks_with_pagination = {
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'}
}

get_transactions_by_addresses = {
    'addresses': {'required': True, 'type': 'string'},
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'},
    'positive': {'type': 'string'}
}

get_transaction_intersections_by_addresses = {
    'addresses': {'required': True, 'type': 'string'}
}
get_general_information_by_addresses = {
    'addresses': {'required': True, 'type': 'string'}
}

get_token_transfers_by_addresses = {
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'},
    'addresses': {'required': True, 'type': 'list', 'schema': {'type': 'string'}},
    'token': {'required': True, 'type': 'string'}
}

get_tokens_balances_by_holders = {
    'addresses': {'required': True, 'type': 'string'},
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'}
}

get_token_balance_by_holders_and_token = {
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'},
    'addresses': {'required': True, 'type': 'list', 'schema': {'type': 'string'}},
    'token': {'required': True, 'type': 'string'}
}

get_transactions_with_pagination = {
    'from': {'type': 'string', 'regex': regex_is_hex},
    'to': {'type': 'string', 'regex': regex_is_hex},
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'},
    'block_number': {'type': 'integer'}
}

get_transaction_information = {
    'hash': {'required': True, 'type': 'string', 'regex': regex_is_hex}
}

get_transaction_receipt = {
    'hash': {'required': True, 'type': 'string', 'regex': regex_is_hex}
}

send_transaction = {
    'tx': {'type': 'string', 'regex': regex_is_hex}
}

decode_transaction = {
    'tx': {'type': 'string', 'regex': regex_is_hex}
}

get_tokens = {
    'query': {'type': 'string', 'regex': regex_is_hex},
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'},
    'types': {'type': 'list', 'schema': {'type': 'string'}}
}

get_token_transfers_by_token_address = {
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'},
    'addresses': {'type': 'list', 'schema': {'type': 'string'}},
    'token': {'required': True, 'type': 'string'}
}

get_token_contract = {
    'address': {'required': True, 'type': 'list', 'schema': {'type': 'string'}},
}

subscribe_to_addresses_notifications = {
    'addresses': {'required': True, 'type': 'string'}
}

unsubscribe_from_addresses_notifications = {
    'addresses': {'required': True, 'type': 'string'},
    'firebase_token': {'required': True, 'type': 'string'}
}

get_contracts_logs = {
    'cursor': {'type': 'string'},
    'reversed_fetch': {'type': 'boolean'},
    'from_block': {'type': 'integer'},
    'to_block': {'type': 'integer'},
    'addresses': {'type': 'list', 'schema': {'type': 'string'}},
    'topics': {'type': 'list', 'schema': {'type': 'string'}}
}

contract_call = {
    'address': {'required': True, 'type': 'string'}
}

get_contract_general_information = {
    'address': {'required': True, 'type': 'string'}
}
