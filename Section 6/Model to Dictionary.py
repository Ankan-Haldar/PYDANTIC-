from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int


product = Product(
    name="Laptop",
    price=55000,
    quantity=2
)


data = product.model_dump()

print(data)
print(type(data))


# model_dump() converts the validated model into a normal Python dictionary.