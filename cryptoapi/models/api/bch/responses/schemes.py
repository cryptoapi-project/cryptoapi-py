from cryptoapi.utils.types import hex_type, string_type, integer_type, utc_type, boolean_type,\
    string_nullable_type, integer_nullable_type

# BTC.Common

get_network_information = {
    'last_block': string_type,
    'count_transactions': string_type,
    'hashrate': string_type,
    'difficulty': string_type,
    'estimate_fee': string_type
}


def get_estimate_fee(value):
    return isinstance(value, float)


# BTC.Blocks

get_block = {
    'height': integer_type,
    'hash': hex_type,
    'bits': integer_type,
    'time': utc_type,
    'merkle_root': hex_type,
    'nonce': integer_type,
    'size': integer_type,
    'version': integer_type,
    'previous_block_hash': hex_type,
    'next_block_hash': string_nullable_type,
    'reward': integer_type,
    'count_transactions': integer_type
}
_blocks_items = {
    'height': integer_type,
    'hash': hex_type,
    'bits': integer_type,
    'time': utc_type,
    'merkle_root': hex_type,
    'nonce': integer_type,
    'size': integer_type,
    'version': integer_type,
    'previous_block_hash': hex_type,
    'next_block_hash': string_nullable_type,
    'reward': integer_type,
    'count_transactions': integer_type
}
get_blocks = {
    'skip': integer_type,
    'limit': integer_type,
    'count': integer_type,
    'items': {'type': 'list', 'schema': {'type': 'dict', 'schema': _blocks_items}}
}

# BTC.Transactions

_inputs_items = {
    'address': string_nullable_type,
    'previous_transaction_hash': hex_type,
    'output_index': integer_type,
    'sequence_number': integer_type,
    'script': string_nullable_type,
    'legacy_address': string_nullable_type
}

_outputs_items = {
    'address': string_nullable_type,
    'satoshis': integer_type,
    'script': string_type,
    'legacy_address': string_nullable_type
}

get_transaction_by_hash = {
    'block_height': integer_type,
    'block_hash': string_nullable_type,
    'block_time': string_nullable_type,
    'mempool_time': string_nullable_type,
    'fee': integer_type,
    'size': integer_type,
    'transaction_index': integer_type,
    'n_lock_time': integer_type,
    'value': integer_type,
    'hash': hex_type,
    'input_count': integer_type,
    'output_count': integer_type,
    'inputs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _inputs_items
        }
    },
    'outputs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _outputs_items
        }
    }
}

_transactions_items = get_transaction_by_hash.copy()

_transactions_items['inputs']['schema']['schema'].update({'satoshis': integer_type})
get_transactions = {
    'block_height_or_hash': integer_nullable_type,
    'skip': integer_type,
    'limit': integer_type,
    'from': string_nullable_type,
    'to': string_nullable_type,
    'items': {
        'type': 'list',
        'nullable': True,
        'schema': {
            'type': 'dict',
            'schema': _transactions_items
        }
    }
}

send_transaction = {
    'result': hex_type
}

_decode_transaction_inputs = {
    'previous_transaction_hash': hex_type,
    'output_index': integer_type,
    'sequence_number': integer_type,
    'script': string_nullable_type,
}
_decode_transaction_outputs = {
    'satoshis': integer_type,
    'script': string_type,
    'script_pub_key': string_type
}

decode_transaction = {
    'hash': hex_type,
    'version': integer_type,
    'n_lock_time': integer_type,
    'inputs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _decode_transaction_inputs
        }
    },
    'outputs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _decode_transaction_outputs
        }
    }
}

# BTC.Addresses

get_outputs_by_addresses = {
    'address': string_type,
    'is_coinbase': boolean_type,
    'mint_block_height': integer_type,
    'script': hex_type,
    'value': integer_type,
    'mint_index': integer_type,
    'mint_transaction_hash': hex_type,
    'spent_block_height': integer_type,
    'spent_transaction_hash': string_nullable_type,
    'spent_index': integer_type,
    'sequence_number': integer_type,
    'mempool_time': string_nullable_type
}

_balance = {
    'spent': string_type,
    'unspent': string_type,
    'confirmed': string_type,
    'unconfirmed': string_type
}

get_utxo_coin_addresses_info = {
    'address': string_type,
    'balance': {
        'type': 'dict',
        'schema': _balance
    }
}


_inputs_items = {
    'address': string_nullable_type,
    'previous_transaction_hash': hex_type,
    'output_index': integer_type,
    'sequence_number': integer_type,
    'script': string_nullable_type,
    'legacy_address': string_nullable_type
}

_outputs_items = {
    'address': string_nullable_type,
    'satoshis': integer_type,
    'script': string_type,
    'legacy_address': string_nullable_type
}


_utxo_coin_addresses_history_items = {
    'block_height': integer_type,
    'block_hash': string_nullable_type,
    'block_time': string_nullable_type,
    'mempool_time': string_nullable_type,
    'fee': integer_type,
    'size': integer_type,
    'transaction_index': integer_type,
    'n_lock_time': integer_type,
    'value': integer_type,
    'hash': hex_type,
    'input_count': integer_type,
    'output_count': integer_type,
    'inputs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _inputs_items
        }
    },
    'outputs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _outputs_items
        }
    }
}
get_utxo_coin_addresses_history = {
    'skip': integer_type,
    'limit': integer_type,
    'count': integer_type,
    'items': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _utxo_coin_addresses_history_items
        }
    }
}

# BTC.Push Notifications

subscribe_to_addresses_notifications = {
    'addresses': string_type,
    'token': string_nullable_type
}
