from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int


product = Product(
    name="Laptop",
    price="55000.50",
    quantity="2"
)

print(product)
print(type(product.price))
print(type(product.quantity))


# Pydantic validates the product data and converts compatible string values into the required numeric types.