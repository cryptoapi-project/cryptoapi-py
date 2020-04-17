# -*- coding: utf-8 -*-
from .models import Models
from .api import Api
from .events import Events
from .rpc import Http, WS
from .configs import Config


class Client:

    def __init__(self, api_key, debug=False):
        self.config = Config()
        self.models = Models()
        self.api = Api(
            Http,
            self.config,
            self.models,
            api_key,
            debug
        )
        self.events = Events(
            WS,
            self.config,
            api_key,
            debug
        )
