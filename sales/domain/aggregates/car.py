from datetime import datetime
from typing import Optional

from sales.domain.aggregates.aggregate import Aggregate
from sales.domain.customer_id import CustomerId
from sales.domain.exceptions import CarSoldWithoutCustomerException, CarAlreadySoldException
from sales.domain.frame_id import FrameId
from sales.domain.money import Money
from sales.domain.state import State, CarState


class Car(Aggregate):

    def __init__(self, frame_id: FrameId, prize: Money, state: Optional[State], sold_date: Optional[datetime] = None,
                 customer: Optional[CustomerId] = None):
        super().__init__(frame_id)
        self._prize = prize
        self._state = state
        self._owner = customer
        self._sold_date = sold_date

        if self._state != CarState.SOLD.value and (sold_date or customer):
            raise CarSoldWithoutCustomerException('Car cannot be sold without a customer')

    @property
    def prize(self) -> Money:
        return self._prize

    @property
    def owner(self) -> CustomerId:
        return self._owner

    @property
    def state(self) -> State:
        return self._state

    def sell(self, customer: CustomerId, prize: Money):
        if self._state == CarState.SOLD.value:
            raise CarAlreadySoldException()
        self._state = CarState.SOLD.value
        self._owner = customer
        self._prize = prize
        self._sold_date = datetime.now()

