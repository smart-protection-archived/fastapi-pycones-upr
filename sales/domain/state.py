import enum


class State(str):
    pass


class CarState(enum.Enum):
    STOCK = State('stock')
    SOLD = State('sold')
