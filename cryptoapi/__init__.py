from .api import Api
from .configs import Config
from .events import Events
from .rpc import WS, Http
from .utils import Utils
from .validators import Validators


class Client:

    def __init__(self, api_key, debug=False):
        self.config = Config()
        self.utils = Utils()
        self.validators = Validators(self.utils)
        self.api = Api(Http, self.config, self.validators, self.utils, api_key, debug)
        self.events = Events(WS, self.config, self.validators, self.utils, api_key, debug)
