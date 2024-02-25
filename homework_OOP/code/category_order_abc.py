from abc import ABC, abstractmethod


class CategoryOrderABC(ABC):
    @abstractmethod
    def total_cost(self):
        pass
