from cryptoapi.utils.types import (
    boolean_type,
    float_integer_type,
    hex_type_eth,
    integer_type,
    string_nullable_type,
    string_type,
    utc_type
)

# ETH.Common

get_network_info = {
    'last_block': integer_type,
    'count_transactions': string_type,
    'gas_price': string_type,
    'hashrate': integer_type,
    'difficulty': float_integer_type
}

estimate_gas = {
    'estimate_gas': string_type,
    'gas_price': string_type,
    'nonce': string_type
}

# ETH.Blocks

_block_item = {
    'size': integer_type,
    'difficulty': integer_type,
    'total_difficulty': string_type,
    'uncles': {
        'type': 'list'
    },
    'number': integer_type,
    'hash': hex_type_eth,
    'parent_hash': hex_type_eth,
    'nonce': hex_type_eth,
    'sha3_uncles': hex_type_eth,
    'logs_bloom': hex_type_eth,
    'transaction_root': hex_type_eth,
    'state_root': hex_type_eth,
    'receipts_root': hex_type_eth,
    'miner': hex_type_eth,
    'mix_hash': hex_type_eth,
    'extra_data': hex_type_eth,
    'gas_limit': string_type,
    'gas_used': integer_type,
    'utc': utc_type,
    'reward': string_type,
    'uncle_rewards': {
        'type': 'dict'
    },
    'count_transactions': integer_type
}

get_block = _block_item.copy()

get_blocks = {
    'skip': integer_type,
    'limit': integer_type,
    'count': integer_type,
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _block_item
        }
    }
}

# ETH.Addresses

_transfer_item = {
    'block_number': integer_type,
    'utc': utc_type,
    'from': hex_type_eth,
    'gas': integer_type,
    'hash': hex_type_eth,
    'to': hex_type_eth,
    'value': string_type,
    'gas_price': string_type,
    'internal': boolean_type,
    'input': hex_type_eth,
    'status': boolean_type
}

get_transactions_by_addresses = {
    'addresses': {
        'type': 'list',
        'schema': hex_type_eth
    },
    'skip': integer_type,
    'limit': integer_type,
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _transfer_item
        }
    },
    'count': integer_type
}

_internal_transactions = {
    'to': hex_type_eth,
    'from': hex_type_eth,
    'value': string_type,
    'input': hex_type_eth,
    'is_suicide': boolean_type,
    'type': string_type
}

_transactions_item = {
    'block_hash': hex_type_eth,
    'block_number': integer_type,
    'utc': utc_type,
    'from': hex_type_eth,
    'gas': integer_type,
    'gas_price': string_type,
    'hash': hex_type_eth,
    'input': hex_type_eth,
    'nonce': integer_type,
    'to': string_nullable_type,
    'transaction_index': integer_type,
    'value': string_type,
    'v': hex_type_eth,
    's': hex_type_eth,
    'r': hex_type_eth,
    'internal_transactions': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _internal_transactions
        }
    },
    'status': boolean_type
}

get_transaction_intersections_by_addresses = {
    'addresses': {
        'type': 'list',
        'schema': hex_type_eth
    },
    'skip': integer_type,
    'limit': integer_type,
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _transactions_item
        }
    },
    'count': integer_type
}

get_balances_by_addresses = {
    'address': hex_type_eth,
    'balance': string_type,
}

get_general_information_by_addresses = {
    'address': hex_type_eth,
    'balance': string_type,
    'is_contract': boolean_type,
    'type': string_type,
    'count_transactions': integer_type
}

_token_item = {
    'type': string_type,
    'execute_address': hex_type_eth,
    'from': hex_type_eth,
    'to': hex_type_eth,
    'value': hex_type_eth,
    'address': hex_type_eth,
    'block_number': integer_type,
    'transaction_hash': hex_type_eth,
    'transaction_index': integer_type,
    'log_index': integer_type,
    'utc': utc_type,
}

get_token_transfers_by_addresses = {
    'addresses': {
        'type': 'list',
        'schema': hex_type_eth
    },
    'skip': integer_type,
    'limit': integer_type,
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _token_item
        }
    },
    'count': integer_type
}

_balance_token_item = {
    'address': hex_type_eth,
    'holder': hex_type_eth,
    'balance': string_type
}

get_tokens_balances_by_holders = {
    'count': integer_type,
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _balance_token_item
        }
    },
}
get_token_balance_by_holders_and_token = get_tokens_balances_by_holders.copy()

# ETH.Transactions

get_transactions = {
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _transactions_item
        }
    },
    'count': integer_type
}

_receipt_logs = {
    'address': hex_type_eth,
    'data': hex_type_eth,
    'topics': {
        'type': 'list',
        'schema': hex_type_eth
    },
    'log_index': integer_type,
    'transaction_hash': hex_type_eth,
    'transaction_index': integer_type,
    'block_hash': hex_type_eth,
    'block_number': integer_type,
    'id': string_type
}

_receipt = {
    'contract_address': string_nullable_type,
    'cumulative_gas_used': integer_type,
    'gas_used': integer_type,
    'status': boolean_type,
    'logs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _receipt_logs
        }
    },
}

get_transaction_information = _transactions_item.copy()
get_transaction_information.update({'receipt': {
    'type': 'dict',
    'schema': _receipt
}})

get_transaction_receipt = _receipt.copy()
get_transaction_receipt.update({
    'block_hash': hex_type_eth,
    'block_number': integer_type,
    'from': hex_type_eth,
    'hash': hex_type_eth,
    'to': string_nullable_type,
    'transaction_index': integer_type
})

send_transaction = {
    'hash': hex_type_eth,
}

decode_transaction = {
    'nonce': integer_type,
    'gas_price': string_type,
    'gas_limit': string_type,
    'to': string_type,
    'value': string_type,
    'data': string_type,
    'v': integer_type,
    'r': string_type,
    's': string_type
}

# ETH.Tokens

_tokens_items = {
    'total_supply': string_type,
    'symbol': string_type,
    'decimals': string_type,
    'name': string_type,
}

_get_tokens_items = {
    'info': {
        'type': 'dict',
        'schema': _tokens_items
    },
    'address': hex_type_eth,
    'create_transaction_hash': hex_type_eth,
    'type': string_type,
    'status': boolean_type,
}

get_tokens = {
    'query': string_nullable_type,
    'skip': integer_type,
    'limit': integer_type,
    'count': integer_type,
    'types': {
        'type': 'list'
    },
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _get_tokens_items
        }
    }
}
_token_transfers = {
    'transaction_hash': hex_type_eth,
    'utc': utc_type,
    'to': hex_type_eth,
    'type': string_type,
    'value': hex_type_eth,
    'log_index': integer_type,
    'block_number': integer_type,
    'address': hex_type_eth,
    'transaction_index': integer_type,
    'from': hex_type_eth,
    'execute_address': hex_type_eth,
}

get_token_transfers_by_token_address = {
    'addresses': {
        'type': 'list',
        'schema': string_type
    },
    'limit': integer_type,
    'count': integer_type,
    'skip': integer_type,
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _token_transfers
        }
    }
}

get_token_contract = {
    'holders_count': integer_type,
    'info': {
        'type': 'dict',
        'schema': {
            'total_supply': string_type,
            'symbol': string_type,
            'decimals': string_type,
            'name': string_type,
        }
    },
    'address': hex_type_eth,
    'create_transaction_hash': hex_type_eth,
    'type': string_type,
}

subscribe_to_addresses_notifications = {
    'addresses': {
        'type': 'list',
        'schema': string_type
    },
    'token': string_type,
}

_topics_indexed = {
    'topic': hex_type_eth,
    'index': integer_type,
}

get_contracts_logs = {
    'transaction_hash': string_type,
    'block_hash': string_type,
    'data': string_type,
    'transaction_index': integer_type,
    'log_index': integer_type,
    'topics': {
        'type': 'list',
        'schema': string_type
    },
    'block_number': integer_type,
    'address': string_type,
    "id": string_type
}


def contract_call(value: str) -> bool:
    return isinstance(value, str)


get_contract_general_information = {
    'bytecode': string_type,
}
