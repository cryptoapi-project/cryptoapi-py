from .api import ApiConfig
from .events import EventsConfig


class Config:

    def __init__(self) -> None:
        self.api = ApiConfig()
        self.events = EventsConfig()
