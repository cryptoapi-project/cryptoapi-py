# -*- coding: utf-8 -*-
def api_method_preprocessing(api):
        if not api._api_key:
            raise Exception('API-KEY for this Client is not set')

        validators = {
            401: api._models.error,
            422: api._models.error
        }

        return {'token': api._api_key}, validators


def validate_data(validator, data):
    if not validator.validate(data):
        raise Exception(validator.errors)
