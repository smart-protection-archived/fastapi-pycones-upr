from dataclasses import dataclass

from sales.application.commands.command import Command
from sales.application.query import Query
from sales.domain.customer_id import CustomerId
from sales.domain.frame_id import FrameId
from sales.domain.money import Money


@dataclass(frozen=True)
class ListCarsQuery(Query):
    frame_id: FrameId
    customer_id: CustomerId
    prize: Money
