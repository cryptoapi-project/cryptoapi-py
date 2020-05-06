from .schemes import get_hook_events


class Responses:

    def __init__(self, model_wrapper):
        self.get_hook_events = model_wrapper(get_hook_events)
