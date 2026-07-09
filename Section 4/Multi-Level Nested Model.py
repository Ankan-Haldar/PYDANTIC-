from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str


class Customer(BaseModel):
    name: str
    address: Address


class Order(BaseModel):
    order_id: int
    customer: Customer


order = Order(
    order_id=101,
    customer={
        "name": "Rahul",
        "address": {
            "city": "Kolkata",
            "state": "West Bengal"
        }
    }
)

print(order)



# The model contains three validation levels: Order → Customer → Address.