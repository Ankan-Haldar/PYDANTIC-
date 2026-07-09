from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(
        str_to_upper=True
    )

    product_code: str
    category: str


product = Product(
    product_code="lap-101",
    category="electronics"
)


print(product)


# All string values are automatically converted to uppercase.