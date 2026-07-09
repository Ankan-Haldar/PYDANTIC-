from pydantic import BaseModel, computed_field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


product = Product(
    price=500,
    quantity=3
)


print(
    product.model_dump()
)



# The computed field is automatically included in the serialized output.