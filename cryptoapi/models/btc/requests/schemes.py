from cryptoapi.models.utils import string_type_not_required, integer_type_not_required, required_string_type

# BTC.Blocks

block_by_height_or_hash = {
    'block_height_or_hash': required_string_type
}


blocks = {
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
}

# BTC.Transactions

transaction_by_hash = {
    'hash': required_string_type
}

transactions = {
    'block_height_or_hash': string_type_not_required,
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

# BTC.Addresses

outputs_by_addresses = {
    'addresses': required_string_type,
    'status': required_string_type,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required
}

utxo_coin_addresses_info = {
    'addresses': required_string_type
}

utxo_coin_addresses_history = {
    'addresses': required_string_type,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required
}

# BTC.Push Notifications

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
