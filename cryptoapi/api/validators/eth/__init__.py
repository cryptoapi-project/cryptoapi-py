from typing import Any

from .requests import Requests
from .responses import Responses


class Eth:

    def __init__(self, utils: Any) -> None:
        self.requests: Requests = Requests(utils)
        self.responses: Responses = Responses(utils)
