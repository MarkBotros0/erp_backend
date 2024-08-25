from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def get_choices(cls) -> list:
        return [(member.value, member.verbose) for _, member in cls.__members__.items()]

    def __eq__(self, other):
        if isinstance(other, BaseEnum):
            return self.value == other.value
        return self.value == other

    @classmethod
    def get_verbose_map(cls):
        raise NotImplementedError

    @property
    def verbose(self):
        verbose_map = self.get_verbose_map()
        return verbose_map[self.value] if verbose_map.get(self.value) else self.name
