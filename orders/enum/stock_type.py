from enum import Enum

class StockType(Enum):
    FREE = "Free Stock"
    DISCOUNTED = "Discounted Stock"

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]

