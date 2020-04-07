from cryptoapi.utils.models import hex_type_not_required, string_type, integer_type, boolean_type


_transfer_triggers = {
    "transfer_address": "string",
    "token_address": "string"
}

create_webhook = {
    'project_id': integer_type,
    'url': string_type,
    'coin': string_type,
    'is_subscribe_block': boolean_type,
    'is_subscribe_transfer': boolean_type,
    'is_subscribe_transaction': boolean_type,
    'transaction_addresses': {
        'required': True,
        'type': 'list',
        'schema': string_type
    },
    'transfer_triggers': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _transfer_triggers
        }
    },
    'id': integer_type
}

get_webhook = {
    'project_id': integer_type,
    'url': string_type,
    'coin': string_type,
    'is_subscribe_block': boolean_type,
    'is_subscribe_transfer': boolean_type,
    'is_subscribe_transaction': boolean_type,
    'transaction_addresses': {
        'required': True,
        'type': 'list',
        'schema': string_type
    },
    'transfer_triggers': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _transfer_triggers
        }
    },
    'id': integer_type
}

delete_webhook = {
    'status': integer_type,
    'message': string_type
}

change_webhook = {
    'project_id': integer_type,
    'url': string_type,
    'coin': string_type,
    'is_subscribe_block': boolean_type,
    'is_subscribe_transfer': boolean_type,
    'is_subscribe_transaction': boolean_type,
    'transaction_addresses': {
        'required': True,
        'type': 'list',
        'schema': string_type
    },
    'transfer_triggers': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _transfer_triggers
        }
    },
    'id': integer_type
}

_items = {
    'id': integer_type,
    'user_id': integer_type,
    'hook_id': integer_type,
    'status': integer_type,
    'log_id': integer_type,
    'data': {'type': 'dict'}
}

get_events = {
    'start_id': integer_type,
    'end_id': integer_type,
    'only_failed': boolean_type,
    'skip': integer_type,
    'limit': integer_type,
    'type': string_type,
    'count': integer_type,
    'items': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _items
        }
    },
}
