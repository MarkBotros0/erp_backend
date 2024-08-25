from common.enums import BaseEnum


class FundingType(BaseEnum):
    CASH_FINANCING = "cash_financing"
    MURABAHA = "murabaha"
    NO_FINANCING = "no_financing"
    ALL_FINANCING = "all_financing"

    @classmethod
    def get_verbose_map(cls):
        return {
            cls.CASH_FINANCING.value: "Cash Financing",
            cls.MURABAHA.value: "Murabaha",
            cls.NO_FINANCING.value: "No Financing",
            cls.ALL_FINANCING.value: "All Financing",
        }
