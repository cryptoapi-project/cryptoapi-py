from .model import Model
from .rates import Rates
from .eth import Eth
from .btc import Btc
from .klay import Klay
from .whooks import Whooks

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


class Models:

    def __init__(self):
        self.get_coins = Model(get_coins, True)
        self.error = Model(error)

        self.rates = Rates(Model)
        self.eth = Eth(Model)
        self.btc = Btc(Model)
        self.bch = Btc(Model)
        self.klay = Klay(Model)
        self.whooks = Klay(Whooks)
