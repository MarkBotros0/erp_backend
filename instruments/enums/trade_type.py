from common.enums import BaseEnum


class TradeType(BaseEnum):
    BUY = "buy"
    SELL = "sell"

    @classmethod
    def get_verbose_map(cls):
        return {
            cls.BUY.value: "Buy",
            cls.SELL.value: "Sell",
        }
