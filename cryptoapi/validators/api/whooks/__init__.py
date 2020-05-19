from typing import Callable

from .requests import Requests
from .responses import Responses


class Whooks:

    def __init__(self, validator: Callable) -> None:
        self.requests: Requests = Requests(validator)
        self.responses: Responses = Responses(validator)
