from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str


class User(BaseModel):
    name: str
    address: Address


user = User(
    name="Rahul",
    address={
        "city": "Kolkata",
        "state": "West Bengal"
    }
)


print(user.model_dump())



# Nested Pydantic models are automatically converted into nested dictionaries during serialization.