from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int


product = Product(
    name="Laptop",
    price=55000,
    quantity=2
)


json_data = product.model_dump_json()

print(json_data)
print(type(json_data))



# model_dump_json() converts the model into a JSON string.