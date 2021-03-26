import abc
from typing import List

from sales.domain.aggregates.aggregate import Aggregate


class Repository(abc.ABC):

    @abc.abstractmethod
    def all(self) -> List[Aggregate]:
        pass

    @abc.abstractmethod
    def find_by_id(self, id: int) -> Aggregate:
        pass

    @abc.abstractmethod
    def update(self, aggregate: Aggregate):
        pass
