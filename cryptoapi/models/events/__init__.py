from .notifications import Notifications


def _is_integer(value):
    return isinstance(value, int)


def _is_string(value):
    return isinstance(value, str)


class Events:

    def __init__(self, model_wrapper, utils):

        self.address = model_wrapper(utils.custom_validator(_is_string, 'address must be a string'))
        self.confirmations = model_wrapper(utils.custom_validator(_is_integer, 'confirmations must be a integer'))
        self.token = model_wrapper(utils.custom_validator(_is_string, 'token must be a string'))
        self._from = model_wrapper(utils.custom_validator(_is_string, 'from must be a string'))
        self.to = model_wrapper(utils.custom_validator(_is_string, 'to must be a string'))
        self.topics = model_wrapper(utils.custom_validator(_is_string, 'topics must be a list of strings'), True)
        self.hash = model_wrapper(utils.custom_validator(_is_string, 'hash must be a string'))
        self.subscription_id = model_wrapper(
            utils.custom_validator(_is_integer,
                                   'subscription_id must be a integer')
        )

        self.notifications = Notifications(model_wrapper)
