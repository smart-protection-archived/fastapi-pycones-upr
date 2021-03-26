from typing import Dict, Any

from sales.application.commands.create_sale import CreateSale
from sales.application.use_case import UseCase
from sales.domain.repositories.car_repository import CarRepository


class CreateSaleUseCase(UseCase):

    def __init__(self, car_repository: CarRepository):
        self.car_repository = car_repository

    def execute(self, create_sale: CreateSale):
        car = self.car_repository.find_by_id(create_sale.frame_id)

        car.sell(create_sale.customer_id, create_sale.prize)

        self.car_repository.update(car)
