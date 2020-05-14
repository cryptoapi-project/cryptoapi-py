from cryptoapi.utils.types import (
    boolean_nullable_type_not_required,
    integer_nullable_type_not_required,
    integer_type,
    string_nullable_type_not_required,
    string_type
)

eth_block_notification = {
    'size': integer_type,
    'difficulty': string_type,
    'total_difficulty': string_type,
    'uncles': {
        'type': 'list',
        'schema': {
            'type': string_type
        }
    },
    'number': integer_type,
    'hash': string_type,
    'parent_hash': string_type,
    'nonce': string_type,
    'sha3U_uncles': string_type,
    'logs_bloom': string_type,
    'state_root': string_type,
    'miner': string_type,
    'extra_data': string_type,
    'gas_limit': string_type,
    'gas_used': string_type,
    'utc': string_type,
    'count_transactions': integer_type
}

klay_block_notification = {
    'size': integer_type,
    'block_score': string_type,
    'total_block_score': string_type,
    'number': integer_type,
    'hash': string_type,
    'parent_hash': string_type,
    'reward': string_type,
    'governance_data': string_type,
    'vote_data': string_type,
    'timestamp_fos': string_type,
    'logs_bloom': string_type,
    'state_root': string_type,
    'extra_data': string_type,
    'gas_used': integer_type,
    'utc': string_type,
    'count_transactions': integer_type,
}

address_subscription = {
    'address': string_type,
    'confirmations': integer_type,
}

balance_notification = {
    'address': string_type,
    'balance': string_type,
}

_internal_transactions = {
    'type': 'list',
    'schema': {
        'type': 'dict',
        'schema': {
            'to': string_type,
            'from': string_type,
            'value': string_type,
            'input': string_type,
            'type': string_type,
        }
    }
}

eth_transaction_notification = {
    'utc': string_type,
    'from': string_type,
    'gas': integer_type,
    'gas_price': string_type,
    'hash': string_type,
    'input': string_type,
    'nonce': integer_type,
    'to': string_type,
    'value': string_type,
    'v': string_type,
    's': string_type,
    'r': string_type,
    'internal_transactions': _internal_transactions
}

klay_transaction_notification = {
    'block_hash': string_type,
    'block_number': integer_type,
    'utc': string_type,
    'from': string_type,
    'gas': integer_type,
    'gas_price': string_type,
    'hash': string_type,
    'input': string_type,
    'nonce': integer_type,
    'to': string_type,
    'value': string_type,
    'transaction_index': integer_type,
    'type': string_type,
    'type_int': integer_type,
    'code_format': string_nullable_type_not_required,
    'fee_payer': string_nullable_type_not_required,
    'fee_ratio': string_nullable_type_not_required,
    'human_readable': boolean_nullable_type_not_required,
    'key': string_nullable_type_not_required,
    'sender_tx_hash': string_nullable_type_not_required,
    'internal_transactions': _internal_transactions
}

token_subscription = {
    'token': string_type,
    'address': string_type,
    'confirmations': integer_type,
}

transfer_notification = {
    'type': string_type,
    'execute_address': string_type,
    'from': string_type,
    'to': string_type,
    'value': string_type,
    'address': string_type,
    'block_number': integer_type,
    'transaction_hash': string_type,
    'transaction_index': integer_type,
    'utc': string_type,
}

token_balance_notification = {
    'address': string_type,
    'holder': string_type,
    'balance': string_type,
}

eth_contract_log_subscription = {
    'address': string_type,
    'confirmations': integer_nullable_type_not_required,
    'from': integer_nullable_type_not_required,
    'to': integer_nullable_type_not_required,
    'topics': {
        'type': 'list',
        'required': False,
        'nullable': True,
        'schema': {
            'type': string_type
        }
    }
}

eth_contract_log_notification = {
    'address': string_type,
    'data': string_type,
    'topics': {
        'type': 'list',
        'schema': {
            'type': string_type
        }
    },
    'log_index': integer_type,
    'transaction_hash': string_type,
    'transaction_index': integer_type,
    'block_hash': string_type,
    'block_number': integer_type,
}

transaction_confirmation_subscription = {
    'hash': string_type,
    'confirmations': integer_type,
}

transaction_confirmation_notification = {
    'hash': string_type,
    'confirmations': integer_type,
}

utxo_block_notification = {
    'hash': string_type,
    'bits': integer_type,
    'difficulty': integer_type,
    'time': string_type,
    'time_normalized': string_type,
    'merkle_root': string_type,
    'nonce': integer_type,
    'height': integer_type,
    'size': integer_type,
    'version': integer_type,
    'previous_block_hash': string_type,
    'next_block_hash': string_type,
    'reward': integer_type,
    'status': string_type,
    'count_transactions': integer_type,
}

utxo_transaction_notification = {
    'hash': string_type,
    'block_hash': string_type,
    'block_height': integer_type,
    'block_time': string_type,
    'block_time_normalized': string_type,
    'mempool_time': string_type,
    'fee': integer_type,
    'n_lock_time': integer_type,
    'size': integer_type,
    'value': integer_type,
    'input_count': integer_type,
    'output_count': integer_type,
    'inputs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'previous_transaction_hash': string_type,
                'output_index': integer_type,
                'sequence_number': integer_type,
                'script': string_type,
            }
        }
    },
    'outputs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'address': string_type,
                'satoshis': integer_type,
                'script': string_type
            }
        }
    }
}
