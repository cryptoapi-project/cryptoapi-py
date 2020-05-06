from .schemes import create_webhook, get_webhook, delete_webhook, change_webhook, get_events


class Requests:

    def __init__(self, model_wrapper):
        self.create_webhook = model_wrapper(create_webhook)
        self.get_webhook = model_wrapper(get_webhook)
        self.delete_webhook = model_wrapper(delete_webhook)
        self.change_webhook = model_wrapper(change_webhook)
        self.get_events = model_wrapper(get_events)
