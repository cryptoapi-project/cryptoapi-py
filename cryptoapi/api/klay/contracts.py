class Contracts:

    def __init__(self, http, validators, utils, api_key):
        self._http = http
        self._api_key = api_key
        self._validators = validators
        self._utils = utils

    def get_contracts_logs(
        self,
        cursor=None,
        reversed_fetch=None,
        from_block=None,
        to_block=None,
        addresses=None,
        topics=None
    ):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {}
        if cursor is not None:
            params.update({'cursor': cursor})

        if reversed_fetch is not None:
            params.update({'reversed_fetch': reversed_fetch})

        if from_block is not None:
            params.update({'from_block': from_block})

        if to_block is not None:
            params.update({'to_block': to_block})

        if addresses is not None:
            params.update({'addresses': ','.join(addresses)})

        if topics is not None:
            params.update({'topics': ','.join(topics)})

        self._utils.validate_data(self._validators.api.klay.requests.get_contracts_logs, params)

        validators.update({200: self._validators.api.klay.responses.get_contracts_logs})

        params.update(api_key)

        return self._http.get(url='/contracts/logs', params=params, validators=validators)

    def contract_call(self, address, sender, amount, bytecode):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'address': address
        }

        data = {
            'sender': sender,
            'amount': amount,
            'bytecode': bytecode
        }

        self._utils.validate_data(self._validators.api.klay.requests.contract_call_params, params)
        self._utils.validate_data(self._validators.api.klay.requests.contract_call_body, data)

        validators.update({200: self._validators.api.klay.responses.contract_call})

        return self._http.post(
            url='/contracts/{}/call'.format(params.pop('address')),
            data=data,
            params=api_key,
            validators=validators
        )

    def get_contract_general_information(self, address):
        api_key, validators = self._utils.api_method_preprocessing(self)

        params = {
            'address': address
        }

        self._utils.validate_data(self._validators.api.klay.requests.get_contract_general_information, params)

        validators.update({200: self._validators.api.klay.responses.get_contract_general_information})

        return self._http.get(
            url='/contracts/{}'.format(params.pop('address')),
            params=api_key,
            validators=validators
        )
