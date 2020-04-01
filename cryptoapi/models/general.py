regex_utc = '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]*Z$'
get_coins_response = {
    'type': 'string'
}

get_coins_rates_request = {
    'coins': {'type': 'list', 'schema': {'type': 'string'}},
}

rate_schema = {
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

get_coins_rates_response = {
    'symbol': {'type': 'string'},
    'rate': {'type': 'dict', 'schema': rate_schema}
}

get_coin_rates_history_request = {
    'coins': {'type': 'list', 'schema': {'type': 'string'}},
}


rates_item = {
    'created_at': {'type': 'string', 'regex': regex_utc},
    'rate': {'type': 'dict', 'schema': rate_schema}
}

get_coin_rates_history_response = {
    'symbol': {'type': 'string'},
    'rates': {'type': 'list', 'schema': {'type': 'dict', 'schema': rates_item}}
}
