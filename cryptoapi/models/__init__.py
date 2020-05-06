from .model import Model
from .api import Api

from cryptoapi.utils.models import CustomValidator, string_type, integer_type, string_type_not_required


# get_coins = {
#     'coins': {
#         'type': 'list',
#         'schema': string_type
#     }
# }


def get_coins_validation(value):
    return isinstance(value, str)

get_coins = CustomValidator(
    get_coins_validation,
    'Get coins result must be a list of strings'
)


error = {
    'errors': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'message': string_type,
                'field': string_type_not_required,
                'value': string_type_not_required
            }
        }
    },
    'status': integer_type
}


# events schemes


def is_integer(value):
    return isinstance(value, int)

def is_string(value):
    return isinstance(value, str)


class Models:

    def __init__(self):
        self.get_coins = Model(get_coins, True)
        self.error = Model(error)
        self.api = Api(Model)

        # events schemes
        self.is_integer = Model(is_integer)
        self.is_string = Model(is_string)
        self.is_strings_list = Model(is_string, True)
