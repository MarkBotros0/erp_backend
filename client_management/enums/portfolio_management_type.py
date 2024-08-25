from common.enums import BaseEnum


class PortfolioManagementType(BaseEnum):
    MANAGED = "managed"
    ADVISED = "advised"

    @classmethod
    def get_verbose_map(cls):
        return {
            cls.MANAGED.value: "Managed",
            cls.ADVISED.value: "Advised",
        }
