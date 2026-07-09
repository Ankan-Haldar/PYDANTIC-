from pydantic import (
    BaseModel,
    Field,
    computed_field
)


class OrderItem(BaseModel):
    product_name: str = Field(
        serialization_alias="productName"
    )

    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


item = OrderItem(
    product_name="Laptop",
    price=55000,
    quantity=2
)


print(
    item.model_dump(
        by_alias=True
    )
)



# The output uses the serialization alias for product_name and also includes the calculated total_price field.