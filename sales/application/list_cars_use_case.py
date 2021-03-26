from typing import Dict, Any, List

from sales.application.list_cars_query import ListCarsQuery
from sales.application.use_case import UseCase
from sales.domain.aggregates.car import Car
from sales.domain.repositories.car_repository import CarRepository


class ListCarsUseCase(UseCase):

    def __init__(self, car_repository: CarRepository):
        self.car_repository = car_repository

    def execute(self, list_cars_query: ListCarsQuery) -> List[Car]:
        return self.car_repository.all()
