from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin_code: int


class User(BaseModel):
    name: str
    age: int
    address: Address


user = User(
    name="Rahul",
    age=23,
    address={
        "city": "Kolkata",
        "state": "West Bengal",
        "pin_code": 700001
    }
)

print(user)



# The address dictionary is validated and converted into an Address model object.