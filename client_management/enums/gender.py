from common.enums import BaseEnum


class Gender(BaseEnum):
    MALE = "male"
    FEMALE = "female"
    ENTITY = "Entity"

    @classmethod
    def get_verbose_map(cls):
        return {
            cls.MALE.value: "Male",
            cls.FEMALE.value: "Female",
            cls.ENTITY.value: "Entity",
        }
