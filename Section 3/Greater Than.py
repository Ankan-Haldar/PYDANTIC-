from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    price: float = Field(gt=0)


product = Product(
    name="Laptop",
    price=55000
)

print(product)