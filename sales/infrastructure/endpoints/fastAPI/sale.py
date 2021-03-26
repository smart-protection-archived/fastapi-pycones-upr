from sales.application.commands.create_sale import CreateSale
from sales.container import create_sale_use_case
from sales.domain.customer_id import CustomerId
from sales.domain.frame_id import FrameId
from sales.domain.money import Money
from sales.infrastructure.serializers.pydantic.sale import Sale


def create_sale(sale: Sale):
    command = CreateSale(frame_id=FrameId(sale.frame_id), customer_id=CustomerId(1), prize=Money(sale.prize))
    create_sale_use_case.execute(command)
