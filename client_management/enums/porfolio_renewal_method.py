from common.enums import BaseEnum


class PortfolioRenewalMethod(BaseEnum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"

    @classmethod
    def get_verbose_map(cls):
        return {
            cls.AUTOMATIC.value: "Automatic",
            cls.MANUAL.value: "Manual",
        }
