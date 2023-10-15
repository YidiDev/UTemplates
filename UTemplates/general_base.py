from abc import (ABC, abstractmethod)


class GeneralBaseElement(ABC):
    def __str__(self) -> str:
        return self.to_string()

    @abstractmethod
    def to_string(self) -> str:
        pass
