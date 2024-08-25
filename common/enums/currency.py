from common.enums import BaseEnum


class Currency(BaseEnum):
    EGP = "EGP"
    USD = "USD"
    SAR = "SAR"

    @classmethod
    def get_verbose_map(cls):
        return {
            cls.EGP.value: "EGP",
            cls.USD.value: "USD",
            cls.SAR.value: "SAR",
        }
