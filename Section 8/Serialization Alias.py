from pydantic import BaseModel, Field


class Product(BaseModel):
    product_name: str = Field(
        serialization_alias="productName"
    )

    price: float


product = Product(
    product_name="Laptop",
    price=55000
)


print(
    product.model_dump(
        by_alias=True
    )
)



# The internal field name is product_name, but serialized output uses productName.