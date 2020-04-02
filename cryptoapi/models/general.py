from cryptoapi.models.utils import regex_is_utc


# requests
_coins_request = {
    'type': 'list',
    'schema': {'type': 'string'}
}
get_coins_rates_request = {
    'coins': _coins_request,
}

get_coin_rates_history_request = {
    'coins': _coins_request,
}


# responses
get_coins_response = {
    'type': 'string'
}

_rate_schema = {
    'type': 'dict',
    'schema': {
        'USD': {'type': 'string'},
        'GBP': {'type': 'string'},
        'JPY': {'type': 'string'},
        'AUD': {'type': 'string'},
        'RUB': {'type': 'string'},
        'KRW': {'type': 'string'},
        'CNY': {'type': 'string'},
        'CHF': {'type': 'string'},
        'CAD': {'type': 'string'},
        'EUR': {'type': 'string'}
    }
}

get_coins_rates_response = {
    'symbol': {'type': 'string'},
    'rate': _rate_schema
}


_rates_item = {
    'created_at': {
        'type': 'string',
        'regex': regex_is_utc
    },
    'rate': _rate_schema
}

get_coin_rates_history_response = {
    'symbol': {'type': 'string'},
    'rates': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _rates_item
        }
    }
}
