from .model import Model
from .rates import Rates
from .eth import Eth
from .btc import Btc
from .klay import Klay

from .utils import string_type, integer_type


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
            'message': string_type,
            'field': string_type
        }
    },
    'status': integer_type
}


class Models:

    def __init__(self):
        self.get_coins = Model(get_coins, True)
        self.error = Model(error)

        self.rates = Rates(Model)
        self.eth = Eth(Model)
        self.btc = Btc(Model)
        self.bch = Btc(Model)
        self.klay = Klay(Model)
