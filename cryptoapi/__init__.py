# -*- coding: utf-8 -*-
from cryptoapi.api import Api


class Client:

    def __init__(self, api_key, debug=False):
        self.api = Api(api_key, debug)
        self.events = None
        self.models = None
