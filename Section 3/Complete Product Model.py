from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50
    )

    price: float = Field(
        gt=0
    )

    quantity: int = Field(
        ge=0
    )

    rating: float = Field(
        ge=0,
        le=5
    )


product = Product(
    name="Gaming Laptop",
    price=85000,
    quantity=10,
    rating=4.7
)

print(product)


# Each field has its own validation rule. The model is created only when all fields satisfy their constraints.