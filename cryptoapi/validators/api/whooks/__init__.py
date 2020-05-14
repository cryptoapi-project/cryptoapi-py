from .requests import Requests
from .responses import Responses


class Whooks:

    def __init__(self, validator):
        self.requests = Requests(validator)
        self.responses = Responses(validator)
