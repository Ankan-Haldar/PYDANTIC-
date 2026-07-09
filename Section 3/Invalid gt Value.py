from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    price: float = Field(gt=0)


product = Product(
    name="Laptop",
    price=-500
)

# The value -500 is not greater than 0, so validation fails.