
regex_is_hex = '^[0-9a-fA-F]+'
regex_utc = '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]*Z$'

schema_ETH_common_network = {
    'last_block': {'type': 'integer'},
    'count_transactions': {'type': 'string'},
    'gas_price': {'type': 'string'},
    'hashrate': {'type': 'integer'},
    'difficulty': {'type': 'integer'}
}

schema_ETH_common_gas = {
    'estimate_gas': {'type': 'string'},
    'gas_price': {'type': 'string'},
    'nonce': {'type': 'string'}
}

schema_block_item = {
    'size': {'type': 'integer'},
    'difficulty': {'type': 'integer'},
    'total_difficulty': {'type': 'string'},
    'uncles': {'type': 'list'},
    'number': {'type': 'integer'},
    'hash': {'type': 'string', 'regex': regex_is_hex},
    'parent_hash': {'type': 'string', 'regex': regex_is_hex},
    'nonce': {'type': 'string', 'regex': regex_is_hex},
    'sha3_uncles': {'type': 'string', 'regex': regex_is_hex},
    'logs_bloom': {'type': 'string', 'regex': regex_is_hex},
    'transaction_root': {'type': 'string', 'regex': regex_is_hex},
    'state_root': {'type': 'string', 'regex': regex_is_hex},
    'receipts_root': {'type': 'string', 'regex': regex_is_hex},
    'miner': {'type': 'string', 'regex': regex_is_hex},
    'mix_hash': {'type': 'string', 'regex': regex_is_hex},
    'extra_data': {'type': 'string', 'regex': regex_is_hex},
    'gas_limit': {'type': 'string'},
    'gas_used': {'type': 'integer'},
    'utc': {'type': 'string', 'regex': regex_utc},
    'reward': {'type': 'string'},
    'uncle_rewards': {'type': 'list'},
    'count_transactions': {'type': 'integer'}
}

schema_ETH_block_ = {
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'},
    'count': {'type': 'integer'},
    'items': {'type': 'list', 'schema': {'type': 'dict', 'schema': schema_block_item}}
}

schema_transfer_item = {
    'block_number': {'type': 'integer'},
    'utc': {'type': 'string', 'regex': regex_utc},
    'from': {'type': 'string', 'regex': regex_is_hex},
    'gas': {'type': 'integer'},
    'hash': {'type': 'string', 'regex': regex_is_hex},
    'to': {'type': 'string', 'regex': regex_is_hex},
    'value': {'type': 'string'},
    'gas_price': {'type': 'string'},
    'integer': {'type': 'boolean'}
}

schema_ETH_addresses_transfer = {
    'addresses': {'type': 'list', 'schema': {'type': 'string', 'regex': regex_is_hex}},
    'skip': {'type': 'string'},
    'limit': {'type': 'integer'},
    'items': {'type': 'list', 'schema': {'type': 'dict', 'schema': schema_transfer_item}},
    'count': {'type': 'integer'}
}

schema_internal_transactions = {
    'to': {'type': 'string', 'regex': regex_is_hex},
    'from': {'type': 'string', 'regex': regex_is_hex},
    'value': {'type': 'string'},
    'input': {'type': 'string', 'regex': regex_is_hex},
    'is_suicide': {'type': 'boolean'},
    'type': {'type': 'string'}
}

schema_transactions_item = {
    'block_hash': {'type': 'string', 'regex': regex_is_hex},
    'block_number': {'type': 'integer'},
    'utc': {'type': 'string', 'regex': regex_utc},
    'from': {'type': 'string', 'regex': regex_is_hex},
    'gas': {'type': 'integer'},
    'gas_price': {'type': 'string'},
    'hash': {'type': 'string', 'regex': regex_is_hex},
    'input': {'type': 'string', 'regex': regex_is_hex},
    'nonce': {'type': 'integer'},
    'to': {'type': 'string', 'regex': regex_is_hex},
    'transaction_index': {'type': 'integer'},
    'value': {'type': 'string'},
    'v': {'type': 'string', 'regex': regex_is_hex},
    's': {'type': 'string', 'regex': regex_is_hex},
    'r': {'type': 'string', 'regex': regex_is_hex},
    'internal_transactions': {'type': 'list', 'schema': {'type': 'dict', 'schema': schema_internal_transactions}}
}


schema_ETH_addresses_transactions = {
    'addresses': {'type': 'list', 'schema': {'type': 'string', 'regex': regex_is_hex}},
    'skip': {'type': 'string'},
    'limit': {'type': 'integer'},
    'items': {'type': 'list', 'schema': {'type': 'dict', 'schema': schema_transactions_item}},
    'count': {'type': 'integer'}
}

schema_ETH_addresses_balance = {
    'address': {'type': 'string', 'regex': regex_is_hex},
    'balance': {'type': 'string'},
}

schema_ETH_addresses_address = {
    'address': {'type': 'string', 'regex': regex_is_hex},
    'balance': {'type': 'string'},
    'is_contract': {'type': 'boolean'},
    'type': {'type': 'string'},
    'count_transactions': {'type': 'integer'}
}

schema_token_item = {
    'type': {'type': 'string'},
    'execute_address': {'type': 'string', 'regex': regex_is_hex},
    'from': {'type': 'string', 'regex': regex_is_hex},
    'type': {'type': 'string', 'regex': regex_is_hex},
    'value': {'type': 'string', 'regex': regex_is_hex},
    'address': {'type': 'string', 'regex': regex_is_hex},
    'block_number': {'type': 'integer'},
    'transaction_hash': {'type': 'string', 'regex': regex_is_hex},
    'transaction_index': {'type': 'integer'},
    'log_index': {'type': 'integer'},
    'utc': {'type': 'string', 'regex': regex_utc},
}

schema_ETH_addresses_transfer_token = {
    'addresses': {'type': 'list', 'schema': {'type': 'string', 'regex': regex_is_hex}},
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'},
    'items': {'type': 'list', 'schema': {'type': 'dict', 'schema': schema_token_item}},
    'count': {'type': 'integer'}
}

schema_balance_token_item = {
    'addresses': {'type': 'string', 'regex': regex_is_hex},
    'holder': {'type': 'string', 'regex': regex_is_hex},
    'balance': {'type': 'string'}
}

schema_ETH_addresses_balance_token = {
    'count': {'type': 'integer'},
    'items': {'type': 'list', 'schema': {'type': 'dict', 'schema': schema_balance_token_item}},
}

schema_ETH_transactions_transactions = {
    'items': {'type': 'list', 'schema': {'type': 'dict', 'schema': schema_transactions_item}},
    'count': {'type': 'integer'}
}

schema_receipt_logs = {
    'address': {'type': 'string', 'regex': regex_is_hex},
    'data': {'type': 'string', 'regex': regex_is_hex},
    'topics': {'type': 'list', 'schema': {'type': 'string', 'regex': regex_is_hex}},
    'log_index': {'type': 'integer'},
    'transaction_hash': {'type': 'string', 'regex': regex_is_hex},
    'transaction_index': {'type': 'integer'},
    'block_hash': {'type': 'string', 'regex': regex_is_hex},
    'block_number': {'type': 'integer'},
    'id': {'type': 'string'}
}

schema_receipt = {
    'contract_address': {'type': 'string', 'nullable': True},
    'cumulative_gas_used': {'type': 'integer'},
    'gas_used': {'type': 'integer'},
    'status': {'type': 'boolean'},
    'logs': {'type': 'list', 'schema': {'type': 'dict', 'schema': schema_receipt_logs}},
}

schema_ETH_transactions_hash = {
    'receipt': schema_receipt
}
schema_ETH_transactions_hash.update(schema_transactions_item)

schema_ETH_transactions_receipt = {
    'block_hash': {'type': 'string', 'regex': regex_is_hex},
    'block_number': {'type': 'integer'},
    'from': {'type': 'string', 'regex': regex_is_hex},
    'hash': {'type': 'string', 'regex': regex_is_hex},
    'to': {'type': 'string', 'regex': regex_is_hex},
    'transaction_index': {'type': 'integer'}
}
schema_ETH_transactions_receipt.update(schema_receipt)

schema_ETH_transactions_send = {
    'hash': {'type': 'string', 'regex': regex_is_hex},
}

schema_ETH_transactions_decode = {
    'nonce': {'type': 'integer'},
    'gas_price': {'type': 'string'},
    'gas_limit': {'type': 'string'},
    'to': {'type': 'string'},
    'data': {'type': 'string', 'regex': regex_is_hex},
    'v': {'type': 'integer'},
    'r': {'type': 'string', 'regex': regex_is_hex},
    's': {'type': 'string', 'regex': regex_is_hex}
}

_tokens_items = {
    'total_supply': {'type': 'string'},
    'symbol': {'type': 'string'},
    'decimals': {'type': 'string'},
    'name': {'type': 'string'},
}

_get_tokens_items = {
    'info': {'type': 'dict', 'schema': _tokens_items},
    'address': {'type': 'string', 'regex': regex_is_hex},
    'create_transaction_hash': {'type': 'string', 'regex': regex_is_hex},
    'type': {'type': 'string'},
    'status': {'type': 'integer'},
}

get_tokens = {
    'query': {'type': 'string', 'nullable': True},
    'skip': {'type': 'integer'},
    'limit': {'type': 'integer'},
    'count': {'type': 'integer'},
    'types': {'type': 'list'},
    'items': {'type': 'list', 'schema': {'type': 'dict', 'schema': _get_tokens_items}}

}
get_token_transfers_by_token_address_item = {
    'transaction_hash': {'type': 'string', 'regex': regex_is_hex},
    'utc': {'type': 'string', 'regex': regex_utc},
    'to': {'type': 'string', 'regex': regex_is_hex},
    'type': {'type': 'string'},
    'value': {'type': 'string', 'regex': regex_is_hex},
    'log_index': {'type': 'integer'},
    'block_number': {'type': 'integer'},
    'address': {'type': 'string', 'regex': regex_is_hex},
    'transaction_index': {'type': 'integer'},
    'from': {'type': 'string', 'regex': regex_is_hex},
    'execute_address': {'type': 'string', 'regex': regex_is_hex},
}

get_token_transfers_by_token_address = {
    'addresses': {'type': 'list', 'schema': {'type': 'string'}},
    'limit': {'type': 'integer'},
    'count': {'type': 'integer'},
    'skip': {'type': 'integer'},
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': get_token_transfers_by_token_address_item
        }
    }
}

get_token_contract = {
    'holders_count': {'type': 'integer'},
    'info': {
        'type': 'dict',
        'schema': {
            'total_supply': {'type': 'string'},
            'symbol': {'type': 'string'},
            'decimals': {'type': 'string'},
            'name': {'type': 'string'},
        }
    },
    'address': {'type': 'string', 'regex': regex_is_hex},
    'create_transaction_hash': {'type': 'string', 'regex': regex_is_hex},
    'type': {'type': 'string'},
}

subscribe_to_addresses_notifications = {
    'addresses': {'type': 'list', 'schema': {'type': 'string'}},
    'token': {'type': 'string'},
}

_topics_indexed_item = {
    'topic': {'type': 'string', 'regex': regex_is_hex},
    'index': {'type': 'integer'},
}

get_contracts_logs = {
    'transaction_hash': {'type': 'string', 'regex': regex_is_hex},
    'block_hash': {'type': 'string', 'regex': regex_is_hex},
    'data': {'type': 'string', 'regex': regex_is_hex},
    'transaction_index': {'type': 'integer'},
    'log_index': {'type': 'integer'},
    'topics_indexed': {'type': 'list', 'schema': {'type': 'dict', 'schema': _topics_indexed_item}},
    'topics': {'type': 'list', 'schema': {'type': 'string', 'regex': regex_is_hex}},
    'block_number': {'type': 'integer'},
    'address': {'type': 'string', 'regex': regex_is_hex},
}

get_contract_general_information = {
    'bytecode': {'type': 'string', 'regex': regex_is_hex},
}
