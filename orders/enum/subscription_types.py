from enum import Enum

class SubscriptionType(Enum):
    GENERAL = "General"
    CLOSED = "Closed"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]