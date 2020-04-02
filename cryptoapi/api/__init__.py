# -*- coding: utf-8 -*-
from cryptoapi.rpc import Http


class Api:

    def __init__(self, api_key, debug=False):
        self.eth = None
        self.btc = None
        self.bch = None
        self.klay = None
