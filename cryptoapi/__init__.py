from .api import Api
from .configs import Config
from .events import Events
from .rpc import WS, Http
from .utils import Utils
from .validators import Validators


class Client:

    def __init__(self, api_key: str, debug: bool = False) -> None:
        self.config: Config = Config()
        self.utils: Utils = Utils()
        self.validators: Validators = Validators(self.utils)
        self.api: Api = Api(Http, self.config, self.validators, self.utils, api_key, debug)
        self.events: Events = Events(WS, self.config, self.validators, self.utils, api_key, debug)
