from typing import Any

from cryptoapi.utils.types import integer_type, string_type, string_type_not_required

from .bch import Bch
from .btc import Btc
from .eth import Eth
from .klay import Klay
from .ltc import Ltc
from .rates import Rates
from .whooks import Whooks

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


def get_coins(value: str) -> bool:
    return isinstance(value, str)


class Validators:

    def __init__(self, utils: Any) -> None:
        self._utils: Any = utils

        self.rates: Rates = Rates(self._utils)
        self.eth: Eth = Eth(self._utils)
        self.btc: Btc = Btc(self._utils)
        self.bch: Bch = Bch(self._utils)
        self.ltc: Ltc = Ltc(self._utils)
        self.klay: Klay = Klay(self._utils)
        self.whooks: Whooks = Whooks(self._utils)

        self.get_coins: Any = self._utils.validator((get_coins, 'Get coins result must be a list of strings'),
                                                    True)
        self.error: Any = self._utils.validator(error)
