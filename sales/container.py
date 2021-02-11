from sales.application.create_sale_use_case import CreateSaleUseCase
from sales.infrastructure.repositories.in_memory.car_repository import InMemoryCarRepository

car_repository = InMemoryCarRepository()
create_sale_use_case = CreateSaleUseCase(car_repository=car_repository)
