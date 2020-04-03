from cryptoapi.utils.models import CustomValidator, hex_type, string_type, integer_type, utc_type, boolean_type,\
    string_nullable_type

# KLAY.Common

get_network_information = {
    'last_block': integer_type,
    'count_transactions': string_type,
    'gas_price': string_type,
    'difficulty': integer_type
}

estimate_gas = {
    'estimate_gas': string_type,
    'gas_price': string_type,
    'nonce': string_type
}

# KLAY.Blocks

_block_item = {
    "size": integer_type,
    'block_score': string_type,
    'total_block_score': string_type,
    'number': integer_type,
    'hash': hex_type,
    'parent_hash': hex_type,
    'reward': hex_type,
    'governance_data': string_type,
    'vote_data': string_type,
    'timestamp_fos': string_type,
    'logs_bloom': string_type,
    'transaction_root': hex_type,
    'state_root': hex_type,
    'receipts_root': hex_type,
    'extra_data': string_type,
    'gas_used': integer_type,
    'utc': utc_type,
    'block_reward': string_type,
    'count_transactions': integer_type
}


get_block_information_by_block_number_or_hash = _block_item.copy()


get_information_about_the_latest_blocks_with_pagination = {
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

# KLAY.Addresses

_transfer_item = {
    'block_number': integer_type,
    'utc': utc_type,
    'from': hex_type,
    'gas': integer_type,
    'hash': hex_type,
    'to': hex_type,
    'value': string_type,
    'gas_price': string_type,
    'internal': boolean_type
}

get_transactions_by_addresses = {
    'addresses': {
        'type': 'list',
        'schema': hex_type
    },
    'skip': string_type,
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
    'to': hex_type,
    'from': hex_type,
    'value': string_type,
    'input': hex_type,
    'is_suicide': boolean_type,
    'type': string_type
}
_signatures = {
    's': hex_type,
    'r': hex_type,
    'v': hex_type,
}

_transactions_item = {
    'block_hash': hex_type,
    'block_number': integer_type,
    'utc': utc_type,
    'from': hex_type,
    'gas': integer_type,
    'gas_price': string_type,
    'hash': hex_type,
    'input': hex_type,
    'nonce': integer_type,
    'to': hex_type,
    'transaction_index': integer_type,
    'value': string_type,
    'internal_transactions': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _internal_transactions
        }
    },
    'type': string_type,
    'type_int': integer_type,
    'signatures': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _signatures
        }
    },
    'code_format': string_nullable_type,
    'fee_payer': string_nullable_type,
    'fee_payer_signatures': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _signatures
        }
    },
    'fee_ratio': string_nullable_type,
    'human_readable': string_nullable_type,
    'key': string_nullable_type,
    'sender_tx_hash': hex_type
}

get_transaction_intersections_by_addresses = {
    'addresses': {
        'type': 'list',
        'schema': hex_type
    },
    'skip': string_type,
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
    'address': hex_type,
    'balance': string_type,
}

get_general_information_by_addresses = {
    'address': hex_type,
    'balance': string_type,
    'is_contract': boolean_type,
    'type': string_type,
    'count_transactions': integer_type
}

_token_item = {
    'type': string_type,
    'execute_address': hex_type,
    'from': hex_type,
    'to': hex_type,
    'value': hex_type,
    'address': hex_type,
    'block_number': integer_type,
    'transaction_hash': hex_type,
    'transaction_index': integer_type,
    'log_index': integer_type,
    'utc': utc_type,
}

get_token_transfers_by_addresses = {
    'addresses': {
        'type': 'list',
        'schema': hex_type
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
    'addresses': hex_type,
    'holder': hex_type,
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

# KLAY.Transactions

get_transactions_with_pagination = {
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
    'address': hex_type,
    'data': hex_type,
    'topics': {
        'type': 'list',
        'schema': hex_type
    },
    'log_index': integer_type,
    'transaction_hash': hex_type,
    'transaction_index': integer_type,
    'block_hash': hex_type,
    'block_number': integer_type,
    'id': string_type
}

_receipt = {
    'contract_address': string_nullable_type,
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
get_transaction_information.update({
    'receipt': {
        'type': 'dict',
        'schema': _receipt
    }
})

get_transaction_receipt = _receipt.copy()
get_transaction_receipt.update({
    'block_hash': hex_type,
    'block_number': integer_type,
    'from': hex_type,
    'hash': hex_type,
    'to': hex_type,
    'transaction_index': integer_type
})


send_transaction = {
    'hash': hex_type,
}

_decode_transaction_signatures = {
    'type': 'list',
    'schema': hex_type
}

decode_transaction = {
    'type': string_type,
    'nonce': integer_type,
    'gas_price': string_type,
    'gas': string_type,
    'from': hex_type,
    'human_readable': boolean_type,
    'fee_ratio': string_type,
    'code_format': string_type,
    'fee_payer': string_type,
    'payer_v': string_type,
    'payer_r': string_type,
    'payer_s': string_type,
    'fee_payer_signatures': _decode_transaction_signatures,
    'to': string_type,
    'value': string_type,
    'data': string_type,
    'v': string_type,
    'r': string_type,
    's': string_type,
    'signatures': {
        'type': 'list',
        'schema': _decode_transaction_signatures
    }
}

# KLAY.Tokens

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
    'address': hex_type,
    'create_transaction_hash': hex_type,
    'type': string_type,
    'status': boolean_type,
}

get_tokens = {
    'query': string_nullable_type,
    'skip': integer_type,
    'limit': integer_type,
    'count': integer_type,
    'types': {'type': 'list'},
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _get_tokens_items
        }
    }

}
_token_transfers = {
    'type': string_type,
    'execute_address': hex_type,
    'from': hex_type,
    'to': hex_type,
    'value': string_type,
    'address': hex_type,
    'block_number': integer_type,
    'transaction_hash': hex_type,
    'transaction_index': integer_type,
    'log_index': integer_type,
    'utc': utc_type,
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
    'address': hex_type,
    'create_transaction_hash': hex_type,
    'type': string_type,
}

subscribe_to_addresses_notifications = {
    'addresses': {
        'type': 'list',
        'schema': string_type
    },
    'token': string_type,
}

get_contracts_logs = {
    'address': hex_type,
    'data': hex_type,
    'topics': {
        'type': 'list',
        'schema': hex_type
    },
    'log_index': integer_type,
    'transaction_hash': hex_type,
    'transaction_index': integer_type,
    'block_hash': hex_type,
    'block_number': integer_type,
    'id': string_type
}


def _contract_call_validation(value):
    return isinstance(value, str)

contract_call = CustomValidator(
    _contract_call_validation,
    'Contract call result must be a string'
)

get_contract_general_information = {
    'bytecode': hex_type,
}
