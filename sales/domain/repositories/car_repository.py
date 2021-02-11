import abc

from sales.domain.aggregates.car import Car
from sales.domain.frame_id import FrameId
from sales.domain.repositories.repository import Repository


class CarRepository(Repository):

    @abc.abstractmethod
    def find_by_id(self, id: FrameId) -> Car:
        pass

    @abc.abstractmethod
    def update(self, car: Car) -> Car:
        pass

