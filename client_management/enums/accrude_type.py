from common.enums import BaseEnum


class AccruedType(BaseEnum):
    START_OF_DAY = "start_of_day"
    END_OF_DAY = "end_of_day"
    END_OF_DAY_WITH_HOLIDAYS = "end_of_day_with_holidays"

    @classmethod
    def get_verbose_map(cls):
        return {
            cls.START_OF_DAY.value: "Start of Day",
            cls.END_OF_DAY.value: "End of Day",
            cls.END_OF_DAY_WITH_HOLIDAYS.value: "End of Day with Holidays",
        }
