from cryptoapi.utils.types import (
    boolean_type_not_required,
    integer_type,
    integer_type_not_required,
    string_type_not_required
)

get_hook_events = {
    'hook_id': integer_type,
    'start_id': integer_type_not_required,
    'end_id': integer_type_not_required,
    'only_failed': boolean_type_not_required,
    'skip': integer_type_not_required,
    'limit': integer_type_not_required,
    'type': string_type_not_required
}
