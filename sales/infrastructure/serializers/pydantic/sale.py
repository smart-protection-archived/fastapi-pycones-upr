import pydantic


class Sale(pydantic.BaseModel):
    customer: int
    frame_id: int
    prize: float

