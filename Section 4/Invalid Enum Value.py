from enum import Enum
from pydantic import BaseModel


class OrderStatus(str, Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


class Order(BaseModel):
    order_id: int
    status: OrderStatus


order = Order(
    order_id=101,
    status="unknown"
)

# "unknown" is not one of the allowed Enum values, so Pydantic rejects it.