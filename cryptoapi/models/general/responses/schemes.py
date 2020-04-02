from cryptoapi.models.utils import regex_is_utc

get_coins = {
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

get_coins_rates = {
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

get_coin_rates_history = {
    'symbol': {'type': 'string'},
    'rates': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': _rates_item
        }
    }
}

error = {
    'errors': {
        'type': 'list',
        'schema': {
            'message': {'type': 'string'},
            'field': {'type': 'string'}
        }
    },
    'status': {'type': 'integer'}
}
