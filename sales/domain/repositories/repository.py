import abc

from sales.domain.aggregates.aggregate import Aggregate


class Repository(abc.ABC):

    @abc.abstractmethod
    def find_by_id(self, id: int) -> Aggregate:
        pass

    @abc.abstractmethod
    def update(self, aggregate: Aggregate):
        pass
