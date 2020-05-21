from typing import Any

from .notifications import Notifications


def _is_integer(value: str) -> bool:
    return isinstance(value, int)


def _is_string(value: str) -> bool:
    return isinstance(value, str)


class Validators:

    def __init__(self, utils: Any) -> None:

        self.address: Any = utils.validator((_is_string, 'address must be a string'))
        self.confirmations: Any = utils.validator((_is_integer, 'confirmations must be a integer'))
        self.token: Any = utils.validator((_is_string, 'token must be a string'))
        self._from: Any = utils.validator((_is_string, 'from must be a string'))
        self.to: Any = utils.validator((_is_string, 'to must be a string'))
        self.topics: Any = utils.validator((_is_string, 'topics must be a list of strings'), True)
        self.hash: Any = utils.validator((_is_string, 'hash must be a string'))
        self.subscription_id: Any = utils.validator((_is_integer, 'subscription_id must be a integer'))

        self.notifications: Notifications = Notifications(utils)
