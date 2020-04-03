# -*- coding: utf-8 -*-
from .models import Models
from .api import Api
from .rpc import Http


class Client:

    def __init__(self, api_key, debug=False):
        self.models = Models()
        self.api = Api(
            Http,
            self.models,
            api_key,
            debug
        )
        self.events = None
