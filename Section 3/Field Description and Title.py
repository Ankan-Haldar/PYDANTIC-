from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(
        title="Product Name",
        description="The official name of the product"
    )

    price: float = Field(
        gt=0,
        title="Product Price",
        description="Product price in Indian Rupees"
    )


product = Product(
    name="Laptop",
    price=55000
)

print(product)



# The price field has a validation constraint, while the titles and descriptions provide useful metadata.