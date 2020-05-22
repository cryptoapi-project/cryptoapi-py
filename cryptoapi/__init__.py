from .api import Api
from .events import Events
from .utils import Utils


class Client:

    def __init__(self, api_key: str, debug: bool = False) -> None:
        if not isinstance(api_key, str):
            raise Exception('API-KEY must be a string format')

        self.api_key: str = api_key

        if not isinstance(debug, bool):
            raise Exception('Debug value must be a boolean')

        self.debug: bool = debug

        self._utils: Utils = Utils()
        self.api: Api = Api(api_key, debug, self._utils)
        self.events: Events = Events(api_key, debug, self._utils)

    @property
    def api_key(self) -> str:
        return self._api_key

    @api_key.setter
    def api_key(self, api_key: str) -> None:
        if not isinstance(api_key, str):
            raise Exception('API-KEY must be a string format')

        change: bool = True if hasattr(self, '_api_key') and hasattr(self, '_debug') else False
        self._api_key: str = api_key
        if change:
            self.api: Api = Api(self._api_key, self._debug, self._utils)  # type: ignore
            self.events: Events = Events(self._api_key, self._debug, self._utils)  # type: ignore

    @property
    def debug(self) -> bool:
        return self._debug

    @debug.setter
    def debug(self, debug: bool) -> None:
        if not isinstance(debug, bool):
            raise Exception('Debug value must be a boolean')

        change: bool = True if hasattr(self, '_api_key') and hasattr(self, '_debug') else False
        self._debug: bool = debug

        if change:
            self.api: Api = Api(self._api_key, self._debug, self._utils)  # type: ignore
            self.events: Events = Events(self._api_key, self._debug, self._utils)  # type: ignore
