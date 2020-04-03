from cryptoapi.models.utils import string_type

_coins_request = {
    'type': 'list',
    'required': False,
    'schema': string_type
}
get_coins_rates = {
    'coins': _coins_request,
}

get_coin_rates_history = {
    'coins': _coins_request,
}
