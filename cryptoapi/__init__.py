from .api import Api
from .events import Events
from .utils import Utils


class Client:

    def __init__(self, api_key: str, debug: bool = False) -> None:
        self._utils: Utils = Utils()
        self.api: Api = Api(api_key, debug, self._utils)
        self.events: Events = Events(api_key, debug, self._utils)
