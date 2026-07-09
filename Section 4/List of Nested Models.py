from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float


class Order(BaseModel):
    order_id: int
    items: list[Product]


order = Order(
    order_id=101,
    items=[
        {
            "name": "Laptop",
            "price": 55000
        },
        {
            "name": "Mouse",
            "price": 800
        }
    ]
)

print(order)


# Every dictionary inside the items list is validated and converted into a Product model object.