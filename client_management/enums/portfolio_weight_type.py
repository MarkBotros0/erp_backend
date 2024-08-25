from common.enums import BaseEnum


class PortfolioWeightType(BaseEnum):
    TOTAL_WEIGHT = "total_weight"
    NET_WEIGHT = "net_weight"

    @classmethod
    def get_verbose_map(cls):
        return {
            cls.TOTAL_WEIGHT.value: "Total Weight",
            cls.NET_WEIGHT.value: "Net Weight",
        }
