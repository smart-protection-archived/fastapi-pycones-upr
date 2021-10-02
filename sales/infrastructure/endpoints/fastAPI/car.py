from sales.application.list_cars_use_case import ListCarsUseCase

from sales.application.list_cars_query import ListCarsQuery


def list_cars():
    query = ListCarsQuery()

    list_cars_use_case = ListCarsUseCase()
    list_cars_use_case.execute(query)
