from typing import Any, Callable

from .requests import Requests
from .responses import Responses


class Ltc:

    def __init__(self, validator: Callable, utils: Any) -> None:
        self.requests: Requests = Requests(validator)
        self.responses: Responses = Responses(validator, utils)
