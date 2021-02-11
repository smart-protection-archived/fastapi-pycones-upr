import abc

from sales.domain.aggregates.aggregate_id import AggregateId


class Aggregate(abc.ABC):

    def __init__(self, aggregate_id: AggregateId):
        self._id = aggregate_id

    @property
    def id(self):
        return self._id
