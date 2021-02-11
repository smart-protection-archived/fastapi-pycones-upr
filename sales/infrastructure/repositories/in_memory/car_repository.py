from sales.domain.aggregates.car import Car
from sales.domain.frame_id import FrameId
from sales.domain.money import Money
from sales.domain.repositories.car_repository import CarRepository
from sales.domain.state import CarState
from sales.infrastructure.repositories.in_memory.in_memory_repository import InMemoryRepository


class InMemoryCarRepository(InMemoryRepository, CarRepository):
    _DATABASE = {
        123: Car(FrameId(123), Money(25000.0), CarState.STOCK.value)
    }
