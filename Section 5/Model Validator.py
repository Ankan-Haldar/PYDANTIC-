from pydantic import BaseModel, model_validator


class Product(BaseModel):
    original_price: float
    discount_price: float

    @model_validator(mode="after")
    def validate_prices(self):
        if self.discount_price >= self.original_price:
            raise ValueError(
                "Discount price must be lower than original price"
            )

        return self


product = Product(
    original_price=5000,
    discount_price=4000
)

print(product)

# The model validator compares two fields after standard validation is complete.