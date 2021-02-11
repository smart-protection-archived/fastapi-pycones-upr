from sales.domain.aggregates.aggregate_id import AggregateId


class CustomerId(AggregateId, int):
    pass
