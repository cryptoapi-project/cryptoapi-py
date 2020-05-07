from .models import Models
from .api import Api
from .events import Events
from .rpc import Http, WS
from .configs import Config
from .utils import Utils


class Client:

    def __init__(self, api_key, debug=False):
        self.config = Config()
        self.utils = Utils()
        self.models = Models(self.utils)
        self.api = Api(
            Http,
            self.config,
            self.models,
            self.utils,
            api_key,
            debug
        )
        self.events = Events(
            WS,
            self.config,
            self.models,
            self.utils,
            api_key,
            debug
        )
