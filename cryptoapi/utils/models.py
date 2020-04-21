regex_is_utc = '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]*Z$'
regex_is_hex = '^[0-9a-fA-F]*'
regex_is_hex_eth = '^0x[0-9a-fA-F]*'
hex_type = {'type': 'string', 'regex': regex_is_hex}
hex_type_eth = {'type': 'string', 'regex': regex_is_hex_eth}
utc_type = {'type': 'string', 'regex': regex_is_utc}
string_type = {'type': 'string'}
string_nullable_type = {'type': 'string', 'nullable': True}
integer_type = {'type': 'integer'}
integer_nullable_type = {'type': 'integer', 'nullable': True}
required_string_type = {'required': True, 'type': 'string'}
boolean_type = {'type': 'boolean'}
hex_type_not_required = {'type': 'string', 'required': False, 'regex': regex_is_hex}
hex_type_not_required_eth = {'type': 'string', 'required': False, 'regex': regex_is_hex_eth}
string_type_not_required = {'type': 'string', 'required': False}
integer_type_not_required = {'type': 'integer', 'required': False}
boolean_type_not_required = {'type': 'boolean', 'required': False}
string_int_type = {'type': ['string', 'integer']}


class CustomValidator:

    def __init__(self, func, error_text):
        self._func = func
        self._error_text = error_text
        self._errors = None

    @property
    def errors(self):
        return self._errors

    def validate(self, data):
        if not self._func(data):
            self._errors = self._error_text
            return False
        self._errors = None
        return True
