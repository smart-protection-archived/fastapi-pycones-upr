from typing import Dict

from sales.domain.aggregates.aggregate import Aggregate
from sales.domain.repositories.repository import Repository


class InMemoryRepository(Repository):
    _DATABASE: Dict[int, Aggregate] = {}

    def find_by_id(self, id: int) -> Aggregate:
        return self._DATABASE[id]

    def update(self, aggregate: Aggregate) -> Aggregate:
        self._DATABASE[aggregate.id] = aggregate
        return self._DATABASE[aggregate.id]

