from functools import partial

from cryptoapi.utils.types import integer_type, string_type, string_type_not_required

from .api import Api
from .events import Events
from .validator import Validator

# get_coins = {
#     'coins': {
#         'type': 'list',
#         'schema': string_type
#     }
# }


def get_coins(value):
    return isinstance(value, str)


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


class Validators:

    def __init__(self, utils):
        self._validator = partial(Validator, custom_validator=utils.custom_validator)
        self.get_coins = self._validator(
            utils.custom_validator(get_coins,
                                   'Get coins result must be a list of strings'),
            True
        )
        self.error = self._validator(error)
        self.api = Api(self._validator, utils)
        self.events = Events(self._validator, utils)
