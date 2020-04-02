from cryptoapi.models.utils import string_type, utc_type

_rate_schema = {
    'type': 'dict',
    'schema': {
        'USD': string_type,
        'GBP': string_type,
        'JPY': string_type,
        'AUD': string_type,
        'RUB': string_type,
        'KRW': string_type,
        'CNY': string_type,
        'CHF': string_type,
        'CAD': string_type,
        'EUR': string_type
    }
}

get_coins_rates = {
    'symbol': string_type,
    'rate': _rate_schema
}


_rates_item = {
    'created_at': utc_type,
    'rate': _rate_schema
}

get_coin_rates_history = {
    'symbol': string_type,
    'rates': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _rates_item
        }
    }
}
