from cryptoapi.utils.models import string_type_not_required, integer_type_not_required, required_string_type, string_int_type

# BCH.Blocks

get_block = {
    'block_height_or_hash': string_int_type
}


get_blocks = {
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
}

# BCH.Transactions

get_transaction_by_hash = {
    'hash': required_string_type
}

get_transactions = {
    'block_height_or_hash': string_int_type,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
    'from': string_type_not_required,
    'to': string_type_not_required
}

send_transaction = {
    'hash': required_string_type
}

decode_transaction = {
    'hash': required_string_type
}

# BCH.Addresses

get_outputs_by_addresses = {
    'addresses': {
        'required': True,
        'type': 'list',
        'schema': required_string_type
    },
    'status': required_string_type,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required
}

get_utxo_coin_addresses_info = {
    'addresses': {
        'required': True,
        'type': 'list',
        'schema': required_string_type
    },
}

get_utxo_coin_addresses_history = {
    'addresses': {
        'required': True,
        'type': 'list',
        'schema': required_string_type
    },
    'skip': integer_type_not_required,
    'limit': integer_type_not_required
}

# BCH.Push Notifications

subscribe_to_addresses_notifications_params = {
    'addresses': {
        'required': True,
        'type': 'list',
        'schema': required_string_type
    },
}

subscribe_to_addresses_notifications_body = {
    'firebase_token': required_string_type
}

unsubscribe_from_addresses_notifications = {
    'addresses': {
        'required': True,
        'type': 'list',
        'schema': required_string_type
    },
    'firebase_token': required_string_type
}
