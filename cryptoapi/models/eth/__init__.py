from .requests import Requests
from .responses import Responses


class Eth:

    def __init__(self, model_wrapper):
        self.requests = Requests(model_wrapper)
        self.responses = Responses(model_wrapper)
