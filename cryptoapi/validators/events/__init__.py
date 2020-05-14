from .notifications import Notifications


def _is_integer(value):
    return isinstance(value, int)


def _is_string(value):
    return isinstance(value, str)


class Events:

    def __init__(self, validator, utils):

        self.address = validator(utils.custom_validator(_is_string, 'address must be a string'))
        self.confirmations = validator(utils.custom_validator(_is_integer, 'confirmations must be a integer'))
        self.token = validator(utils.custom_validator(_is_string, 'token must be a string'))
        self._from = validator(utils.custom_validator(_is_string, 'from must be a string'))
        self.to = validator(utils.custom_validator(_is_string, 'to must be a string'))
        self.topics = validator(utils.custom_validator(_is_string, 'topics must be a list of strings'), True)
        self.hash = validator(utils.custom_validator(_is_string, 'hash must be a string'))
        self.subscription_id = validator(utils.custom_validator(_is_integer, 'subscription_id must be a integer'))

        self.notifications = Notifications(validator)
