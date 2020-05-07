from .requests import Requests
from .responses import Responses


class Btc:

    def __init__(self, model_wrapper, utils):
        self.requests = Requests(model_wrapper)
        self.responses = Responses(model_wrapper, utils)
