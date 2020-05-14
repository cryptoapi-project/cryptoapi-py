from .requests import Requests
from .responses import Responses


class Btc:

    def __init__(self, validator, utils):
        self.requests = Requests(validator)
        self.responses = Responses(validator, utils)
