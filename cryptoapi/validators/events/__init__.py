from typing import Any, Callable

from .notifications import Notifications


def _is_integer(value: str) -> bool:
    return isinstance(value, int)


def _is_string(value: str) -> bool:
    return isinstance(value, str)


class Events:

    def __init__(self, validator: Callable, utils: Any) -> None:

        self.address: Callable = validator(utils.custom_validator(_is_string, 'address must be a string'))
        self.confirmations: Callable = validator(
            utils.custom_validator(_is_integer,
                                   'confirmations must be a integer')
        )
        self.token: Callable = validator(utils.custom_validator(_is_string, 'token must be a string'))
        self._from: Callable = validator(utils.custom_validator(_is_string, 'from must be a string'))
        self.to: Callable = validator(utils.custom_validator(_is_string, 'to must be a string'))
        self.topics: Callable = validator(
            utils.custom_validator(_is_string,
                                   'topics must be a list of strings'),
            True
        )
        self.hash: Callable = validator(utils.custom_validator(_is_string, 'hash must be a string'))
        self.subscription_id: Callable = validator(
            utils.custom_validator(_is_integer,
                                   'subscription_id must be a integer')
        )

        self.notifications: Notifications = Notifications(validator)
