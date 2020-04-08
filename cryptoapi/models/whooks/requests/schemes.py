from cryptoapi.utils.models import string_type, integer_type,\
    required_string_type, boolean_type, string_type_not_required, integer_type_not_required, \
    boolean_type_not_required


_transfer_triggers = {
    'transfer_address': string_type,
    'token_address': string_type
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
        'schema': required_string_type
    },
    'transfer_triggers': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _transfer_triggers
        }
    }
}

get_webhook = {
    'project_id': integer_type
}

delete_webhook = {
    'id': integer_type
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
        'schema': {
            'type': 'dict',
            'schema': _transfer_triggers
        }
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

get_events = {
    'hook_id': integer_type,
    'start_id': integer_type_not_required,
    'end_id': integer_type_not_required,
    'only_failed': boolean_type_not_required,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
    'type': string_type_not_required
}
