from enum import Enum
from pydantic import BaseModel


class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


class Order(BaseModel):
    order_id: int
    status: OrderStatus


order = Order(
    order_id=101,
    status="processing"
)

print(order)

# The status field accepts only values defined inside OrderStatus.