from cryptoapi.utils.models import string_type, integer_type, boolean_type


_items = {
    'id': integer_type,
    'user_id': integer_type,
    'hook_id': integer_type,
    'status': integer_type,
    'log_id': integer_type,
    'data': {'type': 'dict'}
}

get_hook_events = {
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
