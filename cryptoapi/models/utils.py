regex_is_utc = '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]*Z$'
regex_is_hex = '^[0-9a-fA-F]+'
hex_type = {'type': 'string', 'regex': regex_is_hex}
utc_type = {'type': 'string', 'regex': regex_is_utc}
string_type = {'type': 'string'}
integer_type = {'type': 'integer'}
required_string_type = {'required': True, 'type': 'string'}
