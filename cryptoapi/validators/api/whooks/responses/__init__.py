from .schemes import get_hook_events


class Responses:

    def __init__(self, validator):
        self.get_hook_events = validator(get_hook_events)
